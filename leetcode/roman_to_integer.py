class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        toDigit = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        prevDigit = None
        
        for c in s:
            digit = toDigit[c]
            if prevDigit is None:
                prevDigit = digit
                
            elif digit > prevDigit:
                result += (digit - prevDigit)
                prevDigit = None
                
            elif digit == prevDigit:
                result += digit
            
            else:
                result += prevDigit
                prevDigit = digit
                
        if prevDigit is not None:
            result += prevDigit
                
            
                
        return result