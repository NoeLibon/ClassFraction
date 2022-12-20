import math


class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : num et den sont des entiers
        POST : crée le numérateur et le dénominateur sous leur forme simplifiée
        RAISES : ZeroDivisionError si den est égal 0
        """
        pass

    @property
    def numerator(self):
        pass

    @property
    def denominator(self):
        pass

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction

        PRE : self est un objet de type Fraction
        POST : la fonction renvoie une string du numérateur si le
        dénominateur = 1, sinon il renvoie une string de la fraction simplifiée à son maximum
        """
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator} / {self.denominator}"

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : self est un objet de type Fraction
        POST : renvoie une string du numérateur si le dénominateur = 1,
        renvoie une string de la fraction réduite si la valeur absolue du numérateur est plus petite que la valeur
        absolue du dénominateur, sinon renvoie le nombre mixte de la fraction
        """

        if self.denominator == 1:
            return f'Voici le resultat : {self.numerator}'
        elif abs(self.numerator) < abs(self.denominator):  # ABS donne la valeur absolue
            return f'Voici le resultat : {self.numerator} / {self.denominator}'

        partie_entiere = abs(self.numerator) // abs(self.denominator)
        reste_fraction = abs(self.numerator) % abs(self.denominator)
        if self.numerator < 0:
            return f'Voici le resultat : - {partie_entiere} - {reste_fraction} / {self.denominator}'
        else:
            return f'Voici le resultat : {partie_entiere} + {reste_fraction} / {self.denominator}'

    # ------------------ Operators overloading ------------------

    def __add__(self, autre):
        """Overloading of the + operator for fractions


        PRE : self et autre sont des objets de type Fraction
        POST : renvoie la somme de self et autre sous forme d'un objet de type Fraction
        """
        nouv_den = math.lcm(self.denominator, autre.denominator)
        nouv_num = self.numerator * (nouv_den / self.denominator) + autre.numerator * (nouv_den / autre.denominator)
        nouv_frac = nouv_num / nouv_den
        if nouv_frac == int(nouv_frac):
            return int(nouv_frac)
        else:
            return nouv_frac

    def __sub__(self, autre):
        """Overloading of the - operator for fractions

        PRE : self et autre sont des objets de type Fraction
        POST : renvoie la différence de self et autre sous forme d'un objet de type Fraction
        """
        nouv_den = math.lcm(self.denominator, autre.denominator)
        nouv_num = self.numerator * (nouv_den / self.denominator) - autre.numerator * (nouv_den / autre.denominator)
        nouv_frac = nouv_num / nouv_den
        if nouv_frac == int(nouv_frac):
            return int(nouv_frac)
        else:
            return nouv_frac

    def __mul__(self, autre):
        """Overloading of the * operator for fractions

        PRE : self et autre sont des objets de type Fraction
        POST : renvoie la multiplication de self et autre sous forme d'un objet de type Fraction
        """
        nouv_den = self.denominator * autre.denominator
        nouv_num = self.numerator * autre.numerator
        nouv_frac = nouv_num / nouv_den
        if nouv_frac == int(nouv_frac):
            return int(nouv_frac)
        else:
            return nouv_frac

    def __truediv__(self, autre):
        """Overloading of the / operator for fractions

        PRE : self et autre sont des objets de type Fraction
        POST : renvoie une instance Fraction qui correspond à la division de l'objet self par l'objet autre
        """
        pass

    def __pow__(self, autre):
        """Overloading of the ** operator for fractions

        PRE : self et autre sont des objets de type Fraction
        POST : renvoie la puissance de self par autre sous forme d'un objet de type Fraction
        """
        nouv_den = self.denominator ** (autre.numerator / autre.denominator)
        nouv_num = self.numerator ** (autre.numerator / autre.denominator)
        nouv_frac = nouv_num / nouv_den
        if nouv_frac == int(nouv_frac):
            return int(nouv_frac)
        else:
            return nouv_frac

    def __eq__(self, autre):
        """Overloading of the == operator for fractions

        PRE : self et autre sont des objets de type Fraction
        POST : renvoie "égal" si le numérateur de self et autre
        sont égaux et si le dénominateur de self et autre sont égaux, sinon renvoie "pas égal"
        """
        if self.numerator == autre.numerator and self.denominator == autre.denominator:
            return "égal"
        else:
            return "pas égal"

    def __float__(self):
        """Returns the decimal value of the fraction

        PRE : self est un objet de type Fraction
        POST : retourne le résultat de la fraction
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0

        PRE : self est un objet de type Fraction
        POST : renvoie "vaut 0" si le numérateur = 0 sinon renvoie "ne vaut pas 0"
        """
        if self.numerator == 0:
            return "vaut 0"
        else:
            return "ne vaut pas 0"

    def is_integer(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : self est un objet de type Fraction
        POST : renvoie "entier" si le dénominateur = 1 sinon renvoie "pas entier"
        """
        if self.denominator == 1:
            return "entier"
        else:
            return "pas entier"

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : self est un objet de type Fraction
        POST : renvoie "propre" si la valeur absolue du numérateur est plus
        petite que la valeur absolue du dénominateur, sinon renvoie "pas propre"
        """
        if abs(self.numerator) < abs(self.denominator):
            return "propre"
        else:
            return "pas propre"

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : self est un objet de type Fraction
        POST : renvoie "is unit" si la valeur du numérateur est = à 1, sinon renvoie "is not unit"
        """
        if self.numerator == 1:
            return "is unit"
        else:
            return "is not unit"

    def is_adjacent_to(self, autre):
        """Check if two fractions differ by a unit fraction

        Two fractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : self et autre sont des objets de type Fraction
        POST : crée une instance Fraction qui correspond à la
        différence de l'objet self et de l'objet autre, et renvoie "adjacent" si la valeur absolue du numérateur de
        cette différence est égal à 1, sinon renvoie "n'est pas adjacent"
        """
        pass
