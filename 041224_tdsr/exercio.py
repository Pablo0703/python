num= int(input(" Escreva um numero inteiro"))
resultado = ""

resto = num % 16
num = num // 16
#quoc = num // 16
resultado =str(resto) + resultado 

resto = num % 16
num = num // 16

resultado =str(resto) + resultado 


resto = num % 16
num = num // 16

resultado = str(resto) + resultado 
print(resultado)

