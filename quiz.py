import time
score=0
count_down=60


starting_time=time.time()
print('QUIZ WORLD...')
print(' ')
print('QUESTION 1: Winner of FIFA WORLD CUP 2018 ?')
print('a:Germany','b:Brazil','c:Spain','d:France')
a=input('ANSWER:')
ending_time=time.time()
time_taken=ending_time-starting_time
count_down=count_down-time_taken
if count_down<=0:
    print('sorry<<<<<<< time out')
    exit()


if a=='d':
    print('correct answer')
    score=score+1
    print('Score =',score)
else:
    print('wrong answer')



starting_time=time.time()

print('QUESTION 2:How many districts in Kerala ?')
print('a:10','b:14','c:12','d:9')
b=input('ANSWER:')
ending_time=time.time()
time_taken=ending_time-starting_time
count_down=count_down-time_taken
if count_down<=0:
    print('sorry<<<<<<< time out')
    exit()

if b=='b':
    print('correct answer')
    score=score+1
    print('Score=',score)
else:
    print('wrong answer')



starting_time=time.time()
print('QUESTION 3:Capital of India ?')
print('a:Delhi','b:Mumbai','c:Kolkata','d:Kochi')
c=input('ANSWER:')

ending_time=time.time()
time_taken=ending_time-starting_time
count_down=count_down-time_taken
if count_down<=0:
    print('sorry<<<<<<< time out')
    exit()
if c=='a':
    print('correct answer')
    score=score+1
    print('score=',score)
else:
    print('wrong answer')
print('Congratulations.....Total score =',score)
total_score=score/3*100
print(total_score,'%')