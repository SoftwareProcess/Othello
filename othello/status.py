'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
def __validateParms(parmsIn):
    
    if int(parmsIn['light']) > 9:
        return {'status': 'error: above bound light value in board'}

def _status(parms):
    parmsIn = parms
    result = __validateParms(parmsIn)
    return result
