# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 02:49:24 2026

@author: Artur Z
"""
#если мы запишем число как текст, можем с ним проводить различные операции
smthLikeNumber = '1000'
print(smthLikeNumber)
#Пробуем добавить единицу 
int(smthLikeNumber) + 1 #лишняя команда, можно сделать все под функциуй вывода
print(int(smthLikeNumber) + 1)
#теперь попробуем добавить единицу, но в качестве текста 
print(smthLikeNumber + str(1))
#задание 4
#Большой текст нужно выделять тремя апострофами с обоих сторон, если это будут кавычки, сойдет за комментарий 
article = '''Monty Python, grupa Monty Pythona, Pythoni –
zespół twórców i gwiazd telewizyjnego serialu komediowego
Latający cyrk Monty Pythona, założony 
pod koniec lat 60. XX wieku w Anglii. 
W skład grupy wchodziło sześciu komików: 
Graham Chapman, John Cleese, Terry Gilliam, Eric Idle,
Terry Jones i Michael Palin.'''
print(article)
#теперь напишем только большими буквами
print(article.upper())
#поиграемся с текстом 
print(article.lower().replace("monty", "FLYING"))
#попробуем разбить текст на составляющие
print(article.split(" "))
#попробуем найти сколько раз встречается какое то конкретное слово в данном тексте
print('Word python appears',article.lower().count('python'),'times')
#Поаробуем вывести специальные знаки не используя код ascii
print('To print the \\ you need to put \\ twice in your text like this: \\\\')
#Нужно помнить что слеш понимает после себя только один знак, поэтому что бы написать два слеша подрят нужно искользовать 4
#Попробуем другие знаки
print("\"The best hits of \'80s!!!\"")
print('\'The best hits of \'80s!!!\'')
#По всей видимости дял функции принт, не имеет особого значения апостроф это или кавычки
#Попробуем написать таблицу используя принт 
amountPLN = 234
print('cur\t','exchange\t','amount')
print('USD\t','3.65\t',amountPLN / 3.65)
print('EUR\t','4.23\t',amountPLN / 4.23)
#Сделаем то же самое только менее читабельную версию
print('cur\t','exchange\t','amount\nUSD\t','3.65\t',amountPLN / 3.65,'\nEUR\t','4.23\t',amountPLN / 4.23)
#Теперь попробуем конвертировать текст в другие типы данных и проводить с ними операции
valueAsText = '123.45'
factor = 1.23
print('value is ',valueAsText,'factor is',factor,'value*factor=',float(valueAsText) * factor)
