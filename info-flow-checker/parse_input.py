

class mqtt_user:
    def __init__(self, name, permission):
        self.name = name
        self.permission = permission
        self.topics = {}

def parse_input():

    usernamelist = []

    input_file = "C:\\Users\\Andrew\\Documents\\CSE_543\\acl.txt"

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
        # print(line)
        if len(line) > 3:
            splitline = line.split()
            if splitline[0] == 'user':
                for user in userlist:
                    if user.name == splitline[1]:
                        user.permission = splitline[2]
                        currentuser = user
                        # print("current user is now: ", currentuser.name, currentuser.topics)
            if splitline[0] == 'topic':
                topic = splitline[2]
                rw_permission = str(splitline[1])
                # print("Adding topic: ", topic, "To user: ", currentuser.name, currentuser.topics)
                currentuser.topics[topic] = rw_permission
                # print("User is: ", currentuser.name, currentuser.topics)
    f.close()

    return userlist
