import re

content = ''

with open('replace.txt', 'r') as fd:
    content = fd.read()

replacements = [l.split()]

template = '''

..  figure:: {path}
    :align: center
    :width: 70%

    {legend}

'''

