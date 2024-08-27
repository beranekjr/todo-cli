# To-Do List CLI Application

This is a simple command-line interface (CLI) application written in Python that allows you to manage a to-do list. The application supports adding, listing, marking tasks as done, and removing tasks from the list. It also includes color-coded output for a better user experience.

## Features

- **Add Tasks**: Add a new task to your to-do list.
- **Mark Tasks as Done**: Mark a task as done using its unique ID.
- **Delete Tasks**: Remove a task from the list using its ID.
- **List Tasks**: Display all tasks in your to-do list.
- **Help**: Display a list of available commands.
- **Exit**: Safely exit the application.

## Requirements

- **Python 3.x**: Make sure you have Python 3 installed on your machine.

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/beranekjr/todo-cli.git
cd todo-cli
```

## Usage

Run the `todo.py` script to start the application:

```bash
python todo.py
```

### Available Commands

- **add `<task>`**: Add a new task to the to-do list.
- **done `<task_id>`**: Mark a task as done using its unique ID.
- **delete `<task_id>`**: Remove a task from the to-do list using its ID.
- **list**: Display all tasks in your to-do list.
- **help**: Display a list of available commands.
- **exit**: Exit the application.

### Example Usage

1. **Add a task**:

    ```bash
    $ add Buy groceries
    ```
    Output:
    ```
    Novo item adicionado a lista de afazeres.
    ID: 123456
    Detalhes: Buy groceries
    ```

2. **List tasks**:

    ```bash
    $ list
    ```
    Output:
    ```
    Lista de tarefas:
    - 123456: Buy groceries
    ```

3. **Mark a task as done**:

    ```bash
    $ done 123456
    ```
    Output:
    ```
    Item 123456 atualizado com sucesso! Parabens :)
    ```

4. **Delete a task**:

    ```bash
    $ delete 123456
    ```
    Output:
    ```
    Item 123456 successfully removido com sucesso!
    ```

5. **Exit the application**:

    ```bash
    $ exit
    ```
    Output:
    ```
    Saindo do programa...
    ```

### Handling Keyboard Interrupts

If you press `CTRL + C` while the application is running, it will safely exit and print a message:
```
Interrupção detectada! Saindo do programa...
```
