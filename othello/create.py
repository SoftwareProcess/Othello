def _create(light = None):
    if (isinstance(light, str)):
        result = {'status':'error: Non integer light'}
    elif (light > 9):
        result = {'status': 'error: Above bound light integer'}
    elif (light < 0):
        result = {'status': 'error: Below bound light integer'}
    return result
