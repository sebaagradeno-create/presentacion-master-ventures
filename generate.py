import os

filepath = r'D:\AGENCIA MASTER\_PROYECTOS\presentacion-master-ventures\public\index.html'

with open('html_part1.txt', 'r', encoding='utf-8') as f1, open('html_part2.txt', 'r', encoding='utf-8') as f2:
    html = f1.read() + f2.read()

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)

print('BUILD SUCCESSFUL')

