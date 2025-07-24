hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

dura_hours = dura//60
dura_minutes = dura%60
hour +=dura_hours
mins +=dura_minutes
print("ending time is : ",str(hour%24 + mins//60)+":"+str( mins%60))

