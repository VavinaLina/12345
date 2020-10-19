import random 
import math 
import os
import time

clear = lambda: os.system('clear')
def menu():
    print('Здравствуйте, выберите напиток!')
    lis =["Эспрессо","Американо","Латте","Капучино","Раф","Гляссе"]
    price = [70,100,200,190,220,210]
    a=0
    print("{0:1} - {1:15} - {2:4}".format("№ ", "Название напитка", "Цена"))
    while a<=5:
        print("{0:2d} - {1:16} - {2:d} рублей".format(a+1, lis[a], price[a]))
        a=a+1    
    x=int(input())
    clear()
    print("Вы выбрали напиток №{}, пожалуйста внесите {} рублей.".format(x,price[x-1]))
    mon=int(input())
    if mon<price[x-1]:
        print("Недостаточно средств, внесите {} рублей.".format(price[x-1]-mon))
        input()
    elif mon>price[x-1]:
        print("Заберите сдачу в размере {} рублей.".format(mon-price[x-1]))
    print("Пожалуйста подождите, напиток будет готовиться 10 секунд.")
    progress=""
    for i in range(10):
        time.sleep(1)
        clear()
        progress=progress+"."
        print("[",progress,"]")
    time.sleep(2)
    clear()
    print("Ваш напиток готов! Спасибо за ожидание.")
    time.sleep(3)
    clear()
    print("Хотите ли вы сделать еще заказ? Если да, то нажмите 1, если нет, то нажмите 2")
    A=int(input())
    if A==1:
        print("Хорошо!")
        menu()
    elif A==2:
        print("Хорошо, возвращайтесь скорее!")
menu()
