def _create(light, dark, blank, size):
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
    elif (blank == None):
        result = {'status':'error: Null blank'}
    elif (blank > 9):
        result = {'status':'error: Above bound blank integer'}
    elif (blank < 0):
        result = {'status':'error: Below bound blank integer'}
    
    # Checking boundary for size
    if (isinstance(size, float)):
        result = {'status':'error: Non integer size'}
    elif (size == None):
        result = {'status':'error: Null size'}
    elif (size > 16):
        result = {'status':'error: Above bound size integer'}
    elif (size < 6):
        result = {'status':'error: Below bound size integer'}
    
    return result
