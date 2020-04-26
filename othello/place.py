'''
    Created on Apr 25, 2020
    
    @author:    Tae Myles
'''
def __validateTokenBoundaryAndType(tokenParmsIn):
    for parameter in ['light']:
        if (int(tokenParmsIn[parameter]) > 9):
            return {'status': 'error: above bound ' + parameter + ' value'} 
    return tokenParmsIn

def _place(parms):
    result = __validateTokenBoundaryAndType(parms)
    return result
