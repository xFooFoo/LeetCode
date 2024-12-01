class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        num = list(num)
        n = len(num)
        currProduct = 1
        for i in range(n):
            currDigit = num[i] 

            if currDigit == "0":
                num[i] = "1"
            currProduct *= int(num[i])

        if currProduct % t == 0:
            return ''.join(num)

        
        t_factors = []
        for i in range(2,10):
            if t % i == 0:
                t_factors.append(str(i))
        
        print(t_factors)

        for i in range(n-1, -1, -1):
            for factor in t_factors:
                currProduct /= int(num[i])
                num[i] = factor
                currProduct *= int(num[i])
                if currProduct % t == 0:
                    return ''.join(num) 

        return "-1"


#print(Solution().smallestNumber("10", 320))
print(Solution().smallestNumber("11111", 26))