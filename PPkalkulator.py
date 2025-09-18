import math
PI = math.pi
print(PI)
SQRT3 = (math.sqrt(3))

print("a - polaskie b - bryly")
inp = input("--- ")
if inp == "a":
    print("a - ppKwadaratu b - ppProstokata c - ppRownoległoboku d - ppTrapezu")
    print("e - ppTrojkątów f - ppKoła g - ppRobów")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla {a} ppKwadratu = {a**2}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"dla a={a} i dla b={b} ppProstokatu = {a*b}")
    elif inp == "c":
        a = float(input("a = "))
        h = float(input("h = "))
        print(f"dla a={a} i dla h={h} ppRownoległoboku = {a*h}")
    elif inp == "d":
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        print(f"dla a={a} i dla b{b} i dla h={h} ppTrapezu = {(a+b)*h/2}")
    elif inp == "e":
        print("e - ppTrójkata f - ppTrójaktaRównobocznego")
        inp = input("--- ")
        if inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla a={a} i dla h={h} ppTrojkata = {1/2*a*h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"dla a={a} ppTrójkataRownobocznego = {(a**2*SQRT3)/4}")
    elif inp == "f":
        r = float(input("f = "))
        print(f"dla r={r} ppKoła = {PI*r**2}")
    elif inp == "g":
        print("g - ppRombu a*h  h - ppRombu e*f/2")
        inp = input("--- ")
        if inp == "g":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla a={a} i dla h={h} ppRombu a*h = {a*h}")
        elif inp == "h":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"dla e={e} i  dla f={f} pprRombu e*f/2 = {e*f/2}")
    else:
        print("Nie ma takiej komendy")
elif inp == "b":
    print("a - ppSzeacianu b - ppProstopadłoscianu")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla a={a} ppSzecaniu = {6*a**2}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"dla a={a} i dla b={b} i dla c={c} ppProstopadłoscianu = {(a*b)*2 + (a*c)*2 + (b*c)*2}")
else:
