#!usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from random import randint

# Criação de argumentos de linha de comando
parser = argparse.ArgumentParser(description='Gerador de casos de teste.')
# parser.add_argument('quantum', type=int, help='Janela de tempo que cada processo têm por vez para executar.')
parser.add_argument('num_processos', type=int, help='Quantidade de processos a serem gerados.')
parser.add_argument('arquivo', type=str, help='Nome do arquivo que conterá as descrições dos processos.')
try:
    args = parser.parse_args()
except:
    parser.print_help()
    raise SystemExit

with open(args.arquivo, 'w') as arq:
        for i in range(args.num_processos):
            arq.write("{} {} {} \n".format((i),randint(i, i + 20), randint(2,30)))
