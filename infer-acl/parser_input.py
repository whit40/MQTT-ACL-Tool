import getopt
import sys


# Gets the list of topics to check from user-supplied file.
def getTopicsFromFile(input_file):
    topiclist = []

    if input_file != "none":
        f = open(input_file, "r")
        for topic in f:
            topiclist.append(topic.rstrip())
        f.close()

    return topiclist


def parse_args(argv):

    # Get user arguments
    try:
        opts, args = getopt.getopt(argv, "hu:p:i:H:")
    except getopt.GetoptError:
        print("Please check usage with -h")
        sys.exit(2)

    username = "none"
    password = "none"
    input_file = "none"
    hostname = "none"

    # Check user arguments and act accordingly.
    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ")
            print("-h : show this dialogue")
            print("-i : Specify input file of topics. Each topic should be on a new line.")
            print("-u : Specify MQTT username")
            print("-p : Specify MQTT password")
            print("-H : Specify MQTT hostname")
            sys.exit(1)
        elif opt == '-i':
            input_file = arg
        elif opt == '-u':
            username = arg
        elif opt == '-p':
            password = arg
        elif opt == '-H':
            hostname = arg

    topiclist = getTopicsFromFile(input_file)

    return username, password, topiclist, hostname

