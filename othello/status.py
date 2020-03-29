from othello.create import _create as create
import re
'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''

def __checkParms(parmsIn):
    createOutput = create(parmsIn)
    # Check board parameter
    if 'board' not in parmsIn.keys():
        return {'status': 'error: board does not exist'}
    if parmsIn.get('board') == None:
        return {'status': 'error: null board'}
    if len(parmsIn.get('board')) not in (36, 64, 100, 144, 196, 256):
        return {'status': 'error: uneven board'}
    for i in parmsIn.get('board'):
        if i not in (int(parmsIn.get('light')), int(parmsIn.get('dark')), int(parmsIn.get('blank'))):
            return {'status': 'error: incorrect board value'}   
    
    # Check integrity parameter
    if 'integrity' not in parmsIn.keys():
        return {'status': 'error: integrity does not exist'}
    if parmsIn.get('integrity') == None:
        return {'status': 'error: null integrity'}
    if len(parmsIn.get('integrity')) < 64:
        return {'status': 'error: short integrity'}
    if len(parmsIn.get('integrity')) > 64:
        return {'status': 'error: long integrity'}
    if not re.match('^[a-zA-Z0-9]*$', parmsIn.get('integrity')):
        return {'status': 'error: non hex characters'}
    return createOutput

def _status(parms):
    statusParmsIn = parms
    result = __checkParms(statusParmsIn)
    return result

