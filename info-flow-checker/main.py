import sys
import parse_input


def main(argv):
    print("Reading input")

    #  Get necessary information from user provided ACL file.
    userlist = parse_input.parse_input(argv)

    # create list of topics using dict of users and their topics
    all_topics = {}

    for user in userlist:
        for topic in user.topics:
            all_topics[topic] = {}

    for user in userlist:
        for topic in user.topics:
            all_topics[topic][user.name] = (user.permission,user.topics[topic])

    # We now have, for each topic, each user with access to the topic and their permission information.

    # for each topic, check the users. If a low and high user are present,
    # check against the integrity policy. If not permitted, print it.

    for topic in all_topics:
        print("Now checking topic: ", topic)
        for user1 in all_topics[topic]:
            user1_permission = all_topics[topic][user1][0]
            for user2 in all_topics[topic]:
                if user2 != user1:
                    user2_permission = all_topics[topic][user2][0]
                    if user2_permission != user1_permission:
                        if user1_permission == 'low' and user2_permission == 'high':
                            if all_topics[topic][user1][1] == "write" or all_topics[topic][user1][1] == "readwrite":
                                if all_topics[topic][user2][1] != "write":
                                    print("violation with users: (", user1,",", user2, ") on topic: ", topic)


if __name__ == "__main__":
    main(sys.argv[1:])