# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 01:35:47 2026

@author: Artur Z
"""
#Тут будем использовать использовать разные возможности функции print
spisok = list(("TVP1", "TVP2","TVP", "Polsat", "BBC", "HBO", "MTV")) #Двойные скобки нужны чтобы указать больше 1 жлемента в списке
#показываем просто список 
print(spisok)
#Показываем список, разделенный точкой с запятой
print("TVP1", "TVP2","TVP", "Polsat", "BBC", "HBO", "MTV", sep=';')
#В качестве сепаратора можно использовать например текст 
print("I like Computers", "TVP1", "TVP2","TVP", "Polsat", "BBC", "HBO", "MTV", sep=' But better is ')
#В качестве сепаратора попробуем использовать переменную
separator = " but better is "
print("I like Computers", "TVP1", "TVP2","TVP", "Polsat", "BBC", "HBO", "MTV", sep=separator)
#функция принт распознает также код ascii 
print("\u03c8")
#Функция принт можен не только что то показывать на экране, но и издавать звуки 
print("\a")