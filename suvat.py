import math
x = input("What do you want to find? ")
suvat = ["s", "u", "v", "a", "t"]
values = []


def inputs():
    if x in suvat:
        for y in suvat:
            if y != x:
                try:
                    y = float(input(y+":"))
                    values.append(y)
                except ValueError:
                    y = None
        return values
    else:
        print("Not a valid option.")


def solve():
    if x == "s":
        u = values[0]
        v = values[1]
        t = values[2]
        z = input("Equation with v or a? ")
        if z == 'v':
            s = (u+v)/2*t
            print(s)
        elif z == 'a':
            s = u*t+0.5*v*t*t
            print(s)

    if x == "u":
        s = values[0]
        v = values[1]
        a = values[2]

        z = input("Equation with s or t? ")
        if z == 's':
            u = math.sqrt(v*v-2*a*s)
            print(u)
        elif z == 't':
            u = s-(v*a)
            print(u)

    if x == "v":
        s = values[0]
        u = values[1]
        a = values[2]

        z = input("Equation with s or t? ")
        if z == 's':
            v = math.sqrt(u*u+2*a*s)
            print(v)
        elif z == 't':
            v = s+(u*a)
            print(v)

    if x == "a":
        s = values[0]
        u = values[1]
        v = values[2]

        z = input("Equation with s or t? ")
        if z == 's':
            a = (v*v-u*u)/(2*s)
            print(a)
        elif z == 't':
            a = (u-s)/v
            print(a)

    if x == "t":
        s = values[0]
        u = values[1]
        v = values[2]

        z = input("Equation with s or a? ")
        if z == 's':
            t = (2*s)/(u+v)
            print(t)
        elif z == 'a':
            t = (u-s)/v
            if t < 0:
                print(str(t) + " which is impossible as time is positive.")
            else:
                print(t)


if not x:
    print("Empty field.")
else:
    inputs()
    solve()
