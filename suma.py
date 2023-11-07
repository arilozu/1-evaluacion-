#Este programa suma los 100 primeros números enteros. ¿Te enteras?
 def suma():
num_final=input( "Dime hasta qué numero quieres que sume: ")
suma()
suma_acumulada=0 #Es una variable que acumula la suma for cont in range(1, int(num_final)+1):
#print( Esta vez cont= "+str(cont))
suma_acumulada=suma_acumulada+cont
print("SUMA ACUMULADA = "+str( suma_acumulada))
