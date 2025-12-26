class Customer:
    def __init__(self, customer_id, name, email, balance=0.0):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.balance = balance
    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} added successfully.")
        else:
            print("Amount must be positive.")
    def purchase(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Purchase of ₹{amount} successful.")
        else:
            print("Insufficient balance.")
    def display_details(self):
        print("Customer Details")
        print("----------------")
        print(f"ID      : {self.customer_id}")
        print(f"Name    : {self.name}")
        print(f"Email   : {self.email}")
        print(f"Balance : ₹{self.balance}")
