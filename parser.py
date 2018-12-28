import re


def replace_power(raw_equation):
    pattern = r'X\^([0-9])*'
    power_list = re.findall(pattern, raw_equation)
    if '' in power_list:
        return None
    raw_equation = raw_equation.replace('X^0', '*1')
    for power in power_list:
        raw_equation = raw_equation.replace("X^" + power, "X" * int(power))
    return raw_equation


def string_treatment(raw_equation):
    try:
        raw_equation = raw_equation.upper()
        raw_equation = raw_equation.replace(" ", "")
        raw_equation = replace_power(raw_equation)
        if raw_equation is None:
            print("Format error.")
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
    try:
        eq_a, eq_b = string_treatment(raw_equation)
        if (eq_a, eq_b) == (None, None):
            return None
        length = eq_a.count('X') + eq_b.count('X') + 1
        if length < 3:
            length = 3
        coef_array = [0] * length
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
