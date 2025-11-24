# sales.py 

from inventory import inventory
sales_history = []

# Discount rules by customer type
discounts = {
    "regular": 0.00,
    "premium": 0.10,
    "vip": 0.20
}

def register_sale():
    """
    Interactive sale registration. Validates inputs and appends a clean record
    to sales_history. Returns True on success, False otherwise.
    """
    try:
        customer = input("Customer name: ").strip()
        if not customer:
            print("Customer name cannot be empty.")
            return False

        cust_type = input("Customer type (regular/premium/vip): ").strip().lower()
        if cust_type not in discounts:
            print("Unknown customer type. Defaulting to 'regular'.")
            cust_type = "regular"

        # Search by name/keyword (keeps current behavior)
        keyword = input("Product name or keyword: ").strip().lower()
        matches = [(pid, p) for pid, p in inventory.items() if keyword in p["name"].lower()]

        if not matches:
            print("No matching products found.")
            return False

        if len(matches) > 1:
            print("\nMatching products:")
            for i, (pid, p) in enumerate(matches, start=1):
                print(f"{i}. {p['name']} (Author: {p['author']}, Price: {p['price']}, Stock: {p['stock']})")
            try:
                choice = int(input("Select an option number: ")) - 1
                if choice < 0 or choice >= len(matches):
                    print("Invalid selection.")
                    return False
                prod_id, product = matches[choice]
            except ValueError:
                print("Invalid selection.")
                return False
        else:
            prod_id, product = matches[0]

        # Quantity
        try:
            qty = int(input("Quantity: "))
            if qty <= 0:
                print("Quantity must be a positive integer.")
                return False
        except ValueError:
            print("Invalid quantity.")
            return False

        if product["stock"] < qty:
            print("Insufficient stock.")
            return False

        # Apply discount using lambda (kept as requirement)
        discount = discounts.get(cust_type, 0.0)
        calc_total = lambda price, q: round(price * q * (1 - discount), 2)

        total = calc_total(product["price"], qty)

        # Update inventory
        inventory[prod_id]["stock"] -= qty
        # Optionally keep a sold counter: add field 'sold' if desired
        if "sold" in inventory[prod_id]:
            inventory[prod_id]["sold"] += qty
        else:
            inventory[prod_id]["sold"] = qty

        # Append a normalized sale record (types ensured)
        sale_record = {
            "customer": str(customer),
            "type": str(cust_type),
            "product": str(product["name"]),
            "author": str(product["author"]),
            "qty": int(qty),
            "discount": float(discount),
            "total": float(total)
        }
        sales_history.append(sale_record)
        print("Sale registered successfully.")
        return True

    except Exception as e:
        # No crash: report error and return False
        print(f"Unexpected error registering sale: {e}")
        return False


def view_sales():
    """
    Prints the sales history in a human-readable, defensive format.
    Skips entries that are obviously invalid but reports them.
    """
    if not sales_history:
        print("No sales recorded yet.")
        return

    print("\n--- SALES HISTORY ---")
    bad_count = 0
    for s in sales_history:
        try:
            customer = s.get("customer", "<unknown>")
            cust_type = s.get("type", "<unknown>")
            product = s.get("product", "<unknown>")
            author = s.get("author", "<unknown>")

            # Validate numeric fields and coerce if possible
            qty = s.get("qty", 0)
            if isinstance(qty, (float, str)) and not isinstance(qty, int):
                qty = int(qty) if str(qty).isdigit() else None
            discount = s.get("discount", 0.0)
            total = s.get("total", 0.0)

            if qty is None or not isinstance(qty, int):
                raise ValueError("Invalid qty")

            discount = float(discount)
            total = float(total)

            print(f"Customer: {customer} | Type: {cust_type} | Product: {product} | Author: {author} | Qty: {qty} | Discount: {discount:.2f} | Total: ${total:.2f}")

        except Exception:
            bad_count += 1
            print("Invalid sale record skipped:", s)

    if bad_count > 0:
        print(f"\nNote: {bad_count} invalid sale record(s) were skipped.")
    print()

        
def save_sales_csv(ruta="sales_history.csv"):
    import csv

    if not sales_history:
        print("No sales to save.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Encabezado correcto
            writer.writerow(["customer", "type", "product", "author", "qty", "discount", "total"])

            for sale in sales_history:
                writer.writerow([
                    sale["customer"],
                    sale["type"],
                    sale["product"],
                    sale["author"],
                    sale["qty"],
                    sale["discount"],
                    sale["total"]
                ])

        print(f"Sales history saved successfully to {ruta}")

    except PermissionError:
        print("Permission denied: cannot write to this file.")
    except Exception as e:
        print(f"Unexpected error while saving sales CSV: {e}")

def load_sales_csv(ruta="sales_history.csv"):
    import csv

    try:
        with open(ruta, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader)

            expected = ["customer", "type", "product", "author", "qty", "discount", "total"]
            if header != expected:
                print("Invalid header. Expected:", ", ".join(expected))
                return

            sales_history.clear()  # reiniciar ventas

            for row in reader:
                if len(row) != 7:
                    print("Invalid row skipped:", row)
                    continue

                try:
                    customer = row[0]
                    cust_type = row[1]
                    product = row[2]
                    author = row[3]
                    qty = int(row[4])
                    discount = float(row[5])
                    total = float(row[6])

                    sales_history.append({
                        "customer": customer,
                        "type": cust_type,
                        "product": product,
                        "author": author,
                        "qty": qty,
                        "discount": discount,
                        "total": total
                    })

                except ValueError:
                    print("Invalid values in row:", row)
                    continue

        print("Sales history loaded successfully.")

    except FileNotFoundError:
        print("Sales CSV file not found.")
    except Exception as e:
        print(f"Unexpected error loading sales CSV: {e}")