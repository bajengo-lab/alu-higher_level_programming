#!/usr/bin/python3
"""Defines a Square class with size validation and printing."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square with a validated size."""
        self.size = size

    @property
    def size(self):
        """Returns the square's private size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square's size after validating its value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character."""
        for row in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
