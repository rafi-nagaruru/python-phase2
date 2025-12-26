class Alpha:
    def __init__(self, value):
        self.value = value
    def display(self):
        print("Value:", self.value)
    def is_alpha(self):
        if isinstance(self.value, str) and self.value.isalpha():
            print("The value contains only alphabets.")
        else:
            print("The value does not contain only alphabets.")
