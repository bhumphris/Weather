monthly_average_temp = {'Jan': 54, 'Feb': 57, 'Mar': 61, 'Apr': 68, 'May': 77, 'Jun': 86, 'Jul': 91, 'Aug': 90, 'Sep': 84, 'Oct': 73, 'Nov': 61, 'Dec': 54}
vals = monthly_average_temp.values()
top_range = 91
high = dict()
def avg_temp(year):
    total = 0
    for temp in year:
        total += year[temp]
    avg = total / len(monthly_average_temp)
    print("The average temperature in Phoenix is " + str(avg))

def over(today):
    global top_range
    for temp in today:
        if today[temp] > top_range:
            high[temp] = (today[temp])
    print high

avg_temp(monthly_average_temp)
over(monthly_average_temp)
