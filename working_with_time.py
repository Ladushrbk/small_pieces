import datetime

#1. approach based on time:
currentTime = datetime.datetime.now()
currentTime.hour

if currentTime.hour < 12:
    print("Good morning my player! I wish you a beautiful day, let's play with me!")
elif 12 <+ currentTime.hour < 18:
    print("Good afternoon my player! I wish you a lovely rest of your day, so let's play with me!")
else:
    print("Good evening my favorite player! Did you have a wonderful day? Let's play with me")