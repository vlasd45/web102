#Задание 1
def palin(text):
    able = ''.join(text.split()).lower()
    return able == able[::-1]
print(palin(input("Введите строку . . . ")))
#Задание 2
def registration(name, second_name, father_name, age: int):
    string = f"{name} {second_name} {father_name} {2023 - age} г.р. зарегестрирован"
    return string 
print(registration("Владислав" , "Крапивин" , "Артёмович" , 16))
#Задание 3
def my_max(a, b, c = 0):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c
print(f"Максимальное число: {my_max(53,25,64)}")
