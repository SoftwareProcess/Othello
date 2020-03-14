'''
Created on Mar 12, 2020

@author:    Tae Myles
'''

parms = {'op': 'create', 'light': '1', 'dark': '2', 'blank': '0', 'size': '8'}
# parms['light'] = 'w'
# 
# try: (int(parms['light']))
# except ValueError:
#     print('caught it')
#     
# parms['light'] = '1'
# print(parms)
# 
# result = {'board': 0, 
#           'tokens': {'light': int(parms['light']), 'dark': int(parms['dark']),
#                      'blank': int(parms['blank'])
#                      },
#           'status': 'ok',
#           'integrity': ''}
# del parms['light']
# if 'light' not in parms.keys():
#     parms['light'] = 1
# print (parms)
b = {'board': [int(parms['blank'])] * (int(parms['size']) ** 2)}
if len(b.get('board')) == 64:
    a =  b['board']
    a[2] = 3

print(b.get('board'))
