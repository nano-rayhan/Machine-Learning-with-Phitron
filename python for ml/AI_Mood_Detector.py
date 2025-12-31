massage = input().lower().split()


for i in massage:
    if i == ['happy','joy','smile']:
        print('Happy Mood')
        break
    else:
        print('Neutral Mood')
        break
