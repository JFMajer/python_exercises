def run_timing():
    run_times = []
    while True:
        user_input = input("Enter 10 km run time: ")
        if user_input.strip() == "":
            if run_times:
                average_run = sum(run_times) / len(run_times)
                print(f"Average of {average_run:.2f}, over {len(run_times)}")
            else:
                print("No run times recorded")
            break
        else:
            try:
                run_time = float(user_input)
                if run_time < 0:
                    print("Please provide positive number")
                else:
                    run_times.append(run_time)
            except ValueError:
                print("Invalid input. Please enter a valid number.")


run_timing()
