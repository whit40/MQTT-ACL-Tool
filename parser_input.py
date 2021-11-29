# Function(s) to parse user input go here
import getopt
import sys


def parse_args(argv):

    try:
        opts, args = getopt.getopt(argv, "hu:p:i:")
    except getopt.GetoptError:
        print("Please check usage with -h")
        sys.exit(2)

    username = "none"
    password = "none"

    for opt, arg in opts:
        if opt == '-h':
            print("Useage info here")
        elif opt == '-i':
            print("input file")
        elif opt == '-u':
            username = arg
        elif opt == '-p':
            password = arg

    return username, password
