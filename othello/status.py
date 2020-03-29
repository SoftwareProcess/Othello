'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
from othello.create import _create as create

def _status(parms):
    statusParmsIn = parms
    result = create(statusParmsIn)
    if len(result['board']) not in (36, 64, 100, 144, 196, 256):
        return {'status': 'error: non-square board'}
    return result

