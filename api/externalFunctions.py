'''
    This page contains extra functions that support the main prediction functions
'''

def quick_decode(y):
    if y == 1:
        y = "podium"
    if y == 2:
        y = 'the Points'
    if y == 3:
        y = 'out of the Points'
    return y