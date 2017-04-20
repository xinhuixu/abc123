password = "A$DFE$jjg4583"

def somethingsomething(letter):
    if letter.isdigit():
        return "num"
    elif letter.isupper():
        return "upper"
    elif letter.islower():
        return "lower"

def simpleCheck(password):
        makeup = [ somethingsomething(i) for i in password ]
        return "num" in makeup and "upper" in makeup and "lower" in makeup

print simpleCheck(password)
