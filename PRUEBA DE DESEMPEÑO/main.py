from inventory import add_product, view_products, update_product_simple, delete_product, save_inventory_csv, load_inventory_csv
from sales import register_sale, view_sales, save_sales_csv, load_sales_csv
from reports import top_products, sales_by_author, income_report, inventory_performance

def main():
    while True:
        print("\n--- ELECTRONICS STORE SYSTEM ---")
        print("1. Add product")
        print("2. View products")
        print("3. Update product")
        print("4. Delete product")
        print("5. Register sale")
        print("6. View sales history")
        print("7. Report: Top products")
        print("8. Report: Sales by author")
        print("9. Report: Income")
        print("10. Report: Inventory performance")
        print("11. Save inventory CSV")
        print("12. Load inventory CSV")
        print("13. Save sales CSV")
        print("14. Load sales CSV")
        print("0. Exit")

        option = input("Choose an option: ")

        try:
            if option == "1": add_product()
            elif option == "2": view_products()
            elif option == "3": update_product_simple()
            elif option == "4": delete_product()
            elif option == "5": register_sale()
            elif option == "6": view_sales()
            elif option == "7": top_products()
            elif option == "8": sales_by_author()
            elif option == "9": income_report()
            elif option == "10": inventory_performance()
            elif option == "11": save_inventory_csv()
            elif option == "12": load_inventory_csv()
            elif option == "13": save_sales_csv()
            elif option == "14": load_sales_csv()
            elif option == "0":
                print("Exiting system...")
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print("Unexpected error:", e)
            print("Returning to menu.")

main()
