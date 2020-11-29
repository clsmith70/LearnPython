#ExceptionHandling.py
## Iterator always runs 20 times, but the list is shorter.
## just process remaining missing indices with 0

def do_stuff_with_number(n):
    print(n)
    
def catch_this():
    the_list = (1, 2, 3, 4, 5)
    
    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: #raised when accessing a non-existing index
            do_stuff_with_number(0)
                
catch_this()