import getopt
import sys


class mqtt_user:
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission
        self.topics = {}


def get_input_file(argv):

    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print("Please check usage with -h")
        sys.exit(2)

    input_file = None

    for opt, arg in opts:
        if opt == '-h':
            print("Usage: ")
            print("-h : show this dialogue")
            print("-i : Specify input ACL file. ACL file must be edited such that a user's permission follows the "
                  "user name")
            sys.exit(1)
        elif opt == '-i':
            input_file = arg

    return input_file


def parse_input(argv):

    usernamelist = []

    input_file = get_input_file(argv)

    f = open(input_file, "r")

    for line in f:
        if len(line) > 3:
            splitline = line.split()
            if splitline[0] == 'user':
                usernamelist.append(splitline[1])
    f.close()

    userlist = []
    for username in usernamelist:
        userlist.append(mqtt_user(username, None))

    f = open(input_file, "r")
    currentuser = None
    for line in f:
        if len(line) > 3:
            splitline = line.split()
            if splitline[0] == 'user':
                for user in userlist:
                    if user.name == splitline[1]:
                        user.permission = splitline[2]
                        currentuser = user
            if splitline[0] == 'topic':
                topic = splitline[2]
                rw_permission = str(splitline[1])
                currentuser.topics[topic] = rw_permission
    f.close()

    return userlist
