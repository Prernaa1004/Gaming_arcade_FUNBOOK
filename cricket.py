##import random
####import time 
####
####
####def countdown(t): 
####    
####    while t: 
####        mins, secs = divmod(t, 60) 
####        timer = '\n{:02d}'.format(secs) 
####        print(timer, end="\r") 
####        time.sleep(1) 
####        t -= 1
####      
####    print('TIME UP!') 
####t=30  
####countdown(int(t))
##
##i=1
##while i<=6:
##    elements=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P',
##              'S','Cl','Ar','K','Ca','Sc','V','Ti','Cr','Mn','Fe','Co','Ni','Cu','Zn']
##    options=random.randint(1,31)
##    main=elements[options]
##
##    answers=['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen','fluorine','neon',
##             'sodium','magnesium','aluminium','silicon','phosphorous','sulphur','chlorine','argon','potassium','calcium',
##             'scandium','titanium','vanadium','chromium','manganese','iron','cobalt','nickel','copper','zinc']
##    main_ans=answers[options]
##    print("The element's symbhol is:",main)
##
##    user1=input('The name of the element is:')
##    
##    if user1==main_ans:
##        print('correct')
##    else:
##        print('wrong')
##
##    i=i+1







import random
import threading
import time
import sys
final=0
i=1
while i<2:
    elements=['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P',
              'S','Cl','Ar','K','Ca','Sc','V','Ti','Cr','Mn','Fe','Co','Ni','Cu','Zn']
    options=random.randint(1,31)
    main=elements[options]

    answers=['hydrogen','helium','lithium','beryllium','boron','carbon','nitrogen','oxygen','fluorine','neon',
             'sodium','magnesium','aluminium','silicon','phosphorous','sulphur','chlorine','argon','potassium','calcium',
             'scandium','titanium','vanadium','chromium','manganese','iron','cobalt','nickel','copper','zinc']
    main_ans=answers[options]
    print("The element's symbhol is:",main)

    user1=input('The name of the element is:')
    
    if user1==main_ans:
        print('correct')
    else:
        print('wrong')

    i=i+1

# make this work with Python2 or Python3
if sys.version_info[0] < 3:
    input = raw_input


class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval=0.001):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False

    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.interval

    def peek(self):
        '''
        return the current value
        '''
        return self.value

    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value


# create the class instance
count = SecondCounter()

# start the count
count.start()

# test the counter with a key board response time
# or put your own code you want to background-time in here
# you can always peek at the current counter value
print("Press Enter")
user1=input('The name of the element is:')#e = input("Press Enter again")

# stop the count and get elapsed time
seconds = round((count.finish()*10),2)
if seconds<=5:
    final=final+6
elif seconds>5 and seconds<=10:
    final=final+4
elif seconds>10 and seconds<20:
    final=final+1
else:
    final=final+0


print("You took {} seconds between Enter actions".format(seconds))

print('your total socre in one over is:',final,'runs')
