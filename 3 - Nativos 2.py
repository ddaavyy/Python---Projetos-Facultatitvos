"""

Bem-Vindo ao meu código :D


"""

from datetime import datetime
from collections import OrderedDict

def add_task(tasks, task):
    # Adicionar uma nova tarefa com a data de criação.
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tasks[len(tasks) + 1] = {'task': task, 'done': False, 'created': timestamp}

def list_tasks(tasks):
    # Listar todas as tarefas.
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    else:
        for number, task_info in tasks.items():
            status = "Concluída" if task_info['done'] else "Pendente"
            print(f"{number}. {task_info['task']} - {status} (Criada em: {task_info['created']})")

def remove_task(tasks, task_number):
    # Remover uma tarefa pelo número.
    if task_number in tasks:
        del tasks[task_number]
    else:
        print("Número de tarefa inválido.")
    # Reorganizar os números das tarefas
    tasks = OrderedDict((i+1, v) for i, (k, v) in enumerate(tasks.items()))

def mark_task_done(tasks, task_number):
    # Marcar uma tarefa como concluída.
    if task_number in tasks:
        tasks[task_number]['done'] = True
    else:
        print("Número de tarefa inválido.")

def main():
    tasks = OrderedDict()
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Marcar Tarefa como Concluída")
        print("5. Sair")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            task = input("Digite a tarefa: ")
            add_task(tasks, task)
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            if len(tasks) > 0:
                task_number = int(input("Digite o número da tarefa a ser removida: "))
                remove_task(tasks, task_number)
            else:
                print("Não há tarefas anotadas.")
        elif choice == '4':
            if len(tasks) > 0:
                task_number = int(input("Digite o número da tarefa a ser marcada como concluída: "))
                mark_task_done(tasks, task_number)
            else:
                print("Não há tarefas anotadas.")
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

print("Bem-vindo a minha lista de deveres em Python.")
main()
