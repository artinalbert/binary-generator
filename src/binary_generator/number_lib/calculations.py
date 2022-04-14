def product_of_even_numbers(n: int):
    product = 1
    for i in range(2, n+1, 2):
        product *= i
    return product
