import sys
from funcoes import * 
tarefas = []

def main():
    print("----------GERENCIADOR DE TAREFAS----------")
    
    while True:
        opcao = str(input('''
    [1] Adicionar tarefa
    [2] Listar Tarefas
    [3] Marcar tarefa como concluída
    [4] Deletar Tarefa
    [5] Sair
    
Selecione uma opção: '''))
        
        match opcao:
            case "1":
                adicionar_tarefa(tarefas)
            
            case "2":
                listar_tarefas(tarefas)
            
            case "3":
                concluir_tarefa(tarefas)
            
            case "4":
                deletar_tarefa(tarefas)
            
            case "5":
                sys.exit("Encerrando aplicação...")
            
            case _:
                print("Digite uma opção válida.")



if __name__ == "__main__":
    main()