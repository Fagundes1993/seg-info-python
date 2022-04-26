import os ##Importa o módulo ou biblioteca os (integra os programas e recursos do S.O)

print("#" * 60) ##Imprimeindo o # 60 vezes
ip_ou_host = input("Digite o ip ou host a ser verificado: ") #criação da variável que vai receber do usuário um ip
print("_" * 60) ##Imprimeindo o _ 60 vezes
os.system('ping -n 6 {}'.format(ip_ou_host)) #chamando system da biblioteca os - comando ping
print("_" * 60) ##Imprimeindo o _ 60 vezes
