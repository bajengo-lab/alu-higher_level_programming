#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with validated size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the square's private position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the square's position after validating its value."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0
                        for num in value)):
            raise TypeError(
                "position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using #, respecting its position."""
        if self.__size == 0:
            print()
            return

        for row in range(self.__position[1]):
            print()

        for row in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
