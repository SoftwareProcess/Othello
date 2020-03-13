def _create(parms):
    if (parms['light'] > 9):
        result = {'status': 'error: above bound light value'}
    if (parms['light'] < 0):
        result = {'status': 'error: below bound light value'}
    return result
