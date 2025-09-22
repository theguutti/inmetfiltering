from leitor import readCSV
from model.estatisticas import Estatisticas
from datetime import datetime

def checkDateFormat(data_str):
    formatos = ['%Y/%m/%d', '%d/%m/%Y', '%Y-%m-%d', '%d-%m-%Y']
    
    for formato in formatos:
        try:
            data_obj = datetime.strptime(data_str.strip(), formato)
            return data_obj.strftime('%Y/%m/%d')
        except ValueError:
            continue
    return None

def convertDateForComparison(data_str):
    try:
        return datetime.strptime(data_str, '%Y/%m/%d')
    except ValueError:
        return None

def filterByDate(estacoes, data_inicio, data_fim):
    data_inicio_normalizada = checkDateFormat(data_inicio)
    data_fim_normalizada = checkDateFormat(data_fim)
    
    if not data_inicio_normalizada or not data_fim_normalizada:
        print("Formato de data inválido. Use YYYY/MM/DD ou DD/MM/YYYY")
        return []
    
    dt_inicio = convertDateForComparison(data_inicio_normalizada)
    dt_fim = convertDateForComparison(data_fim_normalizada)
    
    if dt_inicio > dt_fim:
        print("A data de início deve ser anterior à data de fim.")
        return []
    
    estacoes_filtradas = []
    
    for estacao in estacoes:
        registros_filtrados = []
        
        for registro in estacao.obter_registros():
            data_registro = checkDateFormat(registro.data)
            if data_registro:
                dt_registro = convertDateForComparison(data_registro)
                if dt_registro and dt_inicio <= dt_registro <= dt_fim:
                    registros_filtrados.append(registro)
        
        if registros_filtrados:
            from model.estacao import EstacaoMeteorologica
            estacao_filtrada = EstacaoMeteorologica(
                estacao.nome, estacao.codigo, estacao.regiao, 
                estacao.uf, estacao.latitude, estacao.longitude, estacao.altitude
            )
            
            for registro in registros_filtrados:
                estacao_filtrada.adicionar_registro(registro)
            
            estacoes_filtradas.append(estacao_filtrada)
    
    return estacoes_filtradas

def showFilterMenu(estacoes):
    if not estacoes:
        print("Nenhuma estação carregada.")
        return
    
    print("\nFILTRAR DADOS POR DATA")
    print("Formatos aceitos: YYYY/MM/DD ou DD/MM/YYYY")
    print("Exemplos: 2023/01/15 ou 15/01/2023")
    
    data_inicio = input("Digite a data de início: ")
    data_fim = input("Digite a data de fim: ")
    
    print("\nFiltrando registros...")
    estacoes_filtradas = filterByDate(estacoes, data_inicio, data_fim)
    
    if not estacoes_filtradas:
        print("Nenhum registro encontrado no período especificado.")
        return
    
    total_registros = sum(len(estacao.obter_registros()) for estacao in estacoes_filtradas)
    print(f"\n{len(estacoes_filtradas)} estação(ões) com registros no período.")
    print(f"Total de {total_registros} registros encontrados.")
    
    while True:
        print("\nO que deseja fazer com os dados filtrados?")
        print("1. Ver informações das estações")
        print("2. Ver estatísticas do período")
        print("3. Ver alguns registros de exemplo")
        print("4. Exportar relatório do período filtrado")
        print("5. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            print("\nESTAÇÕES NO PERÍODO")
            for estacao in estacoes_filtradas:
                print(f"\n{estacao.nome} ({estacao.codigo})")
                print(f"Registros no período: {len(estacao.obter_registros())}")
                print(f"Localização: {estacao.regiao} - {estacao.uf}")
        
        elif opcao == "2":
            print("\nESTATÍSTICAS DO PERÍODO")
            for estacao in estacoes_filtradas:
                registros = estacao.obter_registros()
                if registros:
                    estatisticas = Estatisticas(registros)
                    print(f"\n{estacao.nome}:")
                    print(f" > Registros no período: {len(registros)}")
                    print(f" > Temperatura média: {estatisticas.media_temperatura():.2f}°C")
                    print(f" > Umidade máxima: {estatisticas.max_umidade():.2f}%")
                    print(f" > Precipitação total: {estatisticas.total_precipitacao():.2f}mm")
        
        elif opcao == "3":
            print("\nEXEMPLOS DE REGISTROS")
            for estacao in estacoes_filtradas:
                registros = estacao.obter_registros()
                if registros:
                    print(f"\n{estacao.nome} - Primeiros 3 registros:")
                    for i, registro in enumerate(registros[:3]):
                        print(f"  Registro {i+1}: {registro.data} {registro.hora} - "
                              f"Temp: {registro.temperatura}°C, "
                              f"Umidade: {registro.umidade}%, "
                              f"Precipitação: {registro.precipitacao}mm")
        
        elif opcao == "4":
            periodo = f"{checkDateFormat(data_inicio)}_a_{checkDateFormat(data_fim)}"
            nome_arquivo = f"relatorio_periodo_{periodo.replace('/', '-')}.txt"
            exportReport(estacoes_filtradas, nome_arquivo)
        
        elif opcao == "5":
            break
        
        else:
            print("Opção inválida!")

def exportReport(estacoes, nome_arquivo="relatorio.txt"): 
    if not estacoes:
        print("Nenhuma estação carregada para exportar relatório.")
        return

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write("RELATÓRIO CLIMÁTICO\n\n")
        
        for estacao in estacoes:
            arquivo.write(str(estacao) + "\n")
            registros = estacao.obter_registros()
            
            if registros:
                estatisticas = Estatisticas(registros)
                arquivo.write(f"\nTotal de registros: {len(registros)}\n")
                arquivo.write(f"Temperatura média: {estatisticas.media_temperatura():.2f}°C\n")
                arquivo.write(f"Umidade máxima: {estatisticas.max_umidade():.2f}%\n")
                arquivo.write(f"Precipitação total: {estatisticas.total_precipitacao():.2f}mm\n")

                arquivo.write("\nExemplos de registros:\n")
                for registro in registros[:5]:
                    arquivo.write(str(registro) + "\n")
            else:
                arquivo.write("Nenhum registro disponível para esta estação.\n")
                
            arquivo.write("\n" + "-"*50 + "\n\n")

    print(f"Relatório exportado para {nome_arquivo}")

def menu():
    estacoes = []
    
    while True:
        print("MENU:\n")
        print("1. Carregar arquivos da pasta")
        print("2. Exibir dados da(s) estação(ões)")
        print("3. Exibir estatísticas (média, máximo etc.)")
        print("4. Filtrar dados por data")
        print("5. Exportar relatório")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ano = input("Digite o ano (2020-2024): ")
            estacoes = readCSV(ano)
            if estacoes:
                print(f"{len(estacoes)} estação(ões) carregada(s).")
            else:
                print("Nenhuma estação foi carregada. Verifique se o ano existe.")

        elif opcao == "2":
            if not estacoes:
                print("Nenhuma estação carregada.")
                continue
            for estacao in estacoes:
                print(estacao)

        elif opcao == "3":
            if not estacoes:
                print("Nenhuma estação carregada.")
                continue
            for estacao in estacoes:
                registros = estacao.obter_registros()
                if registros:
                    estatisticas = Estatisticas(registros)
                    print(f"{estacao.nome}:")
                    print(f" > Temperatura média: {estatisticas.media_temperatura():.2f}°C")
                    print(f" > Umidade máxima: {estatisticas.max_umidade():.2f}%")
                    print(f" > Precipitação total: {estatisticas.total_precipitacao():.2f}mm")
                
        elif opcao == "4":
            showFilterMenu(estacoes)

        elif opcao == "5":
            if estacoes:
                exportReport(estacoes)
            else:
                print("Nenhuma estação carregada.")

        elif opcao == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()