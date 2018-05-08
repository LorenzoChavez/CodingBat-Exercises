# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). 
# So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):
    counter = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'xyz' and str[i-1] != '.':
            counter += 1
    return counter > 0
