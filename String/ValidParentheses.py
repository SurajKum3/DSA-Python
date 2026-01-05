#  -> Stack Data Structure:- Stack helps match brackets in correct order and nesting.
#  -> Time Complexity : O(n) - Each character is processed once.
#  -> Space Complexity : O(n) - Stack may store all opening brackets. 👇

class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        a=[]
        for i in range(len(s)):
            if s[i]== '(' or s[i]== '[' or s[i]== '{' :
                a.append(s[i])
            else:
                if not a:
                    return False
                top=a.pop()
                if s[i]==')' and top!='(':
                    return False
                if s[i]==']' and top!='[':
                    return False
                if s[i]=='}' and top!='{':
                    return False
        return len(a)==0