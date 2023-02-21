# Use website https://fossbytes.com/tools/random-name-generator and put it's generated content into "eleitores.dat" file

new = '['
new2 = ''

counter = 0
for i in open('eleitores.dat', 'r', encoding='utf-8').readlines():
    txt = i[:-1]
    counter += 1
    number = str(99999 - counter * 293)
    new += f"['{txt}', {number}],\n"
    new2 += f"{number} - {txt}\n"

new += ']'

open('eleitores.dat', 'w', encoding='utf-8').write(new)
open('eleitores.txt', 'w', encoding='utf-8').write(new2)
