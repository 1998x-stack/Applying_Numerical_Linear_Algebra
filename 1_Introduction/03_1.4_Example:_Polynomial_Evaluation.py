# 03_1.4_Example:_Polynomial_Evaluation

"""
Lecture: /1_Introduction
Content: 03_1.4_Example:_Polynomial_Evaluation
"""

def horner_method(coefficients: list, x: float) -> float:
    """
    使用Horner方法计算多项式在x处的值
    :param coefficients: 多项式系数列表，从最高次到常数项
    :param x: 计算点
    :return: 多项式在x处的值
    """
    result = coefficients[0]
    for coeff in coefficients[1:]:
        result = result * x + coeff
    return result

def evaluate_polynomial(coefficients: list, x: float) -> float:
    """
    使用直接求值法计算多项式在x处的值
    :param coefficients: 多项式系数列表，从最高次到常数项
    :param x: 计算点
    :return: 多项式在x处的值
    """
    result = 0
    for i, coeff in enumerate(coefficients):
        result += coeff * (x ** (len(coefficients) - 1 - i))
    return result

# 比较两种方法的结果
coefficients = [2, -6, 2, -1]  # 2x^3 - 6x^2 + 2x - 1
x = 3
horner_result = horner_method(coefficients, x)
direct_result = evaluate_polynomial(coefficients, x)

print(f"Horner方法结果: {horner_result}")
print(f"直接求值法结果: {direct_result}")
print(f"误差: {abs(horner_result - direct_result)}")

def polynomial_condition_number(coefficients: list, x: float) -> float:
    """
    计算多项式在x处的条件数
    :param coefficients: 多项式系数列表，从最高次到常数项
    :param x: 计算点
    :return: 多项式在x处的条件数
    """
    polynomial_value = horner_method(coefficients, x)
    sum_of_terms = sum(abs(coeff * (x ** i)) for i, coeff in enumerate(coefficients))
    return sum_of_terms / abs(polynomial_value)

condition_number = polynomial_condition_number(coefficients, x)
print(f"多项式在x={x}处的条件数: {condition_number}")


def polynomial_root_bisection(coefficients: list, low: float, high: float, tol: float = 1e-7) -> float:
    """
    使用二分法求解多项式的零点
    :param coefficients: 多项式系数列表，从最高次到常数项
    :param low: 区间下限
    :param high: 区间上限
    :param tol: 收敛阈值
    :return: 零点
    """
    while (high - low) / 2 > tol:
        mid = (low + high) / 2
        f_low = horner_method(coefficients, low)
        f_mid = horner_method(coefficients, mid)
        if f_mid == 0:
            return mid
        elif f_low * f_mid < 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2

root = polynomial_root_bisection(coefficients, 0, 3)
print(f"多项式的零点: {root}")
