InfoDb = []

InfoDb.append({
    "Name": "James Lee",
    "Age": "17",
    "Classes Taking":["US History", "AM Lit", "AP Physics", "AP Stats", "AP CSP"]
})

InfoDb.append({
    "Name": "Alex Do",
    "Age": "16",
    "Classes Taking":["AP Studio Art","APEL","APUSH","AP Stats", "AP Bio"]
})

InfoDb.append({
    "Name": "Evan Sanchez",
    "Age": "16",
    "Classes Taking":["AP Physics","AP Calc BC", "US History", "AM Lit", "AP Music Theory"]
})

InfoDb.append({
    "Name": "William Wu",
    "Age": "February 15",
    "Classes Taking":["US History","Racquet Sports","Pre-Calc","AP Physics", "Offroll"]
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
    for n in range(len(InfoDb)):
        print_data(n)

def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return

# recursion simulates loop incrementing on each call (n + 1) until exit condition is met
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def recur_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * recur_factorial(n-1)

def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

tester()