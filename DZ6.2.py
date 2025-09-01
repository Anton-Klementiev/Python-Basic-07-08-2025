user_input = int(input("Enter between 0 and 8640000 seconds to transform into time : "))

if user_input >= 8640000 or user_input < 0:
    print("Invalid input: number must be between 0 and 8640000")
else:
    seconds = str(user_input % 60).zfill(2)
    total_mins = user_input // 60
    mins = str(total_mins % 60).zfill(2)
    total_hours = total_mins // 60
    hours = str(total_hours % 24).zfill(2)
    days = total_hours // 24
    if days in (5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20) or days % 10 == 0:
        word_for_day = 'днів'
    elif days % 10 in (2,3,4):
        word_for_day = 'дні'
    elif days % 10 in (5,6,7,8,9):
        word_for_day = 'днів'
    elif days % 10 == 1 or days == 1:
        word_for_day = 'день'
    else:
        word_for_day = 'днів'

    print(f"{user_input} seconds is: {days} {word_for_day}, {hours}:{mins}:{seconds}")

