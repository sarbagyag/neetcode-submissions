class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenMap={")":"(", "}":"{", "]":"["}
        stack=[]

        for c in s:
            if(stack and c in closeToOpenMap):
                if(stack[-1]!=closeToOpenMap[c]):
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        else:
            return False

        
            

        