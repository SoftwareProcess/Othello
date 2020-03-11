def _create(light, dark, blank):
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
    if (isinstance(dark, str)):
        result = {'status':'error: Non integer dark'}
    elif (dark == None):
        result = {'status':'error: Null dark'}
    elif (dark > 9):
        result = {'status':'error: Above bound dark integer'}
    elif (dark < 0):
        result = {'status':'error: Below bound dark integer'}
    
    # Checking boundary for blank
    if (isinstance(blank, str)):
        result = {'status':'error: Non integer blank'}
    elif (blank > 9):
        result = {'status':'error: Above bound blank integer'}
    elif (blank < 0):
        result = {'status':'error: Below bound blank integer'}
    return result
