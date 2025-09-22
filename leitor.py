import os
from model.registro import RegistroMeteorologico
from model.estacao import EstacaoMeteorologica

def toFloat(valor):
    try:
        return float(valor.replace(",", "."))
    except:
        return 0.0

def readCSV(pasta_ano):
    
    caminho = os.path.join("inmet", pasta_ano)
    estacoes = []

    if not os.path.exists(caminho):
        print("Ano não encontrado.")
        return []

    for arquivo in os.listdir(caminho):
        if arquivo.endswith(".csv") or arquivo.endswith(".CSV"):
            with open(os.path.join(caminho, arquivo), encoding="latin-1") as f:
                linhas = f.readlines()

                regiao = linhas[0].split(";")[1].strip()
                uf = linhas[1].split(";")[1].strip()
                nome = linhas[2].split(";")[1].strip()
                codigo = linhas[3].split(";")[1].strip()
                latitude = toFloat(linhas[4].split(";")[1].strip())
                longitude = toFloat(linhas[5].split(";")[1].strip())
                altitude = toFloat(linhas[6].split(";")[1].strip())

                estacao = EstacaoMeteorologica(nome, codigo, regiao, uf, latitude, longitude, altitude)

                for linha in linhas[9:]:
                    dados = linha.strip().split(";")
                    if len(dados) < 15:
                        continue
                    try:
                        data = dados[0].strip()
                        hora = dados[1].replace("UTC", "").strip()

                        precipitacao = toFloat(dados[2])
                        temperatura = toFloat(dados[7])
                        umidade = toFloat(dados[14])

                        registro = RegistroMeteorologico(data, hora, temperatura, umidade, precipitacao)
                        estacao.adicionar_registro(registro)
                    except Exception as e:
                        continue

                estacoes.append(estacao)

    return estacoes
