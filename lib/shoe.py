class Shoe:
    def __init__(self, brand, size, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")  # Print instead of raising an error
        else:
            self._size = value

    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"