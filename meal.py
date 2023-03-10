#meal time

def main():

    text_time = convert(input("what time is it? "))

    if 7 <=  text_time <= 8:
       print("Breakfast time")
    elif 12 <= text_time <= 13:
       print("Lunch time")
    elif 18 <=  text_time <= 19:
       print("Dinner time")
    else:
       print("if you eat you'll be fat")

def convert(time):
    hours, minutes =  time.split(":")
    convert_time = float(minutes) / 60
    return float(hours) + convert_time 
main()