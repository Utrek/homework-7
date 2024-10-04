from models import Stack

def check_bracket_balance(string):
    stack = Stack()   
    for i in string:
        if i in ['(', '{', '[']:
            stack.push(i)
        elif i in [')', '}', ']']:
            if stack.is_empty():
                result ='Несбалансировано'
                break
            else:
                top = stack.pop()
                if (i == ')' and top == '(') or (i == '}' and top == '{') or (i == ']' and top == '['):
                    continue
                else:
                    result ='Несбалансировано'
                    break
        else:
            result = f'Неправильный символ: {i}'
            break 
    if 'result' in locals():
        return result
    elif stack.is_empty():
        result ='Сбалансировано'
    else:
         result ='Несбалансировано'   
    return result



