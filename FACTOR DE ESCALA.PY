# -*- coding: cp1252 -*-
print "Programa para el calculo de Factor de Escala"
print ""
print "Desarrollado por Ing. Renny Espinosa"
print ""
print "Contacto: TLF: 507 62754615, rennyespinosa@gmail.com"
print ""
print "Introduzca las coordenadas de la Estacion"
E = input("introduzca coordenada Este: ")
N = input("introduzca coordenada Norte: ")
H = input("introduzca la Altura: ")
print ""
print ""
Y=((E-500000)*0.000001)
T= Y*Y
X= 0.9996 * (1 + 0.012289894 * T)
U= ((E-500000)*0.000001)
V=  U*U*U*U
W= 0.003*V
Z=X+W
J=(6378000+(H+30))/6378000
O=Z/J
print ""
print "FACTOR DE ESCALA ES", O
print ""
print ""
raw_input()
