def _create(parms):
    # Light sad path boundary check
    if (parms['light'] == None):
        return {'status': 'error: Null light value'}
    try: (int(parms['light']))
    except ValueError:
        return {'status': 'error: non-integer light value'}
    if (int(parms['light']) > 9):
        result = {'status': 'error: above bound light value'}
    elif (int(parms['light']) < 0):
        result = {'status': 'error: below bound light value'}

    # dark sad path boundary check
    return result
