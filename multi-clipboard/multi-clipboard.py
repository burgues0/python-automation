import getopt, sys
import clipboard
import json

arg_list = sys.argv[1:]
options = "hc:pl"
long_options = ["help", "copy =", "paste", "list"]

try:
    arguments, values = getopt.getopt(arg_list, options, long_options)

    for cur_arg, cur_value in arguments:
        if(cur_arg in ("-h", "--help")):
            print("\n Syntax \n     python multi-clipboard.py [options ...] \n\n Options \n\n -c [arg] | --copy [arg] \n Copies to your clipboard (Ctrl + V) the value of the data that corresponds to the key [arg].")
        elif(cur_arg in ("-c", "--copy")):
            print()
        elif(cur_arg in ("-p", "--paste")):
            print()
        elif(cur_arg in ("-l", "--list")):
            print()

except getopt.error as err:
    print(str(err))


#if len(sys.argv) == 2:
    #arg = sys.argv[1]

    #if(arg != "save" and arg != "load" and arg != "list"):
    #    print("Command not found.")

#else:
    #print("Invalid arguments. ")