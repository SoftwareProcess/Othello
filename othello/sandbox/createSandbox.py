'''
Created on Mar 12, 2020

@author:    Tae Myles
'''
import hashlib

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
# b = {'board': [int(parms['blank'])] * (int(parms['size']) ** 2)}
# if len(b.get('board')) == 64:
#     a =  b['board']
#     a[27] = 1
#     a[28] = 2
#     a[35] = 2
#     a[36] = 1
#     
# print(b.get('board'))
# ranStr = '1223'
# p = hashlib.sha256(ranStr.encode('utf-8')).hexdigest()
# print(p)

t = {'tokens': {'light': 1, 'dark': 2, 'blank': 0}}
b = {'board': [0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 1, 2, 0, 0, 0,
                0, 0, 0, 2, 1, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0]}
light = t['tokens']['light']
dark = t['tokens']['dark']
blank = t['tokens']['blank']

m = ''
for i in b['board']:
    m = m + str(i)
print (m)

m = m + "/" + str(light) + "/" + str(dark) + "/" + str(blank) + "/" + str(dark)
print (m)

sha = hashlib.sha256(m.encode('utf-8')).hexdigest()
print (sha)

