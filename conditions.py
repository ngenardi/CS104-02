while True:
    temp = float(input("Enter the temperature in degrees fahrenheit or enter \"999\" to end the program: "))

    if temp == 999:
        break
    elif temp > 90:
        print("Wear Shorts")
    elif temp > 70:
        print("Short sleeves are fine")
    elif temp > 50:
        print("Wear a jacket")
    elif temp > 32:
        print("Wear a heavy coat")
    else:
        print("Stay Inside")
