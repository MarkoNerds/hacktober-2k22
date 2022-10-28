'''Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]'''

# solution
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digit = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        def backtrack(i, currentString):
            if len(currentString) == len(digits):
                res.append(currentString)
                return
            for c in digit[digits[i]]:
                backtrack(i+1, currentString +c)
        if digits:
            backtrack(0, "")
        return res
            
