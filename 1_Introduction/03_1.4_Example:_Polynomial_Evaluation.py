"""Horner evaluation, a correctly indexed condition number and safe bisection."""
import math

def _validate_coefficients(coefficients):
    if coefficients is None or len(coefficients) == 0:
        raise ValueError("coefficients must be a non-empty sequence")
    values = [float(c) for c in coefficients]
    if not all(math.isfinite(c) for c in values):
        raise ValueError("coefficients must be finite")
    return values

def horner_method(coefficients, x):
    """Evaluate coefficients ordered from highest degree to constant term."""
    coeffs = _validate_coefficients(coefficients)
    x = float(x)
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    result = coeffs[0]
    for coeff in coeffs[1:]:
        result = result * x + coeff
    return result

def evaluate_polynomial(coefficients, x):
    """Direct power-sum evaluation; coefficients are in descending order."""
    coeffs = _validate_coefficients(coefficients)
    x = float(x)
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    degree = len(coeffs) - 1
    return sum(c * x ** (degree - i) for i, c in enumerate(coeffs))

def polynomial_condition_number(coefficients, x):
    """Relative condition number sum |a_k| |x|^k / |p(x)|."""
    coeffs = _validate_coefficients(coefficients)
    x = float(x)
    if not math.isfinite(x):
        raise ValueError("x must be finite")
    degree = len(coeffs) - 1
    numerator = sum(abs(c) * abs(x) ** (degree - i) for i, c in enumerate(coeffs))
    denominator = abs(horner_method(coeffs, x))
    if denominator == 0.0:
        return math.inf if numerator > 0.0 else math.nan
    return numerator / denominator

def polynomial_root_bisection(coefficients, low, high, tol=1e-7):
    """Find a root in a continuous sign-changing interval using bisection."""
    coeffs = _validate_coefficients(coefficients)
    low, high, tol = float(low), float(high), float(tol)
    if not all(math.isfinite(v) for v in (low, high, tol)):
        raise ValueError("interval endpoints and tolerance must be finite")
    if tol <= 0:
        raise ValueError("tol must be positive")
    if not low < high:
        raise ValueError("low must be less than high")
    f_low = horner_method(coeffs, low)
    f_high = horner_method(coeffs, high)
    if f_low == 0:
        return low
    if f_high == 0:
        return high
    if (f_low > 0 and f_high > 0) or (f_low < 0 and f_high < 0):
        raise ValueError("interval endpoints must bracket a root")
    while (high - low) / 2 > tol:
        mid = low + (high - low) / 2
        f_mid = horner_method(coeffs, mid)
        if f_mid == 0:
            return mid
        if (f_low > 0 and f_mid < 0) or (f_low < 0 and f_mid > 0):
            high, f_high = mid, f_mid
        else:
            low, f_low = mid, f_mid
    return low + (high - low) / 2

if __name__ == "__main__":
    coefficients = [2, -6, 2, -1]
    x = 3.0
    print("Horner:", horner_method(coefficients, x))
    print("Direct:", evaluate_polynomial(coefficients, x))
    print("Condition number:", polynomial_condition_number(coefficients, x))
