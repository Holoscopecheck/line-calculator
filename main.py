from collections import deque

mystack = deque([])

test_text = "1 2 + 3 * 4 5 * +"
tokens = test_text.split()

for ele in tokens:
    match ele:
        case '+':
            ope1 = int(mystack.pop())
            ope2 = int(mystack.pop())
            result = ope1 + ope2
            mystack.append(result)
        case '-':
            ope1 = int(mystack.pop())
            ope2 = int(mystack.pop())
            result = ope1 - ope2
            mystack.append(result)
        case '*':
            ope1 = int(mystack.pop())
            ope2 = int(mystack.pop())
            result = ope1 * ope2
            mystack.append(result)
        case '/':
            ope1 = int(mystack.pop())
            ope2 = int(mystack.pop())
            result = ope1 / ope2
            mystack.append(result)
        case _:
            mystack.append(ele)


result = mystack.pop()
print(result)
                
