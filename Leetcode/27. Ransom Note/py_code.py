class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
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
