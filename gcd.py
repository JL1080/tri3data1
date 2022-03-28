def igcd(a, b):
    if a > b:
        s = b
    if b > a:
        s = a
    for i in range(1, s + 1):
        if a % i == 0 and b % i == 0:
            gcd = i

    return gcd



class Gcd:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        if self.a > self.b:
            s = self.b

        if self.b > self.a:
            s = self.a

        for i in range(1, s+1):
            if self.a % i == 0 and self.b % i == 0:
                gcd = i
        return gcd

def tester():
    num = input("Imperative [i] or OOP [o]")
    try:
        if num == 'i':
            print("The gcd of 45 and 15 is : ",end="")
            print(igcd(45,15))
        elif num == 'o':
            f = Gcd(45,15)
            print("The gcd of 45 and 15 is : ",end="")
            print(f())
    except:
        print("Sorry, something went wrong")


if __name__ == "__main__":
    tester()