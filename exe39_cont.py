def contador(i, f, p):
    print(f"contagerm de {i} ate {f} de {p} em {p}")

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            cont += p
        print("parou.")
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end="")
            cont -= p
        print("parou.")

contador(1, 10, 1)
contador(10, 0, 2)