def findProfession(level, pos):
    if level == 1:
        return 'Engineer'
        
    if (findProfession(level - 1, (pos + 1) // 2) == 'Doctor'): 
        if (pos % 2 == 1): 
            return 'Doctor'
        else: 
            return 'Engineer'
            
    if (pos % 2 == 1): 
        return 'Engineer'
    else: 
        return 'Doctor'

