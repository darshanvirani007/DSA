# LeetCode 49 — Group Anagrams
def groupAnagrams(strs):
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))