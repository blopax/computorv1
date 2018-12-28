import parser
import utils


def equation_info(coefficient):
    reduced_form = ""
    polynomial_deg = 0
    for power in range(len(coefficient)):
        if coefficient[power] != 0:
            polynomial_deg = power
            reduced_form += "+ {} * X^{}".format(coefficient[power], power)
    if reduced_form == "":
        reduced_form = "0 * X^0"
    reduced_form = reduced_form.strip('+ ') + " = 0"
    print("Reduced form: {}".format(reduced_form))
    print("Polynomial degree: {}".format(polynomial_deg))
    return polynomial_deg


def second_degree_solver(a, b, c, show):
    sol, sol1, sol2 = None, None, None
    delta = b ** 2 - 4 * a * c
    if show != 0:
        print("Discriminant is equal to: {}".format(delta))
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
    return sol, sol1, sol2


def first_degree_solver(b, c):
    sol = None
    if b != 0:
        sol = -c / b
        print("The solution is:\n{}".format(sol))
    elif c == 0:
        sol = "Inf"
        print("There is an infinity of solutions: all R is solution")
    else:
        print("There is no solution")
    return sol


def solver(coefficient, show):
    polynomial_degree = equation_info(coefficient)
    if polynomial_degree > 2:
        print("The polynomial degree is strictly greater than 2, I can't solve.")
    else:
        c, b, a = coefficient[0], coefficient[1], coefficient[2]
        if a != 0:
            second_degree_solver(a, b, c, show)
        else:
            first_degree_solver(b, c)


if __name__ == "__main__":
    try:
        equation, show_delta = utils.get_args()
        coefficient_array = parser.reduce_equation(equation)
        if coefficient_array is None:
            raise IOError
        solver(coefficient_array, show_delta)
    except AssertionError:
        print("Please provide equation.")
    except IOError:
        print("Please enter valid equation format.")
