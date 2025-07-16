def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f"somando os valores {valores} temos {s}")

soma(5,2)
soma(3, 5, 3)