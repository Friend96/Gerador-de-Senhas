import random
caracterias = ["!","@","#","$","{","}","(",")","[","]","/","-","+","*",".",",","#","|","<",">","_","?","&",":",";","%"]
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","Ç"]
senha = ""

while True:
    verificar = {
        'letra':0,
        'numero':0,
        'carac':0
    }
    valor = input("Número de caracteres: ")

    if(len(valor) == 0 or int(valor) < 4):
        print("\033[0;33m O número é invalido \033[m")
    else:
        for c in range(1,int(valor)+1):
            aleatorio = random.randint(1,10)
            if(aleatorio <= 4 and aleatorio > 0):
                aleatorio_letras = random.randint(1,2)
                verificar["letra"] += 1
                if(aleatorio_letras == 1):
                    up = alfabeto[random.randint(0,len(alfabeto)-1)]
                    
                    senha += f'{up.upper()}'
                if(aleatorio_letras == 2):
                    small = alfabeto[random.randint(0,len(alfabeto)-1)]
                    senha += f'{small.lower()}'

            if(aleatorio <= 8 and aleatorio > 4):
                verificar["numero"] += 1
                numero = random.randint(0,9)
                senha += f'{numero}'

            if(aleatorio <= 10 and aleatorio > 8):
                verificar["carac"] += 1
                caracteria = random.randint(0,len(caracterias)-1)
                senha += f'{caracterias[caracteria]}'
        
        print(f'tem {verificar["numero"]} numeros, {verificar["letra"]} letras e {verificar["carac"]} caracteres especiais.')
        print(f'\033[1;32m {senha} \033[m')
        break