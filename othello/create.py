def _create(light = None):
    if (isinstance(light, str)):
        result = {'status':'error: Non integer light'}
    if (light > 9):
        result = {'status': 'error: Above bound light integer'}
    if (light < 0):
        result = {'status': 'error: Below bound light integer'}
    return result
