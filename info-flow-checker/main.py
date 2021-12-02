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
            all_topics[topic][user.name] = user.permission

    print("All topics: ", all_topics)

    # for each topic, check the users. If a low and high user are present,
    # check against permitted high/low pairs. If not permitted, record it.

    permitted_pairs = {"test/message2": [('user', 'bob')]}

    for topic in all_topics:
        for user1 in all_topics[topic]:
            # print(user, all_topics[topic][user])
            user_permission = all_topics[topic][user1]
            current_user = user1
            for user2 in all_topics[topic]:
                if user2 != current_user:
                    if all_topics[topic][user2] != user_permission:
                        for pairuser1, pairuser2 in permitted_pairs[topic]:
                            if pairuser1 == current_user:
                                if pairuser2 == user2:
                                    print("no violation, mix permitted")
                            elif pairuser2 == current_user:
                                if pairuser1 == user2:
                                    print("no violation, mix permitted")
                            else:
                                print("violation with users: ", current_user, user2, "On topic: ", topic)


    # print/log all recorded violations



if __name__ == "__main__":
    main(sys.argv[1:])