def _create(parms):
    result = {'empty': 'empty'}
    # Light sad path boundary check
    if (parms['light'] == None):
        return {'status': 'error: Null light value'}
    try: (int(parms['light']))
    except ValueError:
        return {'status': 'error: non-integer light value'}
    if (int(parms['light']) > 9):
        return {'status': 'error: above bound light value'}
    elif (int(parms['light']) < 0):
        return {'status': 'error: below bound light value'}

    # dark sad path boundary check
    if (int(parms['dark']) > 9):
        return {'status': 'error: above bound dark value'}
    elif (int(parms['dark']) < 0):
        return {'status': 'error: below bound dark value'}
    return result
