'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
from othello.create import _create as create
def __checkParms(parmsIn):
    createOutput = create(parmsIn)
    if 'board' not in parmsIn.keys():
        return {'status': 'error: board does not exist'}
    if parmsIn.get('board') == None:
        return {'status': 'error: null board'}
    if len(parmsIn.get('board')) not in (36, 64, 100, 144, 196, 256):
        return {'status': 'error: uneven board'}
    
    # Check integrity parameter
    if len(parmsIn.get('integrity')) < 64:
        return {'status': 'error: short integrity'}
    return createOutput['status']

def _status(parms):
    statusParmsIn = parms
    result = __checkParms(statusParmsIn)
    return result

