import submenu


main_menu = [
    ["matrix", "replit/matrix.py"],
    ["swap", "replit/swap.py"],
    ["Tree", "replit/tree.py"],
]

sub_menu = [
    ["animation1", "replit/animation1.py"],
    ["animation2", "replit/animation2.py"],
    ["Car", "replit/car.py"],
]


# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"

# menu blueprint
def menu():
    title = "Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Animations", submenu])
    buildMenu(title, menu_list)


def submenu():
    title = "Submenu" + banner
    m = submenu.Menu(title, sub_menu)
    m.menu()


def submenu():
    title = "Submenu" + banner
    buildMenu(title, sub_menu)


# builds console menu
def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user input
    choice = input("input your choice> ")

    # Process user input
    try:
        choice = int(choice)
        if choice == 0:
            # stops
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                # check main_menu dictionary
                print(f"file not found!: {action}")
    except ValueError:
        # not a number
        print(f"not a number: {choice}")
    except UnboundLocalError:
        # not one of the numbers listed
        print(f"invalid choice: {choice}")

    buildMenu(banner, options)


if __name__ == "__main__":
    menu()
