import sys
import random

const_add = "add"
const_done = "done"
const_delete = "delete"
const_list = "list"
const_help = "help"
const_exit = "exit"

color_blue ="\033[34m"
color_green = "\033[32m"
color_red="\033[31m"
color_white="\033[0m"

local_storage = dict()
commands = dict()

def init_commands():
    commands[const_add] = "Possibilita usuario adicionar um item a lista de afazeres"
    commands[const_done] = "Marca um item da lista de afazeres como DONE usando o ID especificado como referencia"
    commands[const_delete] = "Deleta um item da lista de afazeres usando o ID especificado como referencia"
    commands[const_list] = "Lista todos os items da lista de afazeres"
    commands[const_help] = "Lista todos os comandos disponiveis"
    commands[const_exit] = "Sai do programa"

def generate_new_id():
    return f"{random.randint(100000, 999999)}"

def add(name):
    if not name:
        print(f"{color_red}Nome do item não pode ser vazio.{color_white}")
        return

    id = generate_new_id()
    local_storage[id] = name
    print(f"{color_green}Novo item adicionado a lista de afazeres\n{color_white}")
    print(f"{color_green}ID: {id}\nDetalhes: {name}\n{color_white}")

def listTodos():
    if len(local_storage) == 0:
        print(f'Nenhum afazer adiconado ainda. Execute {color_blue}add <nome do afazer>{color_white} para comecar a adicionar novas tarefas!')
    else:
        print(f'{color_blue}Lista de tarefas:{color_white}')
        for key, value in local_storage.items():
            print(f"- {key}: {value}\n")

def mark_done(id):
    local_storage[id] = "[DONE] " + local_storage[id]
    print(f"{color_green}Item {id} atualizado com sucesso! Parabens :){color_white}")

def remove(id):
    local_storage.pop(id)
    print(f"{color_green}Item {id} removido com sucesso!{color_white}")

def listCommands():
    print(f'{color_blue}Lista de comandos:\n{color_white}')
    for key, value in commands.items():
        print(f"-{key}: {value}")

def get_input():
    choice = input("\n$ ").strip()
    return choice.split(" ")

def get_args(input):
    input.pop(0)
    return " ".join(input)

def exit():
    print(f"{color_blue}Saindo do programa...{color_white}")
    sys.exit(0)

def handle_actions(action, args):
    try:
        if action == "exit":
            exit()
        elif action == const_add:
            add(args)
        elif action == const_done:
            mark_done(args)
        elif action == const_delete:
            remove(args)
        elif action == const_list:
            listTodos()
        elif action == const_help:
            listCommands()
        else:
            print(f"{color_red}O comando especificado nao pode ser resolvido. Use help para lista de todos os comandos{color_white}")
    except KeyError:
            print(f"{color_red}Nao foi possivel achar nenhum item como o seguinte ID {args}{color_white}")

def main():
    try:
        init_commands()

        while True:
            input = get_input()
            action = input[0]
            args = get_args(input)

            handle_actions(action, args)
    except KeyboardInterrupt:
        print("\nInterrupção detectada! Saindo do programa...")
        sys.exit(0)

if __name__ == "__main__":
    main()
