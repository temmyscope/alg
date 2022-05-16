"""
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.
"""

def getLongestPalindrome(word: str):
    reversedWordList = list(word)
    reversedWordList.reverse()
    reversedWord: str = ''.join(reversedWordList)
    length = len(word)

    streakHasEnded = False
    streakList = []
    streak = ""

    for i  in range(length):
        if reversedWord[i] == word[i]:
            if streakHasEnded == True:
                streak = word[i]
                streakHasEnded = False
            else:
                streak = streak + word[i]
                streakHasEnded = False
        else:
            streakHasEnded = True

        streakList.append(streak)
    
    return max(streakList, key=len)

print(
    getLongestPalindrome("babad")
    #getLongestPalindrome("cbbd")
)