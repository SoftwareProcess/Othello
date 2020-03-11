def _create(light, dark):
    # Checking boundary for light
    if (isinstance(light, str)):
        result = {'status':'error: Non integer light'}
    elif (light == None):
        result = {'status':'error: Null light'}
    elif (light > 9):
        result = {'status': 'error: Above bound light integer'}
    elif (light < 0):
        result = {'status': 'error: Below bound light integer'}
    
    # Checking boundary for dark
    if (dark > 9):
        result = {'status':'error: Above bound dark integer'}
    elif (dark < 0):
        result = {'status':'error: Below bound dark integer'}
    return result
