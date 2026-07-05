class Solution:
    def isValid(self, s: str) -> bool:
    # We map each closing bracket to an open one
    # When we see a closing bracket, try to match it with the last thing in our queue

    # EG -> "([{}])" 
    # stack = ["("]
    # ...
    # stack = ["(", "[", "{"]
    # We see }, pop, ], pop, in the case we cant pop, return false
        close_to_open = { "}" : "{", ")" :"(", "]" : "[" } 
        stack = []
        for bracket in s:
            if bracket in close_to_open.values():
                stack.append(bracket)
            else: 
                if stack and stack[-1] == close_to_open[bracket]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True