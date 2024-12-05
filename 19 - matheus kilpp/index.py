from Funcoes import *

while True:  # Loop principal do sistema
    print("\n--- Sistema de Gerenciamento de Placas ---")
    print("1. Cadastrar uma nova placa")
    print("2. Consultar estado de emplacamento")
    print("3. Listar todas as placas")
    print("4. Atualizar registro de uma placa")
    print("5. Excluir uma placa")
    print("6. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_placa()   

    elif escolha == "2":
        consultar_placa()  

    elif escolha == "3":
        listar_placa()   

    elif escolha == "4":
        alterar_placa()   

    elif escolha == "5":
        excluir_placa()   

    elif escolha == "6":
        print("Saindo, volte sempre")
        break 
       
    else :
        print("Escolha invalida")
                       

                   
                        

    



