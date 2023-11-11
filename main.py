def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print("Enter user name please")
        except ValueError:
            print("Enter a correct phone number")
        except IndexError:
            print("Give me name and phone please")

    return inner


USERS = {}


def hello():
    return print("How can I help you?")


def normalize(name):
    new_name = name.lower().strip()
    return new_name


def add(name_and_phone):
    split_value = name_and_phone.split()
    if len(split_value) == 3:
        name = split_value[1]
        phone_number = split_value[2]
        if name.lower() not in USERS.keys():
            USERS[name] = phone_number
        else:
            print(f"Contact with name:{name}  already exists")
    else:
        raise ValueError


def change(name_and_phone):
    split_val = name_and_phone.split()
    if len(split_val) == 3:
        name = split_val[1].lower()
        phone_numb = split_val[2]
        if name in USERS.keys():
            USERS[name] = phone_numb
        else:
            print(f"{name} is not found")
    else:
        raise ValueError


def phone(name_cont):
    split_value = name_cont.split()
    if len(split_value) != 2:
        raise IndexError
    name = split_value[1].lower()
    return print(USERS[name])


def show_all():
    if len(USERS) > 0:
        for key, value in USERS.items():
            print(f"{key.capitalize()}: {value}")
    else:
        return print("You have no saved contacts")


def exit_bot(command):
    if command.lower() in ["good bye", "close", "exit"]:
        print("Good bye!")
        return True
    else:
        return False


@input_error
def main(inputse):
    res = inputse.split()
    command = res[0]
    if command == "hello":
        hello()
    elif command == "add":
        add(inputse)
    elif command == "change":
        change(inputse)
    elif command == "phone":
        phone(inputse)
    elif inputse == "show all":
        show_all()
    else:
        print("Unknown command. Type 'hello' for assistance.")


while True:
    user_input = normalize(input("Enter command>>>"))
    if exit_bot(user_input):
        break
    else:
        main(user_input)
