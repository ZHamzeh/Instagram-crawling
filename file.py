def read_file(file):
    fi = open(file)
    list = fi.read()
    list = list.split()
    fi.close()
    return list
