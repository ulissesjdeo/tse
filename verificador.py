# -*- coding: utf-8 -*-

from siphash import SipHash_2_4

eleitores = [
    ['Clara Fernandes', 99706],
    ['Sr. Lucca Melo', 99413],
    ['Nathan Pereira', 99120],
]

secret = 'SEGREDODOTSE1234'
line_number = 0

for line in open('logd.dat', 'r').readlines():
    line_number += 1
    line_without_hash = line[:-17]
    hash = line[-17:][:-1]
    if str(SipHash_2_4(secret, line_without_hash).hexdigest()).upper() == hash:
        print('Linha ' + str(line_number) + ' OK.')
    else:
        for eleitor in eleitores:
            for possivel_voto in [22, 13]:
                possible_hash = str(SipHash_2_4(secret, line_without_hash + str(eleitor[1]) + str(possivel_voto)).hexdigest()).upper()
                if possible_hash == hash:
                    print('Linha ' + str(line_number) + ' REVELADA. Título ' + str(eleitor[1]) + ' votou ' + str(possivel_voto))
