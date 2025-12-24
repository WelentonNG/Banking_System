import time
from datetime import datetime, timedelta

def contagem_regressiva():
    duracao = timedelta(seconds=3)
    fim = datetime.now() + duracao

    while datetime.now() < fim:
        tempo_restante = fim - datetime.now()
        segundos_restantes = int(tempo_restante.total_seconds()) + 1
        print(segundos_restantes)
        time.sleep(1)
