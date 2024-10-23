'''
ok_status = True
vowles = ['a', 'e', 'u', 'i', 'o']


def check_word(word):
    #global ok_status
    for i in vowles:
        if i in word:
            return True

    ok_status = False
    return False


print(check_word('adace'))
print(ok_status)
print(check_word('www'))
print(ok_status)
'''


def f():
    ok_status = True
    vowles = ['a', 'e', 'u', 'i', 'o']

    def check_word(word):
        global ok_status
        for i in vowles:
            if i in word:
                return True

        ok_status = False
        return False
    print(check_word('adace'))
    print(ok_status)
    print(check_word('www'))
    print(ok_status)

f()
print(ok_status)


ok_status = True
def f():
    ok_status = True
    vowles = ['a', 'e', 'u', 'i', 'o']

    def check_word(word):
        nonlocal ok_status
        for i in vowles:
            if i in word:
                return True

        ok_status = False
        return False
    print(check_word('adace'))
    print(ok_status)
    print(check_word('www'))
    print(ok_status)

f()
print(ok_status)


'''
ok_status = True
vowles = ['a', 'e', 'u', 'i', 'o']
def f():
    ok_status = True
    vowles = ['a', 'e', 'u', 'i', 'o']

    def check_word(word):
        #global ok_status
        nonlocal ok_status
        for i in vowles:
            if i in word:
                return True

        ok_status = False
        return False
    print(check_word('adace'))
    print(ok_status)
    print(check_word('www'))
    print(ok_status)

f()
print(ok_status)
'''

'''
x, y = 1, 2
#print(x)
#print(y)
def foo():
    global y
    if y == 2:
        x = 2
        print(x)
        y = 1

foo()
print(x)
if y == 1:
    x = 3
print(x)
'''

x = 1
def foo():
    #global x
    x = 2
    print(x)
foo()
print(x)

y = []
def bbb():
    for i in range(5):
        y.append(i)

bbb()
print(y)

y = []
def bbb(h):
    for i in range(5):
        h.append(i)

bbb(y)
print(y)