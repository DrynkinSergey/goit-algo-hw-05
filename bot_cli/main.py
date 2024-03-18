from api import add_contact, change_contact, delete_contact, help, greetings
from tabulate import tabulate


def command_parser(input_str):
    try:
        command, *args = input_str.lower().split()
        return command, *args
    except (TypeError, ValueError):
        print('Command is empty string...Try again!')


def main():
    contacts = list()
    exit_commands = ['q', 'quit', 'exit', 'leave', 'left']
    print('Welcome to assistant bot! You can use "help" command to see more')
    while True:
        params = input('>>>  ')
        if not params:
            continue
        command, *args = command_parser(params)

        match(command):
            case 'hello':
                greetings()
            case 'add':
                add_contact(args, contacts)
            case 'update':
                change_contact(args, contacts)
            case 'delete':
                delete_contact(args, contacts)
            case 'all':
                print(tabulate(contacts, headers="keys", tablefmt="pretty"))
            case 'help':
                help()
            case command if command in exit_commands:
                print('Bye!')
                break
            case _:
                print('Invalid command! Try again...\n')


if __name__ == '__main__':
    main()
