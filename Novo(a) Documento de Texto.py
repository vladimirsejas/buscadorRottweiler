import requests
import os
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a API_KEY do .env
API_KEY = os.getenv("API_KEY")

# Cria pasta para salvar imagens
os.makedirs("rottweilers", exist_ok=True)

url = "https://pixabay.com/api/"
params = {
    "key": API_KEY,
    "q": "rottweiler",
    "image_type": "photo",
    "per_page": 10
}

# Faz requisição
response = requests.get(url, params=params)
data = response.json()

# Verifica se veio resultado
if "hits" not in data:
    print("Erro na requisição. Verifique a API_KEY.")
else:
    fotos = data["hits"]

    for i, foto in enumerate(fotos):
        img = requests.get(foto["webformatURL"]).content
        with open(f"rottweilers/rottweiler_{i+1}.jpg", "wb") as f:
            f.write(img)
        print(f"[{i+1}] Salva: rottweiler_{i+1}.jpg")

    print("Concluído!")