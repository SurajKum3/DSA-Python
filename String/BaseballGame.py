#  -> Used a stack to maintain valid round scores dynamicall, each operation (C, D, +, or number) is processed in order, leveraging the stack’s LIFO nature to access recent scores efficiently.

#  -> Time Complexity : O(n) - Each operation is processed once, and all stack operations (push, pop, peek) run in constant time.

#  -> Space Complexity : O(n) - In the worst case, all operations are valid scores and stored in the stack.👇

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)