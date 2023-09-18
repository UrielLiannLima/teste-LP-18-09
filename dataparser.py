import re
import datetime

#Define a função para extrair e converter a data de texto pra um tipo trabalhável
def extrair_converter_data(input_str):
    #Define um dicionário com indexação para cada mês com seu correspondente número
    meses = {
        "Janeiro": 1, 
        "Fevereiro": 2, 
        "Março": 3, 
        "Abril": 4,
        "Maio": 5, 
        "Junho": 6, 
        "Julho": 7, 
        "Agosto": 8,
        "Setembro": 9, 
        "Outubro": 10, 
        "Novembro": 11, 
        "Dezembro": 12
    }

    #Define o padrão dos dados
    padrao = r'(\d{1,2}) de (\w+) de (\d{4})'
    correspondencias = re.findall(padrao, input_str)

    #Busca correspondências no input dado e retorna se encontrar
    datas = []
    for correspondencia in correspondencias:
        dia, mes_str, ano = correspondencia
        mes = meses.get(mes_str)
        if mes:
            data = datetime(int(ano), mes, int(dia))
            datas.append(data)
    
    return datas