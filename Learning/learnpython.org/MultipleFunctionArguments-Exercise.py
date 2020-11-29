#MultipleFunctionArguments-Exercise.py
def foo(a, b, c, *extras):
    if extras:
        return len(extras)

def bar(a, b, c, **options):
    if options.get("magicnumber") == 7:
        return True
    else:
        return False

#tests
if foo(1,2,3,4) == 1:
    print("Good.")
if foo(1,2,3,4,5) == 2:
    print("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print("Awesome!")