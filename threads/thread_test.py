import threading


def my_fun(param, var, idade):
    print("Executa algo...")
    print(f"Usa o parâmetro recebido: {param}")
    print("var: ", var)
    print("idade: ", idade)

    rev = param * param
    print(rev)
    return rev


th = threading.Thread(target=my_fun, args=(42, "Higor", 29,))

th.start()
th.join()