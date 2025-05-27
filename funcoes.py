def adicionar_tarefa(tarefas):
    nova_tarefa = str(input("Digite a nova tarefa: "))
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")



def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")



def concluir_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    listar_tarefas(tarefas)
    
    try:
        indice_tarefa = int(input("Digite o índice da tarefa concluída: "))
        
        if "✔" not in tarefas[indice_tarefa - 1]:
            tarefas[indice_tarefa - 1] += " ✔"
            print("Tarefa marcada como concluída!")
        
        else:
            print("Essa tarefa já está marcada como concluída.")
    
    except (ValueError, IndexError):
        print("Índice inválido. Tente novamente.")


def deletar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    listar_tarefas(tarefas)
    
    try:
        indice_tarefa = int(input("Digite o índice da tarefa que deseja deletar: "))
        
        tarefas.pop(indice_tarefa - 1)
    
    except (ValueError, IndexError):
        print("Índice inválido. Tente novamente.")
