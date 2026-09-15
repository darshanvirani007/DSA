def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
    
        for char in t:
            if char in count_t:
                count_t[char] += 1
            else:
                count_t[char] = 1
    
        return count_s == count_t

def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t