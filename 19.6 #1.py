def readposint():
    while True:
        user_input = input("Enter a positive integer: ").strip()

        if not user_input:
            print("You must enter something.")
            continue

        try:
            num = int(user_input)
            if num <= 0:
                print("The number must be positive.")
                continue
            return num
        except ValueError:
            print("That is not a valid integer.")
