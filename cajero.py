import os



menuinicio=("""bienvenido al cajero automatico eliga la opcion que desea:
\n1. consultar saldo
\n2. depositar dinero
\n3. retirar dinero
\n0. salir """)

saldo=100000



isActive=True
while isActive:
    os.system ("cls")
    
    print(menuinicio)
    
    try:
     opcion=int(input("\n seleciones una opcion 0-3: "))
     match opcion:
        case 0:
           
           print("gracias por usar nuestros servicos")
           os.system("pause")
           isActive = False
        case 1:
           
           print(f" tu saldo es de: {saldo}")
           os.system("pause")
        case 2:
           
           sumado=float(input("cuanto desea depositar: "))
           saldo=sumado+saldo
           print(f"has ingrsado: {sumado} tu saldo ahora es de: {saldo} ")
           os.system("pause")
        case 3:
         try:
             restando = float(input("Cuánto desea retirar:  "))
                
             if restando > saldo:
                 print("Fondos insuficientes. No puede retirar más de lo que tiene.")
                 os.system("pause")
             elif restando >= 0:
                saldo=saldo-restando
                print(f"suted retiro: {restando} su saldo ahora es de  {saldo} ")
                os.system("pause")
             else:
                 
                 print("error")
                 os.system("pause")
            
         except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
                os.system("pause")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        os.system("pause")
            
    
    
   