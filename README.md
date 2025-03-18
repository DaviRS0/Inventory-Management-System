# Inventory Management System

This project is an Inventory Management System built using Python (Tkinter) for the graphical user interface (GUI) and PostgreSQL for the database. The system allows users to Create, Read, Update, and Delete (CRUD) inventory items and maintain a ledger that records each CRUD operation.

## Features

1. **Add a New Inventory Item**
   - Fields: Item Name, Category, Quantity, Price.

2. **Display All Inventory Items**
   - Fields: Item ID, Item Name, Category, Quantity, Price, Date Added.

3. **Update an Existing Inventory Item**
   - Fields: Item Name, Category, Quantity, Price.

4. **Delete an Inventory Item**
   - A confirmation message is displayed before deletion.

5. **Ledger System**
   - Records each CRUD operation.
   - Fields: Operation Type, Item Name, Category, Previous Quantity, New Quantity, Previous Price, New Price, Timestamp.

## Setup

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/inventory-management-system.git
   cd inventory-management-system 
   ```

2. Create a virtual environment:
```sh
python -m venv .venv
```

3. Activate the virtual environment:

- On Windows:
```sh
.\.venv\Scripts\activate
```

- On macOS/Linxus:
```sh
source .venv/bin/activate
```

4. Install the dependencies:
```sh
pip install -r requirements.txt
```

5. Configure the database connection:

Update the config.py file with your PostgreSQL database credentials:

```sh
DATABASE = {
    'host': 'your_host',
    'port': 'your_port',
    'dbname': 'your_dbname',
    'user': 'your_user',
    'password': 'your_password',
    'sslmode': 'require'
}
```

6. Run the application:
```sh
python -m src.gui.app
```

# Usage
- Add Item: Fill in the item details and click the "Add Item" button.
- Update Item: Select an item from the table, update the details, and click the "Update Item" button.
- Delete Item: Select an item from the table and click the "Delete Item" button.
- View Ledger: Click the "View Ledger" button to view the ledger history.