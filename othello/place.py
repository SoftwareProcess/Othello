'''
    Created on Apr 25, 2020
    
    @author:    Tae Myles
'''
import re
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
    if boardCount == 36 or boardCount == 64 or boardCount == 144 or boardCount == 196 or boardCount == 256:
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
    return result
