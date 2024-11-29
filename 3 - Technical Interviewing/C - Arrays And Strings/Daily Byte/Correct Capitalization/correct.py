def correctCapitalization(strVal):
    if not strVal or len(strVal) == 0:
        return False
        
    if strVal.upper() == strVal:
        return True
    
    if strVal.lower() == strVal:
        return True

    if strVal[0].upper() == strVal[0] and strVal[1:len(strVal)].lower() == strVal[1:len(strVal)]:
        return True

    return False