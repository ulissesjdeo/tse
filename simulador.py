# -*- coding: utf-8 -*-

from datetime import datetime
from siphash import SipHash_2_4

eleitores = [
    ['Clara Fernandes', 99706],
    ['Sr. Lucca Melo', 99413],
    ['Nathan Pereira', 99120]
]

secret = 'SEGREDODOTSE1234'


def clear():
    print(' \n' * 100)


def line(info):
    pre = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + info
    return pre + str(SipHash_2_4(secret, pre).hexdigest()).upper() + '\n'


def line_with_hidden(info, hidden):
    pre = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + info
    return pre + str(SipHash_2_4(secret, pre + hidden).hexdigest()).upper() + '\n'


open('logd.dat', 'w').write(line('	INFO	67305985	LOGD	Início das operações do logd	'))
open('logd.dat', 'a').write(line('	INFO	67305985	SCUE	Iniciando aplicação - Oficial - 2º turno	'))
open('logd.dat', 'a').write(line('	INFO	67305985	SCUE	Versão da aplicação: 8.26.0.0 - Onça-pintada	'))

for i in eleitores:
    clear()
    print('[TELA DO MESÁRIO]')
    open('logd.dat', 'a').write(line('	VOTA	67305985	Aguardando digitação do título	'))
    titulo = input('Por favor digite o título do eleitor: ')
    if titulo != i[1]:
        exit(1)
    clear()
    open('logd.dat', 'a').write(line('	INFO	67305985	VOTA	Título digitado pelo mesário	'))
    open('logd.dat', 'a').write(line('	INFO	67305985	VOTA	Eleitor foi habilitado	'))
    print('[TELA DO ELEITOR]')
    voto_governador = input('Voto para [GOVERNADOR]: ')
    open('logd.dat', 'a').write(line_with_hidden('	INFO	67305985	VOTA	Voto confirmado para [Governador]	', str(i[1]) + str(voto_governador)))
    voto_presidente = input('Voto para [PRESIDENTE]: ')
    open('logd.dat', 'a').write(line_with_hidden('	INFO	67305985	VOTA	Voto confirmado para [Presidente]	', str(i[1]) + str(voto_presidente)))
    open('logd.dat', 'a').write(line('	INFO	67305985	VOTA	O voto do eleitor foi computado	'))
