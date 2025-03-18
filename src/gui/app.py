import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from src.services.crud_operations import add_inventory_item, get_all_inventory_items, update_inventory_item, delete_inventory_item
from src.services.ledger import get_ledger_history

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.configure(bg="#2e2e2e")  # Set dark background color
        
        # Add item form
        self.name_label = tk.Label(root, text="Item Name", bg="#2e2e2e", fg="white")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.category_label = tk.Label(root, text="Category", bg="#2e2e2e", fg="white")
        self.category_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.quantity_label = tk.Label(root, text="Quantity", bg="#2e2e2e", fg="white")
        self.quantity_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.price_label = tk.Label(root, text="Price", bg="#2e2e2e", fg="white")
        self.price_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Buttons
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item, bg="#4CAF50", fg="white")
        self.add_button.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        self.update_button = tk.Button(root, text="Update Item", command=self.update_item, bg="#2196F3", fg="white")
        self.update_button.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

        self.delete_button = tk.Button(root, text="Delete Item", command=self.delete_item, bg="#f44336", fg="white")
        self.delete_button.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

        self.ledger_button = tk.Button(root, text="View Ledger", command=self.view_ledger, bg="#FF9800", fg="white")
        self.ledger_button.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        # Inventory table
        self.inventory_tree = ttk.Treeview(root, columns=("ID", "Name", "Category", "Quantity", "Price", "Date Added"), show="headings")
        self.inventory_tree.heading("ID", text="ID")
        self.inventory_tree.heading("Name", text="Name")
        self.inventory_tree.heading("Category", text="Category")
        self.inventory_tree.heading("Quantity", text="Quantity")
        self.inventory_tree.heading("Price", text="Price")
        self.inventory_tree.heading("Date Added", text="Date Added")
        self.inventory_tree.grid(row=6, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.refresh_inventory_list()

        # Configure grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(6, weight=1)

    def add_item(self):
        name = self.name_entry.get()
        category = self.category_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        add_inventory_item(name, category, quantity, price)
        self.refresh_inventory_list()
        messagebox.showinfo("Success", "Item added successfully")

    def update_item(self):
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected")
            return
        item_id = self.inventory_tree.item(selected_item)["values"][0]
        name = self.name_entry.get()
        category = self.category_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())
        update_inventory_item(item_id, name, category, quantity, price)
        self.refresh_inventory_list()
        messagebox.showinfo("Success", "Item updated successfully")

    def delete_item(self):
        selected_item = self.inventory_tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "No item selected")
            return
        item_id = self.inventory_tree.item(selected_item)["values"][0]
        item_name = self.inventory_tree.item(selected_item)["values"][1]
        category = self.inventory_tree.item(selected_item)["values"][2]
        quantity = self.inventory_tree.item(selected_item)["values"][3]
        price = self.inventory_tree.item(selected_item)["values"][4]
        
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this item?")
        if confirm:
            delete_inventory_item(item_id)
            self.refresh_inventory_list()
            messagebox.showinfo("Success", "Item deleted successfully")

    def refresh_inventory_list(self):
        for item in self.inventory_tree.get_children():
            self.inventory_tree.delete(item)
        items = get_all_inventory_items()
        for item in items:
            self.inventory_tree.insert("", tk.END, values=item)

    def view_ledger(self):
        ledger_window = tk.Toplevel(self.root)
        ledger_window.title("Ledger History")
        ledger_tree = ttk.Treeview(ledger_window, columns=("ID", "Operation Type", "Item Name", "Category", "Previous Quantity", "New Quantity", "Previous Price", "New Price", "Timestamp"), show="headings")
        ledger_tree.heading("ID", text="ID")
        ledger_tree.heading("Operation Type", text="Operation Type")
        ledger_tree.heading("Item Name", text="Item Name")
        ledger_tree.heading("Category", text="Category")
        ledger_tree.heading("Previous Quantity", text="Previous Quantity")
        ledger_tree.heading("New Quantity", text="New Quantity")
        ledger_tree.heading("Previous Price", text="Previous Price")
        ledger_tree.heading("New Price", text="New Price")
        ledger_tree.heading("Timestamp", text="Timestamp")
        ledger_tree.pack(fill=tk.BOTH, expand=True)
        history = get_ledger_history()
        for record in history:
            ledger_tree.insert("", tk.END, values=record)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()