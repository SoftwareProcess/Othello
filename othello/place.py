'''
    Created on Apr 25, 2020
    
    @author:    Tae Myles
'''
import re
import hashlib

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
   
def __validateLocation(locationParmsIn):
    if 'location' not in locationParmsIn.keys():
        return {'status': 'error: missing location'}
    if locationParmsIn['location'] == None:
        return {'status': 'error: Null location'}
    locationList = locationParmsIn['location'].split(':')
    if ':' not in locationParmsIn['location']:
        return {'status': 'error: invalid location separator'}
    if locationList[0] == '' or locationList[1] == '':
        return {'status': 'error: missing a value on one side of separator'}
    # Check left of the separator
    try: int(locationList[0])
    except ValueError:
        return {'status': 'error: non-integer location value'}
    # Check right of the separator
    try: int(locationList[1])
    except ValueError:
        return {'status': 'error: non-integer location value'}
    return locationParmsIn
 
def __validateBoardParms(boardParmsIn):
    if 'board' not in boardParmsIn.keys():
        return {'status': 'error: board does not exist'}
    if boardParmsIn.get('board') == None:
        return {'status': 'error: null board'}
    
    boardCount = len(boardParmsIn['board'])
    
    tokenList = [int(boardParmsIn['light']), int(boardParmsIn['dark']), int(boardParmsIn['blank'])]
    checkBoardAndTokenList = all(index in tokenList for index in boardParmsIn.get('board'))
    for value in boardParmsIn.get('board'):
        if value in tokenList != None and not checkBoardAndTokenList:
                return {'status': 'error: incorrect board value'}
    if boardCount == 36 or boardCount == 64 or boardCount == 100 or boardCount == 144 or boardCount == 196 or boardCount == 256:
        return boardParmsIn
    else:
        return {'status': 'error: uneven board'}


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

def __placeTokenOnBoard(allParm):
    # splitting location separator
    locationList = allParm['location'].split(':')
    row = int(locationList[0])
    col = int(locationList[1])
    boardList = allParm['board']
    boardCount = len(allParm['board'])
    # Initialize 2d array with current board element
    if boardCount == 36:
        twoDList =[boardList[i:i+6] for i in range(0, len(boardList), 6)]
    if boardCount == 64:
        twoDList =[boardList[i:i+8] for i in range(0, len(boardList), 8)]
    if boardCount == 100:
        twoDList =[boardList[i:i+10] for i in range(0, len(boardList), 10)]
    if boardCount == 144:
        twoDList =[boardList[i:i+12] for i in range(0, len(boardList), 12)]
    if boardCount == 196:
        twoDList =[boardList[i:i+14] for i in range(0, len(boardList), 14)]
    if boardCount == 256:
        twoDList =[boardList[i:i+16] for i in range(0, len(boardList), 16)]
    # Need to figure out who's turn it is
    message = ''
    for index in allParm['board']:
        message = message + str(index)
    
    darkMessage = message + "/" + str(allParm['light']) + "/" + \
        str(allParm['dark']) + "/" + str(allParm['blank']) + \
        "/" + str(allParm['dark'])
    darkSha256HexDigest = hashlib.sha256(darkMessage.encode('utf-8')).hexdigest()
    
    lightMessage = message + "/" + str(allParm['light']) + "/" + \
        str(allParm['dark']) + "/" + str(allParm['blank']) + \
        "/" + str(allParm['light'])
    lightSha256HexDigest = hashlib.sha256(lightMessage.encode('utf-8')).hexdigest()
    
    if allParm['integrity'] == lightSha256HexDigest:
        twoDList[row][col] = int(allParm['light'])
        # returning 2d to 1d list
        return sum(twoDList, [])
    
    if allParm['integrity'] == darkSha256HexDigest:
        twoDList[row][col] = int(allParm['dark'])
        # returning 2d to 1d list
        return sum(twoDList, [])
    
def __calculateTurnIntegrity(integParm):
    message = ''
    for index in integParm['originalBoard']:
        message = message + str(index)

    darkMessage = message + "/" + str(integParm['light']) + "/" + \
        str(integParm['dark']) + "/" + str(integParm['blank']) + \
        "/" + str(integParm['dark'])
    darkSha256HexDigest = hashlib.sha256(darkMessage.encode('utf-8')).hexdigest()
    
    lightMessage = message + "/" + str(integParm['light']) + "/" + \
        str(integParm['dark']) + "/" + str(integParm['blank']) + \
        "/" + str(integParm['light'])
    lightSha256HexDigest = hashlib.sha256(lightMessage.encode('utf-8')).hexdigest()
    
    if integParm['integrity'] == lightSha256HexDigest:
        darkMsg = ''
        for index in integParm['board']:
            darkMsg = darkMsg + str(index)
        darkMessage = darkMsg + "/" + str(integParm['light']) + "/" + \
        str(integParm['dark']) + "/" + str(integParm['blank']) + \
        "/" + str(integParm['dark'])
        darkSha256HexDigest = hashlib.sha256(darkMessage.encode('utf-8')).hexdigest()
        return darkSha256HexDigest
    
    if integParm['integrity'] == darkSha256HexDigest:
        lightMsg = ''
        for index in integParm['board']:
            lightMsg = lightMsg + str(index)
        lightMessage = lightMsg + "/" + str(integParm['light']) + "/" + \
        str(integParm['dark']) + "/" + str(integParm['blank']) + \
        "/" + str(integParm['light'])
        lightSha256HexDigest = hashlib.sha256(lightMessage.encode('utf-8')).hexdigest()
        return lightSha256HexDigest
    return {'status': 'invalid integrity'}
    
def _place(parms):
    if ('light' not in parms.keys()):
        parms['light'] = 1
    if ('dark' not in parms.keys()):
        parms['dark'] = 2
    if ('blank' not in parms.keys()):
        parms['blank'] = 0
    result = __validateTokenBoundaryAndType(parms)
    if 'status' not in result:
        result = __validateLocation(parms)
        if 'status' not in result:
            result = __validateBoardParms(parms)
            if 'status' not in result:
                result = __validateIntegrityParms(parms)
                if 'status' in result:
                    return result
                origBoard = result['board']
                result.update({'originalBoard': origBoard})
                result['board'] = __placeTokenOnBoard(parms)
                result['integrity'] = __calculateTurnIntegrity(parms)
                del result['op']
                del result['light']
                del result['dark']
                del result['blank']
                del result['location']
                del result['originalBoard']
                result.update({'status': 'ok'})
    return result