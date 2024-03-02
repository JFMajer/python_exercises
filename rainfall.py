def rainfall():
    rainfall_data = {}
    while True:
        city = input("Enter a city: ")
        if not city:
            break
        rainfall_in = input("How much rainfall: ")
        try:
            rainfall_mm = int(rainfall_in)
            rainfall_data[city] = rainfall_data.get(city,
                                                    0) + rainfall_mm  # Add rainfall to city, using get() for default 0 if city not yet in dict
            # if city in rainfall_data:
            #     rainfall_data[city] += rainfall_mm
            # else:
            #     rainfall_data[city] = rainfall_mm
        except ValueError:
            print("Please enter rainfall amount as whole number")

    for city, total_rainfall in rainfall_data.items():
        print(f"{city}: {total_rainfall}")


rainfall()
