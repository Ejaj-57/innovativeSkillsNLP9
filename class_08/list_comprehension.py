numbers = [1,2,3,4]

square = [n*n for n in numbers]
square1 = [numbers[i]*numbers[i] for i in range(len(numbers))]
print(numbers)
print(square)
print(square1)


