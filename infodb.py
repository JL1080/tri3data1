InfoDb = []

InfoDb.append({
    "Name": "James Lee",
    "Age": "17",
    "Grade": "12",
    "Classes Taking":["AP Gov", "AP Calc BC", "World Lit 1", "AP CSP", "Offroll"] # list inside of a list this will print on replit
})

InfoDb.append({
    "Name": "Alex Do",
    "Age": "16",
    "Grade": "11",
    "Classes Taking":["AP Studio Art","APEL","APUSH","AP Stats", "AP Bio"] # list inside of a list this will print on replit
})

InfoDb.append({
    "Name": "Evan Sanchez",
    "Age": "16",
    "Grade": "11",
    "Classes Taking":["AP Physics","AP Calc BC", "US History", "AM Lit", "AP Music Theory"] # list inside of a list this will print on replit
})

InfoDb.append({
    "Name": "William Wu", #
    "Age": "February 15",
    "Grade": "10",
    "Classes Taking":["US History","Racquet Sports","Pre-Calc","AP Physics", "Offroll"] # list inside of a list this will print on replit
})

    # given an index this will print InfoDb content
def print_data(n):
    print(InfoDb[n]["Name"], InfoDb[n]["Age"])  # using comma puts space between values
    print("\t", "Classes Taking: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes Taking"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def for_loop():
    for n in range(len(InfoDb)):  # for loop and it is printed by tester
        print_data(n)

def while_loop(n):
    while n < len(InfoDb): # while loop takes data and is printed by tester
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n): # recursive loop takes data and is printed by tester
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def tester(): # tester prints the data from the list and the def for loop, recursive and while loops
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

tester()