from othello.create import _create as create
import re
'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
def __validateTokenBoundaryAndType(tokenParmsIn):
    for parameter in ['light', 'dark', 'blank']:
        if (tokenParmsIn[parameter] == None):
            return {'status': 'error: Null ' + parameter +  ' value'}
        try: int(tokenParmsIn[parameter])
        except ValueError:
            return {'status': 'error: non-integer ' + parameter + ' value'}
        if (int(tokenParmsIn[parameter]) > 9):
            return {'status': 'error: above bound ' + parameter + ' value'} 
        if (int(tokenParmsIn[parameter]) < 0):
            return {'status': 'error: below bound ' + parameter + ' value'}
    
    if (int(tokenParmsIn['light']) == int(tokenParmsIn['dark'])):
        return {'status': 'error: light is equal to dark value'}
    if (int(tokenParmsIn['light']) == int(tokenParmsIn['blank'])):
        return {'status': 'error: blank is equal to light value'}
    if (int(tokenParmsIn['dark']) == int(tokenParmsIn['blank'])):
        return {'status': 'error: dark is equal to blank value'}
    return tokenParmsIn
    
def __validateBoardParms(boardParmsIn):
    if 'board' not in boardParmsIn.keys():
        return {'status': 'error: board does not exist'}
    if boardParmsIn.get('board') == None:
        return {'status': 'error: null board'}
    if len(boardParmsIn.get('board')) not in (36, 64, 100, 144, 196, 256):
        return {'status': 'error: uneven board'}
    tokenList = [int(boardParmsIn['light']), int(boardParmsIn['dark']), int(boardParmsIn['blank'])]
    checkBoardAndTokenList = all(index in tokenList for index in boardParmsIn.get('board'))
    for value in boardParmsIn.get('board'):
        if value in tokenList != None and not checkBoardAndTokenList:
                return {'status': 'error: incorrect board value'}
    return boardParmsIn
    
def __validateIntegrityParms(integrityParmsIn):
    if 'integrity' not in integrityParmsIn.keys():
        return {'status': 'error: integrity does not exist'}
    if integrityParmsIn.get('integrity') == None:
        return {'status': 'error: null integrity'}
    if len(integrityParmsIn.get('integrity')) < 64:
        return {'status': 'error: short integrity'}
    if len(integrityParmsIn.get('integrity')) > 64:
        return {'status': 'error: long integrity'}
    if not re.match('^[a-zA-Z0-9]*$', integrityParmsIn.get('integrity')):
        return {'status': 'error: non hex characters'}
    return integrityParmsIn

def _status(parms):
    result = __validateTokenBoundaryAndType(parms)
    if 'status' not in result:
        result = __validateBoardParms(parms)
        if 'status' not in result:
            result = __validateIntegrityParms(parms)
    return result

