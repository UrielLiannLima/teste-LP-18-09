import utils

print("*------------------*")
print("|Calculadora de dias|")
print("*------------------*")

print("Informe duas data e calcularei o número de dias entre elas.")

print("Opções:")
print("1: Inserir datas manualmente")
print("2: Importar datas de arquivo texto")
print("0: Fechar programa")

repete_loop = True

while repete_loop:
    try:
        opcao = int(input("\nDigite sua escolha: "))
        if (opcao < 0 or opcao > 2):
            raise ValueError
    except ValueError:
        print("ERRO: digite um número válido")
        continue
    except:
        print("Apenas números são aceitos")
        continue

    if opcao == 0:
        break
    elif opcao == 1:
        print("Digite as datas no seguinte formato: \n")
        # print("<dia> de <mes> de <ano> - <dia> de <mes> de <ano>: ")

        # verificando data digitada
        try:
            string_data = str(input("<dia> de <mes> de <ano> - <dia> de <mes> de <ano>: "))
            datas = utils.datas_validas(string_data)
        except TypeError:
            print("ERRO: digite uma data válida")
            continue
        except:
            print("ERRO: isso não é uma data")
            continue

    elif opcao == 2:
        pass

print("Encerrando programa")