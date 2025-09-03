def filter_even_numbers(integers):
    evens = []
    for i in range(0, len(integers)):
        number = integers[i]
        if number % 2 == 0:
            evens.append(number)
        #print(evens)
    return evens

numbers = [1,2,3,4,5,6,7,8,9]
evenNumbers = filter_even_numbers(numbers)
print(numbers)
print(evenNumbers)