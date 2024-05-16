player = input('do you want play? ')

if player != "yes":
    quit()

print('lets play')
score=0

qustion = input("how many days do we have in a week? ")

if qustion.lower() =="seven":
    print('correct')
    score += 1
else:
    print('not_correct')


qustion = input(" Who heads the RBI? ")

if qustion.lower() =="governer":
    print('correct')
    score += 1
else:
    print('not_correct')

qustion = input(" What is the currency of India? ")

if qustion.lower() =="rupee":
    print('correct')
    score += 1
else:
    print('not_correct')

qustion = input(" When was India's independence month? ")

if qustion.lower ()=="august":
    print('correct')
    score +=1
else:
    print('not_correct')

qustion = input(" Where is India's Silicon Valley located? ")

if qustion.lower ()=="benguluru":
    print('correct')
    score += 1
else:
    print('not_correct')
    print("your score"+str(score))