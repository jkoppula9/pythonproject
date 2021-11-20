import sys
import datetime

if __name__ == '__main__':
    _input_file_name=sys.argv[1]

def gettimeparts(words):
    timeparts=[]
    for word in words:
        if word.lower().find('am')>-1:
            index=word.lower().find('am')
            if word[index-1].isdigit():
                timeparts.append(word)
        elif  word.lower().find('pm')>-1:
            index=word.lower().find('pm')
            if word[index-1].isdigit():
                timeparts.append(word)
    return timeparts


with open(_input_file_name,'r') as inputfile:
    totaltime=0
    currentline=0
    invalidline=[]
    for line in inputfile:
        currentline+=1
        parts=gettimeparts(line.split())
        if len(parts)>0:
            date_time_obj = datetime.datetime.strptime(parts[0], '%I:%M%p')
            date_time_obj1 = datetime.datetime.strptime(parts[1], '%I:%M%p')
            if date_time_obj1.hour<date_time_obj.hour:
                date_time_obj1+=datetime.timedelta(days=1)
            deltaval=date_time_obj1-date_time_obj
            currentval =-1
            if currentval<0:
                print(deltaval.total_seconds()/60)
                totaltime+=deltaval.total_seconds()/60
        elif currentline>1:
            invalidline.append(currentline)

    timeinhours=totaltime/60
    hours=int(timeinhours)
    minutes=(timeinhours*60) % 60
    print("line numbers without time part: ")
    print(invalidline)
    print("hours: "+str(hours)+" minutes: "+str(int(minutes)))



        


