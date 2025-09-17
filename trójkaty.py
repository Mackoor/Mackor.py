a = float(input())
b = float(input())
c = float(input())

if a + b > c and c + b > a and a + c > b:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("to jest tr prostokątny")
    if a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
        print("to jest tr ostrokatny")
    if a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print("to jest tr rozwartokatny")
    if a == b + c or c == b + a or c == a + b:
        print("to jest tr równoramnienny")
    if a == b == c:
        print("to jest tr równoboczny")
else:
    print("to nie jest trójkąt")