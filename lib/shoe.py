#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self._color = None
        self._material = None
        self.condition = None  # Initialize condition attribute

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if isinstance(value, str) and value.strip():
            self._color = value
        else:
            raise ValueError("Color must be a non-empty string.")

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        if isinstance(value, str):
            self._material = value
        else:
            print("Material must be a string.")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"  # Set condition after repair
