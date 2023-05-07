def add_time(time:str, forward:str, day=None):
    days_to_num = {
        'saturday' : 1,
        'sunday' : 2,
        'monday' : 3,
        'tuesday' : 4,
        'wednesday' : 5,
        'thursday' : 6,
        'friday' : 0,
    }
    num_to_days ={
        1: 'Saturday',
        2: 'Sunday',
        3: 'Monday',
        4: 'Tuesday',
        5: 'Wednesday',
        6: 'Thursday',
        0: "Friday",
    }
    
#####################################################
    # time split
    time_dn =  time.split()
    time_split = time_dn[0].split(":")
    hour = int(time_split[0])
    minutes = int(time_split[1])
#####################################################
    # forward split
    forward_split = forward.split(":")
    fhour = int(forward_split[0])
    fminutes = int(forward_split[1])
    
    hours = sum([hour, fhour])
    mins = sum([minutes, fminutes])
    
    mins_hour, mins_min = mins // 60, mins % 60
    hours += mins_hour
    hours_12, hours_remainder = hours // 12, hours % 12
    
    timer_np = f"{str(hours_remainder).zfill(2)}:{str(mins_min).zfill(2)}"
    if hours_12 % 2 == 0:
        if time_dn[1] == "PM":
            timer_np += " PM"
        else:
            timer_np += " AM"
    else:
        if time_dn[1] == "PM":
            timer_np += " AM"
        else:
            timer_np += " PM"

    days_num = hours_12 // 2
    if hours >= 12 and time_dn[1] == "PM":
        days_num += 1
    if day is not None:
        dnum = days_to_num.get(day.lower())
        dnum += days_num
        timer_np += f", {num_to_days.get(dnum % 7)}"
        
    additional = ''
    if days_num == 0:
        pass
    elif days_num == 1:
        additional += " (next day)"
    else:
        additional += f" ({days_num} days later)"
    
    timer_np += additional
    if timer_np.startswith('00'):
        timer_np = timer_np.replace("00", "12", 1)
    return timer_np
    
    
if __name__ == "__main__":
    print(add_time("11:59 PM", "24:05", "Wednesday"))
    