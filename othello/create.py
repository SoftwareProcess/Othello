def _create(parms):
    if (int(parms['light']) > 9):
        result = {'status': 'error: above bound light value'}
    elif (int(parms['light']) < 0):
        result = {'status': 'error: below bound light value'}
    elif (isinstance(int(parms['light']), int)):
        result = {'status': 'error: non-integer light value'}
        
    return result
