def string_treatment(raw_equation):
    try:
        raw_equation = raw_equation.upper()
        raw_equation = raw_equation.replace(" ", "")
        raw_equation = (raw_equation.replace("X^2", "X*X").
                        replace("X^1", "X").replace("X^0", "1"))
        if '^' in raw_equation:
            print("I can't solve equation with degree that are not 0, 1 or 2.")
            raise IOError
        raw_equation = raw_equation.replace("X", "*1*X")
        raw_equation = (raw_equation.replace("+*", "+").
                        replace("-*", "-").replace("**", "*"))
        raw_equation = raw_equation.replace("-", "+-")
        eq_a, eq_b = raw_equation.split('=')
    except (ValueError, IOError):
        return None, None
    return eq_a, eq_b


def get_coef(liste):
    coef = 1
    float_list = [float(x) for x in liste if x != "X" and x != '']
    for x in float_list:
        coef *= x
    return coef


def reduce_equation(raw_equation):
    coef_array = [0, 0, 0]
    try:
        eq_a, eq_b = string_treatment(raw_equation)
        if (eq_a, eq_b) == (None, None):
            return None
        list_a = [item.split("*") for item in eq_a.split("+") if item != '']
        list_b = [item.split("*") for item in eq_b.split("+") if item != '']

        for item in list_a:
            degree = item.count("X")
            coef_array[degree] += get_coef(item)

        for item in list_b:
            degree = item.count("X")
            coef_array[degree] -= get_coef(item)
    except Exception as err:
        print(err)
        return None
    return coef_array
