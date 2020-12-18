def strchallenge(word):
    y = list(word)
    cx = 0
    co = 0
    for x in y:
        if x == 'x':
            cx += 1
        elif x == 'o':
            co += 1
    if cx == co:
        print('true')
        print('no of x are ', cx)
        print('no of o are ', co)
    else:
        print('flase')
        print('no of x are ', cx)
        print('no of o are ', co)

strchallenge('xoxxxxx')