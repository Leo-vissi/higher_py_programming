#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import argv

    stor = len(argv) - 1
    
    if stor == 0:
        print("0 arguments.")
    
    else if stor == 1:
        print("1 argument:")
    
    else:
        print("{} arguments:".format(stor))

    for i in range(stor):
        print("{}: {}".format(i + 1, argv[i + 1]))
