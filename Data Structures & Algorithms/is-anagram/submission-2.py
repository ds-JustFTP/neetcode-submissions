class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
sol = Solution()
print(sol.isAnagram(s = "racecar", t = "carrace"))   
print(sol.isAnagram(s = "jar", t = "jam"))