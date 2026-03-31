from django.forms import ValidationError
from manage import *
import contextlib, io
from decimal import Decimal

saida = io.StringIO()

with contextlib.redirect_stdout(saida):
    main()

from exemplo.models import Esporte, Time, Cidade, Pessoa
from exemplo.enumerations import Sexo

processados = 0
erros = 0

with open('pessoas.csv', 'r', encoding='utf-8') as arquivo:
    try:
        # Lê a primeira linha e não armazena
        arquivo.readline()

        # Faz a leitura do restante do arquivo
        for linha in arquivo:
            dados = linha.split(',')
            nome = dados[0]
            sexo = dados[1]
            idade = int(dados[2])
            cidade = dados[3]
            estado = dados[4]
            time = dados[5]
            renda = Decimal(dados[6])
            esporte = dados[7]

            if sexo.upper() == "MASCULINO":
                sexo = Sexo.MASCULINO
            elif sexo.upper() == "FEMININO":
                sexo = Sexo.FEMININO
            else:
                raise ValueError("Sexo não cadastrado no enum")

            # Consulta e cadastro da cidade
            try:
                endereco = Cidade.objects.filter(nome=cidade , estado=estado)

                # Cidade não está cadastrada
                if len(endereco) == 0:
                    try:
                        cidade_cadastrada = Cidade(nome=cidade, estado=estado)
                        cidade_cadastrada.full_clean()
                        cidade_cadastrada.save()
                    except ValidationError as e:
                        print(e)
                # Cidade cadastrada
                elif len(endereco) == 1:
                    cidade_cadastrada = endereco[0]
                # Mais de uma cidade cadastrada
                else:
                    raise ValueError("Cidade em duplicidade")
            except Exception as e:
                print(e)

            # Consulta e cadastro de time
            try:
                clube = Time.objects.filter(nome=time)

                if len(clube) == 0:
                    clube_cadastrado = Time(nome=time)
                    clube_cadastrado.full_clean()
                    clube_cadastrado.save()

                elif len(clube) == 1:
                    clube_cadastrado = clube[0]
                else:
                    raise ValueError("Cluve cadastrado em duplicidade")
            except Exception as e:
                print(e)

            # Consulta e cadastro para o esporte favorito
            try:
                esporte_favorito = Esporte.objects.filter(nome=esporte)

                if len(esporte_favorito) == 0:
                    esporte_favorito = Esporte(nome=esporte)
                    esporte_favorito.full_clean()
                    esporte_favorito.save()
                elif len(esporte_favorito) == 1:
                    esporte_favorito = esporte_favorito[0]
                else:
                    raise ValueError("Esporte cadastrado em duplicidade")
            except Exception as e:
                print(e)

            try:
                nova_pessoa = Pessoa(
                    nome = nome, #nome.tittle()
                    sexo = sexo,
                    idade = idade,
                    renda = renda,
                    time = clube,
                    esporte = esporte_favorito,
                    cidade = cidade_cadastrada
                )
                nova_pessoa.full_clean()
                nova_pessoa.save()
                print(f"Registro processado: {linha}")
                processados += 1
            except Exception as e:
                print(f"Problema ao salvar: {linha}")
                print(e)
                erros += 1
        

    except Exception as e:
        print(f"Problema ao salvar: {linha}")
        print(e)
        erros += 1
print(f"Processamento concluído\nTotal: {processados+erros}\nProcessados Corretamente: {processados}\n Erros: {erros}")