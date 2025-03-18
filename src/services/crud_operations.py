from ..database.connection import get_connection
from .ledger import log_operation

def add_inventory_item(name, category, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO inventory (name, category, quantity, price)
        VALUES (%s, %s, %s, %s)
    ''', (name, category, quantity, price))
    conn.commit()
    cursor.close()
    conn.close()
    log_operation('INSERT', name, category, None, quantity, None, price)

def get_all_inventory_items():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items

def update_inventory_item(item_id, name, category, quantity, price):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT quantity, price FROM inventory WHERE id = %s', (item_id,))
    previous_quantity, previous_price = cursor.fetchone()
    cursor.execute('''
        UPDATE inventory
        SET name = %s, category = %s, quantity = %s, price = %s
        WHERE id = %s
    ''', (name, category, quantity, price, item_id))
    conn.commit()
    cursor.close()
    conn.close()
    log_operation('UPDATE', name, category, previous_quantity, quantity, previous_price, price)

def delete_inventory_item(item_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name, category, quantity, price FROM inventory WHERE id = %s', (item_id,))
    item = cursor.fetchone()
    cursor.execute('DELETE FROM inventory WHERE id = %s', (item_id,))
    conn.commit()
    cursor.close()
    conn.close()
    log_operation('DELETE', item[0], item[1], item[2], None, item[3], None)