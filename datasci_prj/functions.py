def get_time_from_dt_list(dt_list):
    time_list = []
    for k in range(len(dt_list)):
        time_list.append(dt_list[k].time())
    return time_list
