#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

count = len(argv)

if count == 1:
     print("0 arguments.")

else if count > 1:
     print("{} argument{}".format
             (count-1, " " 
              if count > 2 else ":"))

for i in range(1, count):
     print("{} : {}".format(i, argv[i]))
