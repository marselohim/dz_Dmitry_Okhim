numbers = []
count = 0
digit = 0
first_sum = 0
second_sum = 0
for elem in range(1001):
    if elem % 2 != 0:
        numbers.append(elem **3)
for elem in numbers:
    number = elem
    while number > 0:
        digit = number % 10
        count += digit
        number = number // 10
    if count % 7 == 0:
        first_sum += elem
    count = 0
for el in range(len(numbers)):
    numbers[el] += 17
for elem in numbers:
    number = elem
    while number > 0:
        digit = number % 10
        count += digit
        number = number // 10
    if count % 7 == 0:
        second_sum += elem
    count = 0
print(first_sum)
print(second_sum)