class Bracket:
    def __init__(self,bracket,position):
        self.bracket=bracket
        self.position=position

def bracketChecker(brackets):
    bracketStack=[]
    for i,char in enumerate(brackets,start=1):
        if char in ['(','[','{']:
            bracketStack.append(Bracket(char,i))

        elif char in [')',']','}']:
            if not bracketStack:
                return i

            top=bracketStack.pop()
            if (top.bracket=='(' and char !=')') or (top.bracket=='[' and char !=']') or (top.bracket=='{' and char !='}'):
                return i
                
    if bracketStack:
        top=bracketStack.pop()
        return top.position
    return 'Success'
brackets=str(input())

print(bracketChecker(brackets))