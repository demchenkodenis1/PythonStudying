#Урок 2. Задача №3
#Узнайте у пользователя число n.
#Найдите сумму чисел n + nn + nnn.
#Например, пользователь ввёл число 3.
#Считаем 3 + 33 + 333 = 369.

n = input("Введите число: ");
n2 = int(n*2);
n3 = int(n*3);
nSum = (int(n) + n2 + n3);
print("Сумма чисел: " + n + " + " + str(n2) + " + " + str(n3) + " равна %d" % nSum);

