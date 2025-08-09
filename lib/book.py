#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    # title property
    def get_title(self):
        return self._title

    def set_title(self, value):
        if isinstance(value, str):
            self._title = value
        else:
            print("Title must be a string.")

    title = property(get_title, set_title)

    # page_count property
    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    # extra method (optional for reading)
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
