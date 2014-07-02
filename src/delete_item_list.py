#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 1, 2014

@author: anroco

In python, how can remove an item from a list?

En python, ¿Como se puede eliminar una item de una lista?
'''

#create a list with different data types
lista = ['hello', False, 2, 1.0]
print (lista)

#removes the last element of the list
item = lista.pop()
print (lista)
print (item)

#removes the element at the specified index
item = lista.pop(1)
print (lista)
print (item)

#removes the element at the specified index
del lista[0]
print (lista)

#create a list from a str
lista = list('hello')
print (lista)

#removes the first item from the list whose value is passed as a parameter
lista.remove('l')
print (lista)
