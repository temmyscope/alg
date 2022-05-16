"""
Given a string, find the length of the longest substring without repeating
characters.
"""

def getNonRepetitiveStrLength(word: str):
    encounteredStr = []
    strLength = len(word)
    lastIndex = strLength-1

    for i in range( lastIndex ):
        encounteredChar = ""
        for char in word[i:strLength]:
            if not char in encounteredChar:
                encounteredChar = encounteredChar + char
            else:
                break

        encounteredStr.append(encounteredChar)

    encounteredStr.sort( key=len )

    return [ encounteredStr[-1], len( encounteredStr[-1] ) ]
