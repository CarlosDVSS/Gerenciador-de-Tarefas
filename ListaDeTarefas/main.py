from tarefas import adicionar_tarefa, lista_de_tarefas, editar_tarefa, remover_tarefa, tarefa_completada, ordenar_tarefas, salvar_tarefa_arquivo, carregar_tarefas_arquivo


def main():
    tarefas = carregar_tarefas_arquivo('tarefas.json')
    while True:
        print("\n=== Gerenciador de tarefas ===")
        print("1 - Adicionar tarefa")
        print("2 - Ver tarefas")
        print("3 - Editar tarefa")
        print("4 - Excluir tarefa")
        print("5 - Marcar tarefa como concluída")
        print("6 - Ordenar tarefas")
        print("0 - Salvar e sair")
        escolha = input("Escolha uma opção: ")

        if escolha not in ['0', '1', '2', '3', '4', '5', '6']:
            print('Opção inválida, tente novamente!')
            continue
        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            lista_de_tarefas(tarefas)
        elif escolha == "3":
            editar_tarefa(tarefas)
        elif escolha == "4":
            remover_tarefa(tarefas)
        elif escolha == "5":
            tarefa_completada(tarefas)
        elif escolha == "6":
            ordenar_tarefas(tarefas)
        elif escolha == "0":
            salvar_tarefa_arquivo('tarefas.json', tarefas)
            print('Até mais!')
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == '__main__':
    main()
