def _create(parms):
        
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
    if (parms['dark'] == None):
        return {'status': 'error: Null dark value'}
    try: (int(parms['dark']))
    except ValueError:
        return {'status': 'error: non-integer dark value'}
    if (int(parms['dark']) > 9):
        return {'status': 'error: above bound dark value'}
    elif (int(parms['dark']) < 0):
        return {'status': 'error: below bound dark value'}
    
    # blank sad path boundary check
    if (parms['blank'] == None):
        return {'status': 'error: Null blank value'}
    try: (int(parms['blank']))
    except ValueError:
        return {'status': 'error: non-integer blank value'}
    if (int(parms['blank']) > 9):
        return {'status': 'error: above bound blank value'}
    elif (int(parms['blank']) < 0):
        return {'status': 'error: below bound blank value'}
    
    # size sad path boundary check
    if (parms['size'] == None):
        return {'status': 'error: Null size value'}
    try: (int(parms['size']))
    except ValueError:
        return {'status': 'error: non-integer size value'}
    if (int(parms['size']) > 16):
        return {'status': 'error: above bound size value'}
    elif (int(parms['size']) < 6):
        return {'status': 'error: below bound size value'}
    elif (int(parms['size']) % 2 != 0):
        return {'status': 'error: Odd size value'}
    
    # Checking if values are equal to two different keys
    if (int(parms['light']) == int(parms['dark'])):
        return {'status': 'error: light is equal to dark value'}
    if (int(parms['light']) == int(parms['blank'])):
        return {'status': 'error: blank is equal to light value'}
    if (int(parms['dark']) == int(parms['blank'])):
        return {'status': 'error: dark is equal to blank value'}
    
    result = {'board': 0, 
              'tokens': {'light': int(parms['light']), 'dark': int(parms['dark']),
                         'blank': int(parms['blank'])
                         },
              'status': 'ok',
              'integrity': ''}
    if ('light' not in parms.keys()):
        parms['light'] = 1
        
    return result
