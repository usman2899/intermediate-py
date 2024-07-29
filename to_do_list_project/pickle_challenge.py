import pickle


def depickle_to_string(pickled_data):
    list_str = pickle.loads(pickled_data)
    the_string = ""
    for str in list_str:
        the_string += str
        the_string += " "

    return the_string
the_data = b'\x80\x04\x95/\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x05Great\x94\x8c\x03job\x94\x8c\tfinishing\x94\x8c\x03the\x94\x8c\x07course!\x94e.'

result = depickle_to_string(the_data)
print(result)