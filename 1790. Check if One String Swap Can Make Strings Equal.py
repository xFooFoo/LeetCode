s1 = "bank"
s2 = "banks"

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Must be same length at least
        if (len(s1) != len(s2)): return False

        counter = 0
        missing1 = set()
        missing2 = set()

        for i in range(0, len(s1)):
            if s1[i] != s2[i]:
                missing1.add(s1[i])
                missing2.add(s2[i])
                counter += 1
                
        return (counter <= 2 and missing1 == missing2)

print(Solution().areAlmostEqual(s1,s2))