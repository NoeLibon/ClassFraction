import unittest
from fraction_impl import Fraction


class FractionTestCase(unittest.TestCase):
    def test_as_mixed_number(self):
        self.assertEqual(Fraction(num=12, den=3).as_mixed_number(), '4')
        self.assertEqual(Fraction(num=12, den=5).as_mixed_number(), '2+2/5')
        self.assertEqual(Fraction(num=-12, den=15).as_mixed_number(), '-4/5')

    def test_add(self):
        self.assertEqual((Fraction(num=5, den=6) + Fraction(num=4, den=7)).__str__(), '59/42')
        self.assertEqual((Fraction(num=7, den=-8) + Fraction(num=-4, den=-7)).__str__(), '-17/56')
        self.assertEqual((Fraction(num=0, den=42) + Fraction(num=13, den=25)).__str__(), '13/25')

    def test_sub(self):
        self.assertEqual((Fraction(num=5, den=6) - Fraction(num=4, den=7)).__str__(), '11/42')
        self.assertEqual((Fraction(num=7, den=-8) - Fraction(num=-4, den=-7)).__str__(), '-81/56')
        self.assertEqual((Fraction(num=0, den=42) - Fraction(num=13, den=25)).__str__(), '-13/25')

    def test_mul(self):
        self.assertEqual((Fraction(num=5, den=6) * Fraction(num=4, den=7)).__str__(), '10/21')
        self.assertEqual((Fraction(num=7, den=-8) * Fraction(num=-4, den=-7)).__str__(), '-1/2')
        self.assertEqual((Fraction(num=0, den=42) * Fraction(num=13, den=25)).__str__(), '0')

    def test_truediv(self):
        self.assertEqual((Fraction(num=5, den=6) / Fraction(num=4, den=7)).__str__(), '35/24')
        self.assertEqual((Fraction(num=7, den=-8) / Fraction(num=-4, den=-7)).__str__(), '-49/32')
        self.assertEqual((Fraction(num=0, den=42) / Fraction(num=13, den=25)).__str__(), '0')

    def test_pow(self):
        with self.assertRaises(TypeError):
            (Fraction(num=5, den=6) ** Fraction(num=4, den=7)).__str__()
        with self.assertRaises(TypeError):
            (Fraction(num=7, den=-8) ** Fraction(num=-4, den=-7)).__str__()
        self.assertEqual((Fraction(num=0, den=42) ** Fraction(num=13, den=25)).__str__(), '0')
        self.assertEqual((Fraction(num=5, den=6) ** Fraction(num=2, den=1)).__str__(), '25/36')

    def test_eq(self):
        self.assertTrue(Fraction(num=4, den=5) == Fraction(num=24, den=30))
        self.assertTrue(Fraction(num=4, den=5) == Fraction(num=-44, den=-55))
        self.assertTrue(Fraction(num=-4, den=5) == Fraction(num=4, den=-5))

    def test_float(self):
        self.assertEqual(Fraction(num=4, den=5).__float__(), 0.8)
        self.assertEqual(Fraction(num=-40, den=25).__float__(), -1.6)
        self.assertEqual(Fraction(num=-0, den=-144).__float__(), 0)
        self.assertEqual(Fraction(num=144, den=-12).__float__(), -12)


if __name__ == '__main__':
    unittest.main()
