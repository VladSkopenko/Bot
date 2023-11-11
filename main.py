def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print(f"Enter user name, pls")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("Index")

    return inner


users = {}


def hello():
    return print("How can I help you?")


def normalize(name):
    new_name = name.lower().strip()
    return new_name

@input_error
def add(name_and_phone):
    split_value = name_and_phone.split()
    if len(split_value) == 3:
        name = split_value[1]
        phone_number = split_value[2]
        if name.lower() not in users.keys():
            users[name] = phone_number
        else:
            print(f"Контакт с именем:{name} уже существует")


def change(name_and_phone):
    split_val = name_and_phone.split()
    if len(split_val) == 3:
        name = split_val[1]
        phone_numb = split_val[2]
        if name.lower() in users.keys():
            users[name] = phone_numb
        else:
            print(f"Контакт с именем:{name} не существует")


@input_error
def phone(name_cont):
    split_value = name_cont.split()
    name = split_value[1].lower()
    return print(users[name])


def show_all():
    if len(users) > 0:
        for key, value in users.items():
            print(f"{key.capitalize()}: {value.capitalize()}")
    else:
        return print("You have no saved contacts")


def exit_bot(command):
    if command.lower() in ["good bye", "close", "exit"]:
        print("Good bye!")
        return True
    else:
        return False


while True:
    user_input = normalize(input(">>>"))
    if user_input == "hello" or user_input == "hi":
        hello()
    if "add" in user_input:
        add(user_input)
    if "change" in user_input:
        change(user_input)
    if "phone" in user_input:
        phone(user_input)
    if "show all" in user_input:
        show_all()
    if exit_bot(user_input):
        break
    else:
        print("Pls enter: 'add', 'change', 'phone', 'show all' or 'exit'")
