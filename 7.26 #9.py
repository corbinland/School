def print_triangular_numbers(n):
    for i in range(1, n + 1):
        triangular = i * (i + 1) // 2
        print(f"{i}\t{triangular}")


print_triangular_numbers(5)
