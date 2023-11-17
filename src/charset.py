'''chars generator'''
import random

def charset(value: int, numbers= False, symbols= False, letterless= False) -> str:
    '''
    GENERATOR
        // value is how long will be line
        // numbers is the presence of numbers in line
        // symbols is the presence of symbols in line
        // letterless remove letters
    '''
    chset = ''
    nuset = '1234567890' * 4
    syset = '-:;!?.,' * 6

    if not letterless:
        chset = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
    if numbers:
        chset += nuset
    if symbols:
        chset += syset

    line = ''.join([random.choice(chset) for x in range(value)]) if chset != '' else ''
    return line
