import json


def carregar_tarefas_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_tarefa_arquivo(nome_arquivo, tarefas):
    with open(nome_arquivo, 'w') as f:
        json.dump(tarefas, f)


def adicionar_tarefa(tarefas):
    descricao = input('Descrição da tarefa: ')
    tarefa = {'descricao': descricao, 'completa': False}
    tarefas.append(tarefa)
    print('Tarefa adicionada com sucesso!')


def lista_de_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
        return
    print('Lista de Tarefas:')
    for i, tarefa in enumerate(tarefas):
        print(f"{i+1}. {tarefa['descricao']:30} [{'' if tarefa['completa'] else 'Não '}Concluída]")


def editar_tarefa(tarefas):
    lista_de_tarefas(tarefas)
    try:
        indice = int(input('Digite o número da tarefa que deseja editar: '))
        tarefa = tarefas[indice-1]
        descricao = input(f'Nova descrição para "{tarefa["descricao"]}": ')
        tarefa['descricao'] = descricao
        print('Tarefa atualizada com sucesso!')
    except (IndexError, ValueError):
        print('Tarefa não encontrada.')


def remover_tarefa(tarefas):
    lista_de_tarefas(tarefas)
    try:
        indice = int(input('Digite o número da tarefa que deseja remover: '))
        tarefa = tarefas.pop(indice-1)
        print(f'Tarefa "{tarefa["descricao"]}" removida com sucesso!')
    except (IndexError, ValueError):
        print('Tarefa não encontrada.')


def tarefa_completada(tarefas):
    lista_de_tarefas(tarefas)
    try:
        indice = int(input('Digite o número da tarefa que deseja marcar como concluída: '))
        tarefa = tarefas[indice-1]
        tarefa['completa'] = True
        print(f'Tarefa "{tarefa["descricao"]}" marcada como concluída com sucesso!')
    except (IndexError, ValueError):
        print('Tarefa não encontrada.')


def ordenar_tarefas(tarefas):
    tarefas.sort(key=lambda x: (not x['completa'], x['descricao'].lower()))
    print('Tarefas ordenadas com sucesso!')