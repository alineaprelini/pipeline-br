import time

import httpx


def buscar_dados(url, tentativas=3):
    """Busca dados de uma API. Se falhar, tenta de novo."""
    for tentativa in range(1, tentativas + 1):
        try:
            resposta = httpx.get(url, timeout=30)
            resposta.raise_for_status()
            return resposta.json()
        except httpx.HTTPError:
            print(f"Falha na tentativa {tentativa} de {tentativas}")
            if tentativa == tentativas:
                raise
            time.sleep(2 * tentativa)