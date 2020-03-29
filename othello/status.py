'''
    Created on Mar 27, 2020
    
    @author:    Tae Myles
'''
def __validateParms(parmsIn):
    
    if int(parmsIn['light']) > 9:
        return {'status': 'error: above bound light value in board'}

def _status(parms):
    parmsIn = parms
    __validateParms(parmsIn)
    result = {'status': 'status stub'}
    return result
