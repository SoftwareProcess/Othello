def _create(parms):
    if (int(parms['light']) > 9):
        result = {'status': 'error: above bound light value'}
    if (int(parms['light']) < 0):
        result = {'status': 'error: below bound light value'}
    if (isinstance(int(parms['light']), int)):
        result = {'status': 'error: non-integer light value'}
        
    return result
