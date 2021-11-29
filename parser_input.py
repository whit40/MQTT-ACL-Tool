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
    input_file = "none"

    for opt, arg in opts:
        if opt == '-h':
            print("Useage info here")
        elif opt == '-i':
            input_file = arg
        elif opt == '-u':
            username = arg
        elif opt == '-p':
            password = arg

    topiclist = []

    if input_file != "none":
        f = open(input_file, "r")
        for topic in f:
            topiclist.append(topic.rstrip())
        f.close()
        print(topiclist)

    return username, password, topiclist
