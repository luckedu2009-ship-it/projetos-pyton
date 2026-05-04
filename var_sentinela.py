#Exemplo de uso da variavel sentinela 
while True: 
 comando = input("Digite um Comando - Para parar digite 'sair'")
 if comando == "sair":
   break 
print(f"Executando:{comando}")
