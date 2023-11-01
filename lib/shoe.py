#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition = None):
        self._size = size
        self.contion = condition
        self.brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if isinstance(value, int) and value > 0:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
