#!/usr/bin/python3
"""define Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        """Init Rectangle"""
        self.__width = width
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """sadasdoasodaso"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self, value):
        """adsaodasoda"""
        return self.__height

    @height.setter
    def height(self, value):
        """asdasdasdasd"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """adasdasdasoa"""
        return (self.__width * self.__height)

    def perimeter(self):
        """asdasdasd"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
