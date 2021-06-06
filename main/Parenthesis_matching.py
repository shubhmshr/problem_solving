from main.stack_adt import ArrayStack

def parenthesis_check(para):
    open_list = '({['
    close_list = ')}]'
    s = ArrayStack()
    for ele in para:
        if ele in open_list:
            #print("pushing",ele)
            s.push(ele)
        elif ele in close_list:
            if s.is_empty():
                print("Stack is empty")
                return False
            elif open_list.index(s.top()) != close_list.index(ele):
                return False
            else:
                s.pop()
    return s.is_empty()


if __name__ == '__main__':
    pass



