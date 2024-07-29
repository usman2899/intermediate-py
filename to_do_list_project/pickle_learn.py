import pickle

age = 2131212
file_name = "pickle_text.txt"

file = open(file_name, "wb")
pickle.dump(age, file)
file.close

file = open(file_name, "rb")
read_age = pickle.load(file)
file.close

print(read_age)