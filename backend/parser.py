

def judgeText (inp):

    if (len(inp) > 10 and len(inp) <= 30):
        print('Not bad')
        return "not bad"
    elif (len(inp) > 30 and len(inp) <= 50):
        print('nice')
        return "Nice"
    else:
        print('wtf')
        return "Wtf chill out"
    