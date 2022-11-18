initial = "( A + B ) * C"
equation = list(initial) 
operator = ["+","-","*","/"]
Current = "" 
Out = [ ] 
Operator = [ ]
Result = '' 
def postfix(input):
    if input in operator:
        if (((input == "/") or (input == "*")) and (Operator != [ ])):
            if ((Operator[-1] == "*") or (Operator[-1] == "/")):
                Out.append(Operator.pop())
                Operator.append(equation.pop(0))
            else:
                Operator.append(equation.pop(0))
        else:
            if (Operator != [ ]):
                if (((input == "+") or (input == "-")) and ((Operator[-1] == "*") or (Operator[-1] == "/"))):
                    Out.append(Operator.pop())
                    while len(Operator) > 0:
                        Out.append(Operator.pop())
                else:
                    Operator.append(equation.pop(0))
            else:
                    Operator.append(equation.pop(0))
    else:
                    Operator.append(equation.pop(0))

while len(equation) > 0:
    Current = equation[0]
    postfix(equation[0])

while len(Operator) > 0:
    Out.append(Operator.pop())

for i in Out: 
    Result += i

print("Initial value : " + initial)
print("Result value : " + Result)




















