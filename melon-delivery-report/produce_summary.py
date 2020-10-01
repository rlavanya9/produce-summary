def summary(day_no, path):
    print("Day",day_no)
    # path will be passed as file name
    the_file = open(path)
    # logic is the same for all three files
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')
# the first value in list gives melon, second gives count and third gives amount
        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

summary(1, "um-deliveries-20140519.txt")
summary(2, "um-deliveries-20140520.txt")
summary(3, "um-deliveries-20140521.txt")
    
