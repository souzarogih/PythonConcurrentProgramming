import random
import datetime as dt
import time as t


print("Inicio", dt.datetime.now())

# x = random.randint(1,52)
# print(x)

# x = random.randrange(1,52)
# print(x)

x = random.randrange(5, 20)
print(x)
t.sleep(x)

print("Fim", dt.datetime.now())

# https://realpython.com/python-sleep/
# https://www.codingame.com/playgrounds/52723/programacao-python-parte-3---prof--marco-vaz/numeros-aleatorios