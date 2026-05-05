from db import get_db
from werkzeug.security import generate_password_hash, check_password_hash


# ── USERS ──────────────────────────────────────────────────────────────────────

def create_user(username, password):
    hashed_pw = generate_password_hash(password)
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s)",
                (username, hashed_pw)
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def find_user(username, password):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, username, password FROM users WHERE username = %s",
                (username,)
            )
            user = cur.fetchone()
    finally:
        conn.close()
    if user and check_password_hash(user['password'], password):
        return {'id': user['id'], 'username': user['username']}
    return None


def get_user_by_id(user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, username FROM users WHERE id = %s",
                (user_id,)
            )
            return cur.fetchone()
    finally:
        conn.close()


# ── EXPENSES ───────────────────────────────────────────────────────────────────

def get_expenses(user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, expense_name, amount, category, notes, created_at
                FROM expenses
                WHERE user_id = %s
                ORDER BY created_at DESC
                """,
                (user_id,)
            )
            rows = cur.fetchall()
    finally:
        conn.close()

    result = []
    for row in rows:
        r = dict(row)
        if hasattr(r['created_at'], 'isoformat'):
            r['created_at'] = r['created_at'].isoformat()
        result.append(r)
    return result


def create_expense(expense_name, price, category, notes, user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO expenses (expense_name, amount, category, notes, user_id)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id
                """,
                (expense_name, price, category, notes, user_id)
            )
            new_id = cur.fetchone()['id']
        conn.commit()
        return new_id
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def delete_expense(expense_id, user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM expenses WHERE id = %s AND user_id = %s",
                (expense_id, user_id)
            )
            deleted = cur.rowcount > 0
        conn.commit()
        return deleted
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def update_expense(expense_id, user_id, expense_name, price, category, notes):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE expenses
                SET expense_name = %s,
                    amount       = %s,
                    category     = %s,
                    notes        = %s
                WHERE id = %s AND user_id = %s
                """,
                (expense_name, price, category, notes, expense_id, user_id)
            )
            updated = cur.rowcount > 0
        conn.commit()
        return updated
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


# ── NET WORTH ──────────────────────────────────────────────────────────────────

def get_net_worth_history(user_id):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT month, assets, liabilities
                FROM net_worth
                WHERE user_id = %s
                ORDER BY month ASC
                """,
                (user_id,)
            )
            rows = cur.fetchall()
        return [dict(r) for r in rows]
    finally:
        conn.close()


def create_net_worth_entry(user_id, month, assets, liabilities):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO net_worth (user_id, month, assets, liabilities)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id, month)
                DO UPDATE SET assets      = EXCLUDED.assets,
                              liabilities = EXCLUDED.liabilities
                """,
                (user_id, month, assets, liabilities)
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()


def delete_net_worth_entry(user_id, month):
    conn = get_db()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "DELETE FROM net_worth WHERE user_id = %s AND month = %s",
                (user_id, month)
            )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()