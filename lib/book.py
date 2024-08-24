class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int) and value > 0:
            self._page_count = value
        else:
            raise ValueError("Page count must be a positive integer")

    def describe(self):
        return f"'{self.title}', {self.page_count} pages."
