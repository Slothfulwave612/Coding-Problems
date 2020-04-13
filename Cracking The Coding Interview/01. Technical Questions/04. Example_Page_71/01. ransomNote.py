'''
Example: A ransom note can be formed by cutting words out of a magazine to form a new
sentence. How would you figure out if a ransom note (represented as a string) can be formed
from a given magazine (string)?

e.g.
canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''

def canConstruct(ransomNote, magazine):
    '''
    Function will tell wheter ransom note can be generated or not.

    Arguments:
    ransomNote -- str, the original note.
    magazine -- str, words/chars from magazine.

    Returns:
    True -- if generated.
    False -- if not.
    '''
    if len(ransomNote) == 0 and len(magazine) == 0:
        return True
    elif len(ransomNote) == 0 and len(magazine) != 0:
        return True
        
    elif len(ransomNote) != 0 and len(magazine) == 0:
        return False
    
    length = len(ransomNote)
    
    hash_table = [0] * 256
    
    for word in ransomNote:
        hash_table[ord(word)] += 1
    
    for word in magazine:
        if hash_table[ord(word)] != 0:
            hash_table[ord(word)] -= 1
            length -= 1
            if length == 0:
                return True
    
    return False

print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))
