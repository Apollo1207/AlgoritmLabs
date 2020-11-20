def write_data(filename, data):
    data = str(data)
    with open(filename, 'w') as file:
        file.write(data)

