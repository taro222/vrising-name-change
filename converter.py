import sys

def find_and_replace(filename, old_name, new_name):
    with open(filename, 'rb') as file:
        data = file.read()

    old_name_bytes = old_name.encode()
    new_name_bytes = new_name.encode()

    occurrences = data.count(old_name_bytes)
    replaced_count = 0

    if len(new_name_bytes) >= 3 and len(new_name_bytes) <= 20:
        while occurrences > 0:
            index = data.index(old_name_bytes)
            length_index = index - 2

            name_length = int.from_bytes(data[length_index:length_index+2], byteorder='little')

            if name_length == len(old_name_bytes):
                data = data[:length_index] + len(new_name_bytes).to_bytes(2, byteorder='little') + data[length_index+2:]
                data = data[:index] + new_name_bytes + data[index + len(old_name_bytes):]
                replaced_count += 1

            occurrences -= 1

        with open(filename, 'wb') as file:
            file.write(data)

        print(f'The name was successfully changed in {replaced_count} entries.')
    else:
        print('The new name must have at least 3 characters and cannot exceed 20 characters.')

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Please provide the filename, old name, and new name as arguments.')
    else:
        filename = sys.argv[1]
        old_name = sys.argv[2]
        new_name = sys.argv[3]
        find_and_replace(filename, old_name, new_name)
