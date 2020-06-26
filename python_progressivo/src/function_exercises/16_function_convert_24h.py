def convert_24h():
    hour = int(input("Insert hour:"))
    min = int(input("Insert minutes:"))
    if hour <= 12:
        print(hour, ":", min, am_pm())
    elif hour > 12:
        if hour == 13:
            hour = 1
        elif hour == 14:
            hour = 2
        elif hour == 15:
            hour = 3
        elif hour == 16:
            hour == 4
        elif hour == 17:
            hour == 5
        elif hour == 18:
            hour == 6
        elif hour == 19:
            hour == 7
        elif hour == 20:
            hour == 8
        elif hour == 21:
            hour == 9
        elif hour == 22:
            hour == 10
        elif hour == 23:
            hour == 11
        elif hour == 24:
            hour == 0
        print(hour, ":", min, am_pm())
        return hour, ":", min, am_pm()


def am_pm():
    am_or_pm = input("AM or PM?")
    if am_or_pm == 'AM':
        return 'AM'
    elif am_or_pm == 'PM':
        return 'PM'


convert_24h()
