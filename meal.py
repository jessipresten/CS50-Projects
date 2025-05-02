def main():
#ask user for input
    time = input("What time is it? ")

#call convert
    convert_time = convert(time)

#verify hours
    if convert_time >= 7 and convert_time <= 8:
       print("Breakfast")
    elif convert_time >= 12 and convert_time <= 13:
       print("Lunch")
    elif convert_time >= 18 and convert_time <= 19:
       print("Dinner")


def convert(time):
    hours, minutes = time.split(":")
    
    new_hours = float(hours)
    new_minutes = float(minutes)
    convert_time = new_hours + new_minutes
    return convert_time



if __name__ == "__main__":
 main()




