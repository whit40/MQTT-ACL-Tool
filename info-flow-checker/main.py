import sys
import parse_input


def main(argv):
    print("Reading input")
    #  Get user input from CLI and files?
    userlist = parse_input.parse_input()
    for user in userlist:
        print(user.name, user.permission, user.topics)

    # create list of topics using dict of users and their topics
    # list the users and their permissions under each topic
    all_topics = {}

    for user in userlist:
        for topic in user.topics:
            all_topics[topic] = {}

    for user in userlist:
        for topic in user.topics:
            all_topics[topic][user.name] = (user.permission,user.topics[topic])

    print("All topics: ", all_topics)

    # for each topic, check the users. If a low and high user are present,
    # check against permitted high/low pairs. If not permitted, record it.

    for topic in all_topics:
        print("Now checking topic: ", topic)
        for user1 in all_topics[topic]:
            user1_permission = all_topics[topic][user1][0]
            for user2 in all_topics[topic]:
                if user2 != user1:
                    user2_permission = all_topics[topic][user2][1]
                    if user2_permission != user1_permission:
                        if user1_permission == 'low':
                            # print("User is: ", user1.name)
                            if all_topics[topic][user1][1] == "write" or all_topics[topic][user1][1] == "readwrite":
                                print("violation with users: (", user1,",", user2, ") on topic: ", topic)



    # print/log all recorded violations



if __name__ == "__main__":
    main(sys.argv[1:])