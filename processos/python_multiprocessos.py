import datetime
import math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f"Realizando o processamento matemático com {qtd_cores} cores(s).")

    inicio = datetime.datetime.now()

    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini = 50_000_000 * (n -1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n} processando de {ini} até {fim}')
            executor.submit(computar, inicio=ini, fim=fim)


    fim = datetime.datetime.now()
    tempo = fim - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} seguntos.')


def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()
