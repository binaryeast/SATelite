import sys


def fileread(file):
    with open(file, "r") as f:
        plaintext = f.read()
        linetext = f.readlines()

    
def filewrite(file, data):
    with open(file, "w") as f:
        writing = f.write(data)


class a():
    pass