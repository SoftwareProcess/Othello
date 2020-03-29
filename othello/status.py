'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
from othello.create import _create as create

def _status(parms):
    statusParmsIn = parms
    createOutput = create(statusParmsIn)
    if 'board' not in parms.keys():
        return {'status': 'error: board does not exist'}
    if parms.get('board') == None:
        return {'status': 'error: null board'}
    if len(parms.get('board')) not in (36, 64, 100, 144, 196, 256):
        return {'status': 'error: uneven board'}
    return createOutput

