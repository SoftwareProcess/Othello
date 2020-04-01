import re
import hashlib
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
    
    message = ''
    for index in integrityParmsIn['board']:
        message = message + str(index)
    
    darkMessage = message + "/" + str(integrityParmsIn['light']) + "/" + \
        str(integrityParmsIn['dark']) + "/" + str(integrityParmsIn['blank']) + \
        "/" + str(integrityParmsIn['dark'])
    darkSha256HexDigest = hashlib.sha256(darkMessage.encode('utf-8')).hexdigest()
    
    lightMessage = message + "/" + str(integrityParmsIn['light']) + "/" + \
        str(integrityParmsIn['dark']) + "/" + str(integrityParmsIn['blank']) + \
        "/" + str(integrityParmsIn['light'])
    lightSha256HexDigest = hashlib.sha256(lightMessage.encode('utf-8')).hexdigest()
    
    if integrityParmsIn['integrity'] == lightSha256HexDigest:
        encryption = lightSha256HexDigest
    elif integrityParmsIn['integrity'] == darkSha256HexDigest:
        encryption = darkSha256HexDigest
    else: 
        return  {'status': 'error: invalid integrity'}
    return encryption

def __checkDark(boardParm):
    result = {'status': 'ok'}
    lightCounter = 0
    darkCounter = 0
    blankCounter = 0
    for index in boardParm['board']:
        if index == int(boardParm['light']):
            lightCounter = lightCounter + 1
        if index == int(boardParm['dark']):
            darkCounter = darkCounter + 1  
        if index == int(boardParm['blank']):
            blankCounter = blankCounter + 1
    if len(boardParm['board']) == 36:
        if blankCounter <= 4 and lightCounter-4 > darkCounter:
            result = {'status': 'dark'} 
    return result  
      
def __checkLight(boardParm):
    result = {'status': 'ok'}
    lightCounter = 0
    darkCounter = 0
    blankCounter = 0
    for index in boardParm['board']:
        if index == int(boardParm['light']):
            lightCounter = lightCounter + 1
        if index == int(boardParm['dark']):
            darkCounter = darkCounter + 1  
        if index == int(boardParm['blank']):
            blankCounter = blankCounter + 1
    if len(boardParm['board']) == 36:
        if blankCounter <= 4 and lightCounter < darkCounter-4:
            result = {'status': 'light'} 
    return result        
             
def _status(parms):
    if ('light' not in parms.keys()):
        parms['light'] = 1
    if ('dark' not in parms.keys()):
        parms['dark'] = 2
    if ('blank' not in parms.keys()):
        parms['blank'] = 0
        
    result = __validateTokenBoundaryAndType(parms)
    if 'status' not in result:
        result = __validateBoardParms(parms)
        if 'status' not in result:
            result = __validateIntegrityParms(parms)
            if 'status' not in result:
                result = {'status': 'ok'}
                result = __checkDark(parms)
                result = __checkLight(parms)
                
    return result

