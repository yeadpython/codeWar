import string

def pig_it(text):
    """
    pig_it('Pig latin is cool') # igPay atinlay siay oolcay
    pig_it('Hello world !')     # elloHay orldway !
    """
    x = text.split()

    new_text = ""

    for i in x:
        if i not in string.punctuation:
            new_text += i[1:] + i[0] + "ay" + " "
        else:
            new_text += i
    new_text.rstrip

    return new_text


print(pig_it('Pig latin is cool'))