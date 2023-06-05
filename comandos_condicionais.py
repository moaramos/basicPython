# -*- coding: utf-8 -*-

#condicionais básicos
a = 2; b = 3; c = 4

if a > b:
	print("'a' é maior que 'b'")
else:
	print("'b' é maior que 'a'")

print("--------\n")

#comando elif (cai no primeiro que der "True")
if a == b:
	print("numeros iguais")
elif a > b:
	print("'a' é maior que 'b'")
else:
	print("numeros sao diferentes")
