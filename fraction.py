import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : ?
        POST : ?
        """
        if not den:
            raise ZeroDivisionError('division par zéro interdite')
        if type(num) != int or type(den) != int:
            raise TypeError('les paramètres doivent être des entiers')
        if den < 0:
            num = -num
            den = -den
        gcd = math.gcd(num, den)
        self.__numerator = num / gcd
        self.__denominator = den / gcd

    @property
    def numerator(self):
        return int(self.__numerator)

    @property
    def denominator(self):
        return int(self.__denominator)

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        if self.denominator == 1:
            return f'{self.numerator}'
        return f'{self.numerator}/{self.denominator}'

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : ?
        """
        if self.denominator == 1:
            return f'{self.numerator}'
        if abs(self.numerator) < abs(self.denominator):
            return f'{self.numerator}/{self.denominator}'
        whole_number = abs(self.numerator) // abs(self.denominator)
        new_numerator = abs(self.numerator) % abs(self.denominator)
        if self.numerator < 0:
            return f'-{whole_number}-{new_numerator}/{self.denominator}'
        return f'{whole_number}+{new_numerator}/{self.denominator}'

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions

         PRE : ?
         POST : ?
         """
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = self.numerator * (new_denominator / self.denominator) + other.numerator * (new_denominator /
                                                                                                   other.denominator)
        return Fraction(num=int(new_numerator), den=int(new_denominator))

    def __sub__(self, other):
        """Overloading of the - operator for fractions

        PRE : ?
        POST : ?
        """
        new_denominator = math.lcm(self.denominator, other.denominator)
        new_numerator = self.numerator * (new_denominator / self.denominator) - other.numerator * (new_denominator /
                                                                                                   other.denominator)
        return Fraction(num=int(new_numerator), den=int(new_denominator))

    def __mul__(self, other):
        """Overloading of the * operator for fractions

        PRE : ?
        POST : ?
        """
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(num=new_numerator, den=new_denominator)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions

        PRE : ?
        POST : ?
        """
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(num=new_numerator, den=new_denominator)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions

        PRE : ?
        POST : ?
        """
        if other.__float__() != int(other.__float__()):
            raise TypeError('les puissances de fractions ne sont pas autorisées')
        new_numerator = self.numerator ** other.__float__()
        new_denominator = self.denominator ** other.__float__()
        return Fraction(num=int(new_numerator), den=int(new_denominator))

    def __eq__(self, other):
        """Overloading of the == operator for fractions

        PRE : ?
        POST : ?
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        return not self.numerator

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        return self.denominator == 1

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        return self.numerator == 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : ?
        POST : ?
        """
        difference = self - other
        return abs(difference.numerator) == 1
