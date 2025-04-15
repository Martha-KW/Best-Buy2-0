import store
import products

# Setup initial stock of inventory
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def list_products(store):
    """This function prints a listing of all products that are available at Best
    Buy including the name, the price and the quantity of the products."""
    print("------")
    products = store.get_all_products()
    if products:
        for idx, product in enumerate(products, 1):
            print(
                f"{idx}. {product.name}, Price: ${product.price},"
                f" Quantity: {product.get_quantity()}")
    else:
        print("No active products in the store.")
    print("------")
    return True


def show_total_number(store):
    """This function prints the total amount of products in store regardless of what
    instance it is and what price it has."""
    total = store.get_total_quantity()
    print(f"\nTotal of {total} items in store.\n")
    return True


def make_order(store):
    """This function simulates the ordering process in the simulated Best Buy store."""
    print("\n------")
    products = store.get_all_products()
    if not products:
        print("No active products in the store.")
        return True

    for idx, product in enumerate(products, start=1):
        print(f"{idx}. {product.name}, Price: ${product.price},"
              f" Quantity: {product.get_quantity()}")
    print("------")

    order_items = []

    while True:
        print("When you want to finish order, enter empty text.")
        choice = input("Which product # do you want?: ").strip()
        if not choice:
            break

        if not choice.isdigit() or not (1 <= int(choice) <= len(products)):
            print("Invalid input. Please enter a valid product number.")
            continue

        product_index = int(choice) - 1
        selected_product = products[product_index]

        amount = input(
            f"What amount do you want of {selected_product.name}? "
        ).strip()
        if not amount.isdigit() or int(amount) <= 0:
            print("Invalid amount. Please enter a positive number.")
            continue

        amount = int(amount)
        if selected_product.get_quantity() < amount:
            print("Not enough stock available.")
            continue

        order_items.append((selected_product, amount))
        print("Product added to list!")

    if order_items:
        total_price = store.order(order_items)
        print("********")
        print(f"Order made! Total payment: ${total_price}")
        print("********")
    else:
        print("No items were ordered.")

    return True



def quit_best_buy(store):
    """This function is the exit door for the shop and interrupts the while True loop."""
    print("Thanks for your visit at Best Buy. Goodbye!")
    return False


# function dispatcher for scalability of the online shop
func_dict = {
    1: list_products,
    2: show_total_number,
    3: make_order,
    4: quit_best_buy,
}


def start(store):
    """This function prints and controls the CLI menu and processes user input."""
    while True:
        print("\n   Store Menu ")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        user_choice = input("Please choose a number: ")

        if not user_choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        user_choice = int(user_choice)
        if user_choice in func_dict:
            if not func_dict[user_choice](store):
                break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    """This function initializes the whole process of shopping at Best Buy."""
    start(best_buy)
