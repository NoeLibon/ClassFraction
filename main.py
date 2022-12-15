from fraction_impl import Fraction


def main():
    f1 = Fraction(num=7, den=-3)
    print(f1)
    f2 = Fraction(num=1, den=4)
    print(f1 + f2)
    print(f1 - f2)
    print(f1 * f2)
    print(f1 / f2)
    print(f1 ** f2)
    print(f1 == f2)
    print(f1.__float__())
    print(f1.is_zero())
    print(f1.is_integer())
    print(f1.is_proper())
    print(f1.is_unit())
    print(f1.is_adjacent_to(f2))
    print(f1.as_mixed_number())


if __name__ == '__main__':
    main()
