
import datetime

def executar_robo():
    while True:
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{agora}] Robô rodando sem pausa... verificando sinais.")

if __name__ == "__main__":
    executar_robo()
