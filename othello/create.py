def _create(light):
    if (light > 9):
        result = {'status': 'error: Above bound light integer'}
    if (light < 0):
        result = {'status': 'error: Below bound light integer'}
    return result
