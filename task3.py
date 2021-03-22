list_names = ['процент', 'процента', 'процентов']
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
user_answer = 1
if user_answer in list_numbers[0:1]:
    print(user_answer, list_names[0])
user_answer = 3
if user_answer in list_numbers[1:4]:
    print(user_answer, list_names[1])
user_answer = 13
if user_answer in list_numbers[4:20]:
    print(user_answer, list_names[2])
user_answer_next = int(input('Введите число от 1 до 20 '))
if user_answer_next in list_numbers[0:1]:
    print(user_answer_next, list_names[0])
if user_answer_next in list_numbers[1:4]:
    print(user_answer_next, list_names[1])
if user_answer_next in list_numbers[4:20]:
    print(user_answer_next, list_names[2])