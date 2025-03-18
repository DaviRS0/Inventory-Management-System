from database.models import create_tables

if __name__ == "__main__":
    create_tables()
    from gui.app import InventoryApp
    import tkinter as tk

    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()