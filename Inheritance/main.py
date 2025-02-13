from E_commerce import User, Customer, Order

Alice = Customer("C001", "Alice", "alice@example.com")
Bob = Customer("C002", "Bob", "bob@example.com")

Alice.add_item_to_cart("Laptop")
Alice.add_item_to_cart("Mouse")
Bob.add_item_to_cart("Smartphone")
Bob.add_item_to_cart("Headphones")

Alice.view_cart()
Bob.view_cart()

Alice_order = Order(Alice, "O001")
Bob_order = Order(Bob, "O002")

print("\nUser Details:")
Alice.print_user_details()
Bob.print_user_details()


print("\nOrder Details:")
Alice_order.print_order_details()
Bob_order.print_order_details()