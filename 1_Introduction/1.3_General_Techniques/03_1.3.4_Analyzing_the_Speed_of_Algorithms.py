"""Theory-only performance estimates; no hardware benchmark is implied."""
def matmul_flops(n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    return 2 * n ** 3

def minimum_matrix_bytes(n, bytes_per_value=8):
    """Idealized one-read-A, one-read-B, one-write-C traffic lower bound."""
    if n < 1 or bytes_per_value < 1:
        raise ValueError("n and bytes_per_value must be positive")
    return 3 * n * n * bytes_per_value

def arithmetic_intensity_lower_bound(n, bytes_per_value=8):
    return matmul_flops(n) / minimum_matrix_bytes(n, bytes_per_value)

if __name__ == "__main__":
    for n in (32, 128, 512):
        print(n, "FLOPs:", matmul_flops(n),
              "idealized bytes:", minimum_matrix_bytes(n),
              "FLOP/byte:", arithmetic_intensity_lower_bound(n))
