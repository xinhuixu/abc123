password = "Pa5$word"

def charMap(letter):
    if letter.isdigit():
        return "num"
    elif letter.isupper():
        return "upper"
    elif letter.islower():
        return "lower"
    elif letter in ".?!&#,;:-_ *":
        return "symb"

def simpleCheck(password):
    makeup = [ charMap(i) for i in password ]
    return "num" in makeup and "upper" in makeup and "lower" in makeup

def passRate(password):
    makeup = [ charMap(i) for i in password ]
    lenRating = len(password)/15.0 if len(password) < 15 else 1
    print (("num" in makeup)*2.5 + ("upper" in makeup)*2.5 + ("lower" in makeup)*2.5 + ("symb" in makeup)*2.5) * lenRating
