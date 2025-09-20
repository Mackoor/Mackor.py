import math
PI = math.pi
print(PI)
SQRT3 = (math.sqrt(3))

print("a - P.Płaskie b - Obw.Płaskie c - Pc.brył d - Obj.brył")
inp = input("--- ")
if inp == "a":
    print("a - P.Kwadaratu b - P.Prostokata c - P.Rownoległoboku d - P.Trapezu")
    print("e - P.Trojkątów f - P.Koła g - P.Robów")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla {a} P.Kwadratu = {a**2}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"dla a={a} i dla b={b} P.Prostokatu = {a*b}")
    elif inp == "c":
        a = float(input("a = "))
        h = float(input("h = "))
        print(f"dla a={a} i dla h={h} P.Rownoległoboku = {a*h}")
    elif inp == "d":
        a = float(input("a = "))
        b = float(input("b = "))
        h = float(input("h = "))
        print(f"dla a={a} i dla b{b} i dla h={h} P.Trapezu = {(a+b)*h/2}")
    elif inp == "e":
        print("e - P.Trójkata f - P.TrójaktaRównobocznego")
        inp = input("--- ")
        if inp == "e":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla a={a} i dla h={h} P.Trojkata = {1/2*a*h}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"dla a={a} P.TrójkataRownobocznego = {(a**2*SQRT3)/4}")
    elif inp == "f":
        r = float(input("r = "))
        print(f"dla r={r} P.Koła = {PI*r**2}")
    elif inp == "g":
        print("g - P.Rombu a*h  h - P.Rombu e*f/2")
        inp = input("--- ")
        if inp == "g":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla a={a} i dla h={h} P.Rombu a*h = {a*h}")
        elif inp == "h":
            e = float(input("e = "))
            f = float(input("f = "))
            print(f"dla e={e} i  dla f={f} P.Rombu e*f/2 = {e*f/2}")
    else:
        print("Nie ma takiej komendy")
elif inp == "b":
    print("a - Obw.Kwadaratu b - Obw.Prostokata c - Obw.Rownoległoboku d - Obw.Trapezu")
    print("e - Obw.Trojkątów f - Obw.Koła g - Obw.Robu")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla {a} Obw.Kwadratu = {4*a}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"dla a={a} i dla b={b} Obw.Prostokatu = {2*a+2*b}")
    elif inp == "c":
        a = float(input("a = "))
        b = float(input("b = "))
        print(f"dla a={a} i dla b={b} Obw.Rownoległoboku = {2*a+2*b}")
    elif inp == "d":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        d = float(input("d = "))
        print(f"dla a={a} i dla b{b} i dla c={c} i dla d={d} Obw.Trapezu = {a+b+c+d}")
    elif inp == "e":
        print("e - Obw.Trójkata f - Obw.TrójaktaRównobocznego")
        inp = input("--- ")
        if inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla a={a} i dla b={b} i dla c={c} OBw.Trojkata = {a+b+c}")
        elif inp == "f":
            a = float(input("a = "))
            print(f"dla a={a} Obw.TrójkataRownobocznego = {3*a}")
    elif inp == "f":
        r = float(input("r = "))
        print(f"dla r={r} Obw.Koła = {2*PI*r}")
    elif inp == "g":
        a = float(input("a = "))
        print(f"dla a={a} Obw.Rombu = {4*a}")
    else:
        print("Nie ma takiej komendy")
elif inp == "c":
    print("a - Pc.Szeacianu b - Pc.Prostopadłoscianu c - Pc.Graniatosłupa d - Pc.Ostrosłupa")
    print("e - Pc.Walca f - Pc.Storzka g - Pc.Kuli")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla a={a} Pc.Szecaniu = {6*a**2}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"dla a={a} i dla b={b} i dla c={c} Pc.Prostopadłoscianu = {2*(a*b) + 2*(a*c) + 2*(b*c)}")
    elif inp == "c":
        Pp = float(input("Pp = "))
        Pb = float(input("Pb = "))
        print(f"dla Pp={Pp} i dla Pb={Pb} Pc.Graniatosłupa = {2*Pp+Pb}")
    elif inp == "d":
        Pp = float(input("Pp = "))
        Pb = float(input("Pb = "))
        print(f"dla Pp={Pp} i dla Pb={Pb} Pc.Ostrosłupa = {Pp+Pb}")
    elif inp == "e":
        r = float(input("r = "))
        h = float(input("h = "))
        print(f"dla r={r} i dla h={h} Pc.Walca = {2*PI*r**2+2*PI*r*h}")
    elif inp == "f":
        r = float(input("r = "))
        l = float(input("l = "))
        print(f"dla r={r} i dla l={l} Pc.storzka = {PI*r**2+PI*r*l}")
    elif inp == "g":
        r = float(input("r = "))
        print(f"dla r={r} Pc.Kuli = {4*PI*r**2}")
    else:
        print("Nie ma takiej komendy")
elif inp == "d":
    print("a - Obj.Szeacianu b - Obj.Prostopadłoscianu c - Obj.Graniatosłupa d - Obj.Ostrosłupa")
    print("e - Obj.Walca f - Obj.Storzka g - Obj.Kuli")
    inp = input("--- ")
    if inp == "a":
        a = float(input("a = "))
        print(f"dla a={a} Obj.Szecaniu = {a**3}")
    elif inp == "b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print(f"dla a={a} i dla b={b} i dla c={c} Obj.Prostopadłoscianu = {a*b*c}")
    elif inp == "c":
        Pp = float(input("Pp = "))
        h = float(input("h = "))
        print(f"dla Pp={Pp} i dla h={h} Obj.Graniatosłupa = {Pp*h}")
    elif inp == "d":
        Pp = float(input("Pp = "))
        h = float(input("h = "))
        print(f"dla Pp={Pp} i dla h={h} Obj.Ostrosłupa = {1/3*Pp*h}")
    elif inp == "e":
        r = float(input("r = "))
        h = float(input("h = "))
        print(f"dla r={r} i dla h={h} Obj.Walca = {PI*r**2*h}")
    elif inp == "f":
        r = float(input("r = "))
        h = float(input("h = "))
        print(f"dla r={r} i dla h={h} Pc.storzka = {1/3*PI*r**2*h}")
    elif inp == "g":
        r = float(input("r = "))
        print(f"dla r={r} Pc.Kuli = {4/3*PI*r**3}")
else:
    print("Nie ma takiej komendy")