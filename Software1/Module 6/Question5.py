def filter_even_numbers(numbers):
    n = []
    for i in numbers:
        if i % 2 == 0 :
            n.append(i)
    return n

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = filter_even_numbers(numbers)
print(f"Original list: {numbers}")
print(f'List with even numbers only: {even}')
