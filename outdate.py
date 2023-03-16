months = {
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    }

while True:
    #MM/DD/YYYY
    date = input("Date: ")

    #yyyy/mm/dd
    if len(date.split("/")) > 2:
        mm, dd, yyyy = date.split("/")
    else:
        date = date.replace(",", "").split(" ")

        for _ in range(len(date)):
            if int(date[_]) < 32:
                dd = date[_]
            else:
                yyyy = date[_]

    if int(mm) < 12 and int(dd) < 31:
        print(f"{yyyy}-{mm:0>2}-{dd:0>2}")                    