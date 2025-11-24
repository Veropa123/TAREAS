# ---------------- INVENTORY MODULE ----------------


import csv

inventory = {
    1: {"name": "Libro la Divina Comedia", "author": "Dante Aligueri", "category": "Mitologia Griega", "price": 80000, "stock": 25, "warranty": 1},
    2: {"name": "Libro la Iliada", "author": "Homero", "category": "Mitologia Griega", "price": 50000, "stock": 15, "warranty": 1},
    3: {"name": "Libro Doce Cuentos Peregrinos", "author": "Gabriel Garcia Marquez", "category": "Fantasia", "price": 30000, "stock": 30, "warranty": 1},
    4: {"name": "Libro Cien años de soledad ", "author": "Gabriel Garcia Marquez", "category": "Fantasia", "price": 100000, "stock": 50, "warranty": 1},
    5: {"name": "Libro El amor en los tiempos del colera", "author": "Gabriel Garcia Marquez", "category": "romance, fantasia", "price": 35000, "stock": 10, "warranty": 1},
}


# ---------------- CRUD ----------------

def add_product():     #se adicciona producto y se le asigna id en numero 
    try:
        new_id = max(inventory.keys()) + 1
        name = input("Product name: ")
        author= input("Author: ")
        category = input("Category: ")
        price = float(input("Unit price: "))
        stock = int(input("Stock quantity: "))
        warranty = int(input("Warranty (months): "))

        inventory[new_id] = {
            "name": name,
            "author": author,
            "category": category,
            "price": price,
            "stock": stock,
            "warranty": warranty
        }

        print("Product added successfully.")
    except Exception:
        print("Invalid input. Product not added.")

def view_products():        # se visualiza el inventario hasta el momento
    print("\n--- INVENTORY LIST ---")
    for pid, data in inventory.items():
        print(pid, "->", data)

def update_product_simple():    # buscar y actualizar cualquier informacion del archivo, el da la opcion 
    try:
        keyword = input("Enter product name or keyword: ").lower()
        match_id = None

        for pid, product in inventory.items():
            if keyword in product["name"].lower():
                match_id = pid
                break

        if match_id is None:
            print("Product not found.")
            return

        print(f"Found: {inventory[match_id]['name']} (ID: {match_id})")

        field = input("Field to update (name/author/category/price/stock/warranty): ").lower()
        if field not in inventory[match_id]:
            print("Invalid field.")
            return
        
        if field == "price":
            inventory[match_id][field] = float(input("New price: "))
        elif field in ("stock", "warranty"):
            inventory[match_id][field] = int(input(f"New {field}: "))
        else:
            inventory[match_id][field] = input(f"New {field}: ")

        print("Product updated successfully.")

    except Exception:
        print("Error updating product.")

def delete_product():   #elimina el producto que llamemos del inventario por nombre
    try:
        keyword = input("Enter product name or keyword to delete: ").lower()
        match_id = None

        for pid, product in inventory.items():
            if keyword in product["name"].lower():
                match_id = pid
                break

        if match_id is None:
            print("Product not found.")
            return

        del inventory[match_id]
        print("Product deleted.")

    except:
        print("Error deleting product.")

        # ---------------- CSV EXPORT / IMPORT ----------------

def save_inventory_csv(ruta="inventory.csv"):    # se crea archivo CSV y guarda la información 
    try:
        with open(ruta, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "author", "category", "price", "stock", "warranty"])

            for pid, p in inventory.items():
                writer.writerow([pid, p["name"], p["author"], p["category"], p["price"], p["stock"], p["warranty"]])

        print("Inventory saved successfully.")
    except Exception:
        print("Error saving inventory file.")

import csv

def load_inventory_csv(path="inventory.csv"):     # Busca el archivo CSV en carpeta y sube la informacion a python para poderla modificar

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            inventory = []
            for row in reader:
                inventory.append({
                    "name": row["name"],
                    "author": row["author"],
                    "category": row["category"],
                    "price": float(row["price"]),
                    "stock": int(row["stock"]),
                    "warranty": int(row["warranty"])
                })
        return inventory
    except FileNotFoundError:
        print("Inventory CSV not found.")
        return []