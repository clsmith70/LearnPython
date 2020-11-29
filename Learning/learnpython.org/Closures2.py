#Closures2.py
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
    return data_transmitter

fun = transmit_to_space("Burn the Sun!")
fun()