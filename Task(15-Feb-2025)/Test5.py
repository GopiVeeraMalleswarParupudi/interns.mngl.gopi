while True:
    a = input("Enter Anything: ")  # Get user input
    if a.lower() == 'exit':  # Exit condition for the loop
        print("Exiting program.")
        break
    # Check if it's an integer
    is_int = True
    for char in a:
        if char not in "0123456789":
            is_int = False
            break
    if is_int:
        print("It is an Int")
        continue  # Skip to the next loop iteration
    # Check if it's a float
    is_float = False
    dot_count = 0
    for char in a:
        if char == '.':
            dot_count += 1
        elif char not in "0123456789":
            is_float = False
            break
        else:
            is_float = True
    if dot_count == 1 and is_float:
        print("It is a Float")
        continue  # Skip to the next loop iteration
    # Check if it's a boolean (True or False)
    if a.lower() == "true" or a.lower() == "false":
        print("It is a Bool")
        continue  # Skip to the next loop iteration
    # If none of the above, it's a string
    print("It is a Str")