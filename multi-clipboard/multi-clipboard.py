import getopt, sys
import clipboard
import json

SAVED_DATA_PATH = "clipboard.json"

arg_list = sys.argv[1:]
options = "hc:p:ld:"
long_options = ["help", "copy =", "paste", "list", "delete"]

#function to store the current clipboard into an json file
def save_data(file_path, data):
    with open(file_path, "w") as store_data:
        json.dump(data, store_data)

#returns the current saved items fron the json
def load_data(file_path):
    try:
        with open(file_path, "r") as load_data:
            data = json.load(load_data)
            return data
    except:
        return {}

def delete_data(file_path, data):
    with open(file_path, "w") as new_stored_data:
        json.dump(data, new_stored_data)

try:
    arguments, values = getopt.getopt(arg_list, options, long_options)

    data = load_data(SAVED_DATA_PATH)

    for cur_arg, cur_value in arguments:
        #argument options
        if(cur_arg in ("-h", "--help")):
            #help argument, prints a basic documentation to help the user *****STILL NEEDS TO BE FINISHED*****
            print("\n Syntax \n     python multi-clipboard.py [options ...] \n\n Options \n\n -c [arg] | --copy [arg] \n Copies to your clipboard (Ctrl + V) the value of the data that corresponds to the key [arg].")

        elif(cur_arg in ("-c", "--copy")):
            #copy argument, copies data from the key passed in the command argument
            if(cur_value not in data):
                print(f"Key \"{cur_value}\" does not exist. Please insert a valid key.")
            else:
                clipboard.copy(data[cur_value])
                print(f"Data copied to the clipboard: \"{data[cur_value]}\"")
        elif(cur_arg in ("-p", "--paste")):
            #paste argument, pastes current clipboard onto the multi-clipboard assigning it to the key passed in the argument
            data[cur_value] = clipboard.paste()
            save_data(SAVED_DATA_PATH, data)
            print(f"Data saved into the key \"{cur_value}\": {data[cur_value]}")
        elif(cur_arg in ("-l", "--list")):
            for keys in data:
                print(f"------------------\n{keys} = \"{data[keys]}\"")
            print("------------------")
        elif(cur_arg in ("-d", "--delete")):
            for items in data:
                if(items == cur_value):
                    print(f"Item deleted: \"{items}\": \"{data[cur_value]}\"")
                    data.pop(cur_value)
                    break
            delete_data(SAVED_DATA_PATH, data)    

except getopt.error as err:
    print(str(err))