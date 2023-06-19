import sys

def modify_hex_file(filename, old_name, new_name):
    with open(filename, 'rb') as file:
        hex_data = file.read()

    #Convert Names into HEX
    old_name_hex = old_name.encode()
    new_name_hex = new_name.encode()

    #lf old name
    if old_name_hex in hex_data:
        if len(new_name) > 20:
            print("Only up to 20 characters are allowed")
            return

        #replace name in hex
        hex_data = hex_data.replace(old_name_hex, new_name_hex)
        
        #length difference and fillers
        old_len = len(old_name)
        new_len = len(new_name)
        if old_len < new_len:
            hex_data = hex_data.replace(b'\x00' * (new_len - old_len), b'')
        elif old_len > new_len:
            hex_data = hex_data.replace(new_name_hex, new_name_hex + b'\x00' * (old_len - new_len))

        with open(filename, 'wb') as file:
            file.write(hex_data)

        print("Datei erfolgreich aktualisiert.")
    else:
        print("Alter Name nicht gefunden.")

#python converter.py filename.save Liv Mario
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Wrong arguments. python converter.py filename.save old_name new_name")
    else:
        filename = sys.argv[1]
        old_name = sys.argv[2]
        new_name = sys.argv[3]
        modify_hex_file(filename, old_name, new_name)
