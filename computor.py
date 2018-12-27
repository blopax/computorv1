import sys

from parser import reduce_equation

# cleaner  unitest? "X^2 = X^  assez moche


def print_equation_info(coef):
    reduced_form = ""
    polynomial_deg = 0

    if coef[0] != 0:
        reduced_form += "{} * X^0 ".format(coef[0])
    if coef[1] != 0:
        polynomial_deg = 1
        reduced_form += "+ {} * X^1 ".format(coef[1])
    if coef[2] != 0:
        polynomial_deg = 2
        reduced_form += "+ {} * X^2 ".format(coef[2])
    if reduced_form == "":
        reduced_form = "0 * X^0"
    reduced_form = reduced_form.strip('+ ') + " = 0"
    print("Reduced form: {}".format(reduced_form))
    print("Polynomial degree: {}".format(polynomial_deg))


def second_degree_solver(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        sol1 = (-b - delta ** (1/2)) / (2 * a)
        sol2 = (-b + delta ** (1/2)) / (2 * a)
        print("Discriminant is strictly positive, the two solutions are:"
              "\n{}\n{}".format(sol1, sol2))
    if delta == 0:
        sol = -b / (2 * a)
        print("Discriminant equals zero, the solution is:\n{}".format(sol))
    if delta < 0:
        sol1 = (-b - 1j * (-delta) ** (1/2)) / (2 * a)
        sol2 = (-b + 1j * (-delta) ** (1/2)) / (2 * a)
        print("Discriminant is strictly negative, the two solutions are:"
              "\n{}\n{}".format(sol1, sol2))


def first_degree_solver(b, c):
    if b != 0:
        print("The solution is:\n{}".format(-c / b))
    elif c == 0:
        print("There is an infinity of solutions: all reals are solutions")
    else:
        print("There is no solution")


def solver(coef):
    c, b, a = coef[0], coef[1], coef[2]
    if a != 0:
        second_degree_solver(a, b, c)
    else:
        first_degree_solver(b, c)


if __name__ == "__main__":
    try:
        assert len(sys.argv) > 1
        if len(sys.argv) == 2:
            args = sys.argv[1]
        else:
            args = ''.join(sys.argv[1:])
        coef_array = reduce_equation(args)
        if coef_array is None:
            raise IOError
        print_equation_info(coef_array)
        solver(coef_array)

    except AssertionError:
        print("Please provide equation.")
    except IOError:
        print("Please enter valid equation format.")
