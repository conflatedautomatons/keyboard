

qwerty  = '1234567890qwertyuiopasdfghjklzxcvbnm'
alpha   = '1234567890abcdefghijklmnopqrstuvwxyz'
dvorak  = '1234567890pyfgcrlaoeuidhtnsqjkxbmwvz'
# Except - Dvorak actually has only 7 letters on top row, includes punctuation 
colemak = '1234567890qwfpgjluyarstdhneiozxcvbkm'

def hop(keyFrom,keyboardFrom,keyboardTo):
    return keyboardTo[keyboardFrom.find(keyFrom)]

def loopFromStart(keyStart,keyFrom,keyboardFrom,keyboardTo):
    nextKey = hop(keyFrom,keyboardFrom,keyboardTo)
    if nextKey == keyStart:
        return keyFrom
    return keyFrom + loopFromStart(keyStart,nextKey,keyboardFrom,keyboardTo)

def loop(keyFrom,keyboardFrom,keyboardTo):
    return loopFromStart(keyFrom,keyFrom, keyboardFrom,keyboardTo)


import unittest

class TestKeyboard(unittest.TestCase):
    def testQ(self):
        self.assertEqual('a', hop('q',qwerty,alpha) )
        self.assertEqual('qakrdmztecvwbxugoihpj', loop('q',qwerty,alpha) )

    def testS(self):
        self.assertEqual('s', hop('l',alpha,qwerty) )
        self.assertEqual('sl', loop('s',alpha,qwerty) )


def printKeyboard(keyboardName,keyboard,keyboardTo=alpha):
        print ('=====' + keyboardName.upper() + '=====')
        for key in keyboard:
            print ( loop(key,keyboard,keyboardTo) )
        print (' \n ')

def keyboardLoops():
    printKeyboard('qwerty',qwerty)
    printKeyboard('dvorak',dvorak)
    printKeyboard('colemak',colemak)
    printKeyboard('dvorak to qwerty',dvorak,qwerty)
    printKeyboard('qwerty to dvorak',qwerty,dvorak)



if __name__ == '__main__':
    # unittest.main()
    keyboardLoops()

