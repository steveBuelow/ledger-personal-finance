from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    hashed_pw = generate_password_hash(password)  # never store plaintext passwords
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_pw)
            )
        conn.commit()  # required to persist the insert

def find_user(username, password):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, password FROM users WHERE username = %s",
                (username,)  # note: single-item tuple needs trailing comma
            )
            user = cur.fetchone()
    if user and check_password_hash(user['password'], password):  # colon!
        return user['id']
    return None

def create_expense(expense_name, price, category, notes, user_id):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO expenses (expense_name, amount, category, notes, user_id) VALUES (%s, %s, %s, %s, %s)",
                (expense_name, price, category, notes, user_id)  # params must match %s count
            )
        conn.commit()

def delete_expense(expense_id, user_id):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM expenses WHERE id = %s AND user_id = %s",  # IDOR protection
                (expense_id, user_id)
            )
        conn.commit()

def update_expense(expense_id, user_id, expense_name, price, category, notes):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE expenses
                SET expense_name=%s, amount=%s, category=%s, notes=%s
                WHERE id=%s AND user_id=%s
                """,
                (expense_name, price, category, notes, expense_id, user_id)
            )
        conn.commit()