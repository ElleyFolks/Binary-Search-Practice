def binary_search(sorted_list, input_key):
    low = 0
    high = len(sorted_list)-1  # getting last index value
    mid = (high + low) // 2

    while (high >= low):
        mid = (high + low) // 2

        if (sorted_list[mid] < input_key):
            low = mid+1

        elif (sorted_list[mid] > input_key):
            high = mid-1

        else:
            return mid  # index value for mid

    return -1  # if returned, not found


# main program
numbers = [2, 6, 7, 8, 10]

user_input = ' '  # set as default, reassigned iff user enters valid input

while (user_input == ' '):
    try:
        user_input = int(input("Please enter a number to search.\n"))
    except:
        print("Not a number, please try again.")

index = binary_search(numbers, user_input)
if (index == -1):
    print("not found")
else:
    print("number found at index: ", index)
