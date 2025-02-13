class User:
    def __init__(self, user_id: str, name: str):
        self._user_id = user_id
        self._name = name

    def print_user_details(self):
        print(f"User ID: {self._user_id}, Name: {self._name}")
        

class Customer(User):
    def __init__(self, user_id: str, name: str, email: str):
        super().__init__(user_id, name)
        self._email = email
        self._cart = []

    def add_item_to_cart(self, item: str):
        self._cart.append(item)

    def view_cart(self):
        print(f"{self._name}'s Cart: {', '.join(self._cart)}")

class Order(Customer):
    def __init__(self, customer: Customer, order_id: str):
        super().__init__(customer._user_id, customer._name, customer._email)
        self._order_id = order_id
        self._order_details = customer._cart.copy()
        customer._cart.clear()

    def print_order_details(self):
        print(f"Order ID: {self._order_id}")
        self.print_user_details()
        print(f"Email: {self._email}")
        print(f"Ordered Items: {', '.join(self._order_details)}\n")