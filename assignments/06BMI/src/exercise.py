def main():
    # Escribe el código adecuado para completar el programa
        pass

    
peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))




if peso > 0 and altura >0:
    altura = altura * altura
    ind = (peso / altura)

    if ind < 20:

        x = ind
        x = str("PESO BAJO")

    if 20 <= ind < 25:
        x = ind
        x = ("NORMAL")	

    if 25 <= ind < 30:	
        x = ind
        x = ("SOBREPESO")

    if 30 <= ind < 40:	
        x = ind
        x = str("OBESIDAD")

    if ind >= 40:
        x = ind
        x= str("OBESIDAD MORBIDA")
    
    print(x)

else: 
    print("Revisa tus datos, alguno de ellos es erróneo.")    



if __name__ == '__main__':
    main()
