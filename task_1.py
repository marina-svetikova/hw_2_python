# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# - 6782 -> 23 # - 0,56 -> 11

number = input('Введите любое число:')
sum = 0
for i in range(len(number)):
     if number [i] != '.':
        sum = sum + int(number[i])
print ((sum))
