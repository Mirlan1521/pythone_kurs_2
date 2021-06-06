from random import randrange

number = randrange(10)

vvod = -1
kolichestvo = 0

while vvod != number:
    vvod = int(input("Введите ваше число   "))
    kolichestvo += 1
    if vvod > number:
        print("введено число больше попытайся еще раз")
    elif vvod < number:
        print("введено число меньше попытайся еще раз")

print("Ураа ты угадал число")