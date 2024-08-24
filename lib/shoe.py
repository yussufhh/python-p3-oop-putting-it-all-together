class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None  # Initialize _size as None
        self.size = size  # Use the setter to validate size
        self.condition = "Used"  # Default condition when a shoe is created

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
