import requests
import time
import sys

IP_DO_CELULAR = "192.168.18.57" # ALTERE COM O IP DO SEU CELULAR
PORTA = "8080"
URL_PHYPHOX = f"http://{IP_DO_CELULAR}:{PORTA}/get?accX&accY"

LARGURA_DA_BARRA = 50
SENSIBILIDADE = 2.5

print("Nível Digital Iniciado.")
print("Deixe o celular em uma superfície plana e pressione 'play' no phyphox.")
print("Incline para a esquerda e direita para ver a bolha se mover.")
print("Pressione Ctrl+C para parar.")

try:
    while True:
        try:
            response = requests.get(url=URL_PHYPHOX, timeout=5)
            response.raise_for_status()
            data = response.json()

            ay = data['buffer']['accY']['buffer'][0]
            
            centro = LARGURA_DA_BARRA // 2
            deslocamento = int(ay * SENSIBILIDADE)
            posicao_bolha = centro + deslocamento
            
            posicao_bolha = max(0, min(LARGURA_DA_BARRA - 1, posicao_bolha))
            
            barra_visual = list("·" * LARGURA_DA_BARRA)
            barra_visual[posicao_bolha] = 'O'
            barra_visual[centro] = '|'
            barra_visual = "".join(barra_visual)
            
            status = "✔ NIVELADO!" if abs(ay) < 0.15 else "✖ Inclinado"
            
            print(f"\r[{barra_visual}] {status.ljust(15)}", end="")
            
            time.sleep(0.05)

        except requests.exceptions.RequestException:
            print("\nErro de conexão. Verificando novamente em 5 segundos...", flush=True)
            time.sleep(5)
        except KeyError:
            print("\nErro nos dados. Certifique-se de que o experimento 'Acelerômetro (com g)' está ativo.", flush=True)
            time.sleep(5)

except KeyboardInterrupt:
    print("\n\nPrograma interrompido.")
    sys.exit()
