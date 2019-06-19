#excercise 1 
def times_table(x, y = 10):
    appender = []
    for i in range(y+1):
        if i == 0:
            pass
        else:
            appender.append(i*x)

    return appender


#excercise 2
def times_tables(x, y = 10):
    empty_dict = dict()
    c = 1
    for index in range(x):
        empty_dict[c] = times_table(c)
        c+=1
    return empty_dict

#excercise 3

x = int(input('Enter x'))
y = int(input('Enter y'))

timetable = dict(times_tables(x,y))
timetablevals = timetable.values()
fileout = open('times_tables.txt','w')
print(timetable)
make_a_list = []
for index in timetable.values():
    make_a_list.append(index)
print(make_a_list)
for key,val in timetable.items():
    fileout.write(str(val))
    fileout.write('\n')
fileout.close()




