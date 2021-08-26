def main():
    
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "
    pass

edad=int(input("Ingresa tu edad: "))


if edad < 18:
   print("No cumples requisitos")  
if edad < 0:
    print("Respuesta incorrecta")   

if edad >= 18:
    identi =str(input("¿Tienes identificación oficial? (s/n): ")) 

    if identi == "n":
        print("No cumples requisitos") 

    elif identi == "s":
        print("Trámite de licencia concedido")
        
    else: 
        print("Respuesta incorrecta")
      
 

if __name__ == '__main__':
    main()
