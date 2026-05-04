from flask import request, session, jsonify, render_template
import psycopg2
from db import get_db
from models import (
    create_user, find_user,
    create_expense, delete_expense, update_expense,
    get_expenses, get_user_by_id,
    create_net_worth_entry, get_net_worth_history, delete_net_worth_entry,
)


def register_routes(app):

    # ── INDEX ──────────────────────────────────────────────
    @app.route('/')
    def index():
        return render_template('index.html')

    # ── AUTH ───────────────────────────────────────────────
    @app.route('/signup', methods=['POST'])
    def signup():
        data = request.get_json()
        try:
            create_user(data.get('username'), data.get('password'))
            return jsonify({"message": "Account created successfully!"}), 201
        except psycopg2.IntegrityError:
            return jsonify({"error": "User exists"}), 409

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        result = find_user(data.get('username'), data.get('password'))
        if result:
            session.permanent = True
            session['user_id'] = result['id']
            session['username'] = result['username']
            return jsonify({"status": "Logged in successfully!"}), 200
        return jsonify({"error": "Invalid login, please check credentials!"}), 401

    @app.route('/logout', methods=['POST'])
    def logout():
        session.clear()
        return jsonify({"status": "Logged out"}), 200

    @app.route('/me')
    def me():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        user = get_user_by_id(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"id": user['id'], "username": user['username']}), 200

    # ── EXPENSES ───────────────────────────────────────────
    @app.route('/expenses', methods=['GET'])
    def list_expenses():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        rows = get_expenses(user_id)
        return jsonify(rows), 200

    @app.route('/expenses', methods=['POST'])
    def add_expense():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        data = request.get_json()
        name     = data.get('expense_name', '').strip()
        amount   = data.get('amount')
        category = data.get('category', 'Other')
        notes    = data.get('notes', '')
        if not name or amount is None:
            return jsonify({"error": "expense_name and amount are required"}), 400
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return jsonify({"error": "amount must be a number"}), 400
        new_id = create_expense(name, amount, category, notes, user_id)
        return jsonify({"id": new_id, "message": "Expense created"}), 201

    @app.route('/expenses/<int:expense_id>', methods=['PUT'])
    def edit_expense(expense_id):
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        data = request.get_json()
        name     = data.get('expense_name', '').strip()
        amount   = data.get('amount')
        category = data.get('category', 'Other')
        notes    = data.get('notes', '')
        if not name or amount is None:
            return jsonify({"error": "expense_name and amount are required"}), 400
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return jsonify({"error": "amount must be a number"}), 400
        updated = update_expense(expense_id, user_id, name, amount, category, notes)
        if not updated:
            return jsonify({"error": "Expense not found or not yours"}), 404
        return jsonify({"message": "Expense updated"}), 200

    @app.route('/expenses/<int:expense_id>', methods=['DELETE'])
    def remove_expense(expense_id):
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        deleted = delete_expense(expense_id, user_id)
        if not deleted:
            return jsonify({"error": "Expense not found or not yours"}), 404
        return jsonify({"message": "Expense deleted"}), 200

    # ── NET WORTH ──────────────────────────────────────────
    @app.route('/net-worth', methods=['GET'])
    def list_net_worth():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        rows = get_net_worth_history(user_id)
        return jsonify(rows), 200

    @app.route('/net-worth', methods=['POST'])
    def save_net_worth():
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        data = request.get_json()
        month  = data.get('month')       # "YYYY-MM"
        assets = data.get('assets')
        liab   = data.get('liabilities')
        if not month or assets is None or liab is None:
            return jsonify({"error": "month, assets, and liabilities are required"}), 400
        try:
            assets = float(assets)
            liab   = float(liab)
        except (TypeError, ValueError):
            return jsonify({"error": "assets and liabilities must be numbers"}), 400
        create_net_worth_entry(user_id, month, assets, liab)
        return jsonify({"message": "Net worth entry saved"}), 201

    @app.route('/net-worth/<month>', methods=['DELETE'])
    def remove_net_worth(month):
        """month is YYYY-MM, e.g. /net-worth/2025-04"""
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({"error": "Not authenticated"}), 401
        delete_net_worth_entry(user_id, month)
        return jsonify({"message": "Entry removed"}), 200
