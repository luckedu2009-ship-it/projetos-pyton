#Aluno1 : Padronizar nome do Filme 
def formatar (nome):
    return nome.upper()
#Aluno2 . Verificador de Idade 
def verificar_idade(idade):
   if idade >= 18:
       return "Autorizado"
   else:
       return "Nao Autorizado"
#Aluno3 : Mensagem de Retorno
def gerar_mensagem(status):
   if status == "Autorizado":
       return "Tenha uma otima sessao!"
   else: 
       return "Sentimos, mas voce nao tem a idade minima."
#Aluno4 : Execucao do Algoritmo
filme_entrada = input("Digite o filme escolhido")
idade_entrada = int(input("Digite sua Idade"))
nome_final = formatar(filme_entrada)
status_acesso = verificar_idade(idade_entrada)
mensagem = gerar_mensagem(status_acesso)
print(F"\nFilme :{nome_final}")
print(F"Status:{status_acesso}")
print(F"mensagem:{mensagem}")

