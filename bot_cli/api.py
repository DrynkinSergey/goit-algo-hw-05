from colorama import Fore


def errors_handler(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except IndexError:
            print(f"{Fore.RED} [Error] {Fore.RESET} Please enter the params")
        except ValueError:
            print(
                f"{Fore.RED} [Error] {Fore.RESET}Parameters is not correct... Example 'add Olena 0932223355 ")
    return wrapper


def greetings():
    print("Welcome to CLI assistant 🔥")


@errors_handler
def add_contact(args, contacts):
    name, phone = args
    contacts.append({'name': name, 'phone': phone})
    print(f"{Fore.GREEN} [Info] {Fore.RESET} Contact has been added!")


@errors_handler
def change_contact(args, contacts):
    name, phone = args
    for index, item in enumerate(contacts):
        if item['name'] == name:
            contacts[index] = {**contacts[index], 'phone': phone}
    print(f"{Fore.GREEN} [Info] {Fore.RESET} Contact has been updated!")


@errors_handler
def delete_contact(args, contacts):
    name = args[0]
    if (len(contacts) == 0):
        print(f"{Fore.RED} [Warning] {Fore.RESET} Contacts is empty!")
    for index, item in enumerate(contacts):
        if item['name'] == name:
            del contacts[index]
        else:
            print(f"{Fore.RED} [Info] {Fore.RESET} Contact is not exists")
        print(f"{Fore.GREEN} [Info] {Fore.RESET} Contact has been updated!")


def help():
    print("Available commands: \n")
    print("- add name number")
    print("- update name number ")
    print("- delete name")
    print("- all (saw all contacts) \n")
