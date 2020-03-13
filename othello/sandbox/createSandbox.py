'''
Created on Mar 12, 2020

@author:    Tae Myles
'''

parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}
parms['light'] = 'w'

try: (int(parms['light']))
except ValueError:
    print('caught it')
    