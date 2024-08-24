class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None  # Initialize _page_count as None
        self.page_count = page_count  # Use the setter to validate page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
