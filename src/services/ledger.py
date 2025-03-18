from ..database.connection import get_connection

def log_operation(operation_type, item_name, category, previous_quantity, new_quantity, previous_price, new_price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO ledger (operation_type, item_name, category, previous_quantity, new_quantity, previous_price, new_price)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (operation_type, item_name, category, previous_quantity, new_quantity, previous_price, new_price))
    conn.commit()
    cursor.close()
    conn.close()

def get_ledger_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ledger ORDER BY timestamp DESC')
    history = cursor.fetchall()
    cursor.close()
    conn.close()
    return history