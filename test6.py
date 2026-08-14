# WAP to help an employee to complete maximum number of tasks based on start and end time
# Activity selection problem
'''
---------------------------------------
| tasks | A1 | A2 | A3 | A4 | A5 | A6 |
---------------------------------------
| start | 0  | 3  | 1  | 5  | 5  | 8  |
---------------------------------------
| end   | 6  | 4  | 2  | 8  | 7  | 9  |
---------------------------------------

'''
def activity_selection(activities):
    # print(activities)
    # print()
    activities.sort(key = lambda x:x[2])
    # print(activities)

    # actual code
    selected_activities = [activities[0]]

    last_end_time = activities[0][2]

    for i in range(1, len(activities)):
        current_start_time = activities[i][1]

        if current_start_time >= last_end_time:
            selected_activities.append(activities[i])
            last_end_time = activities[i][2]
    return selected_activities

    # i = 0
    # print(activities[i][0], end=" ")
    # for j in range(len(activities)):
    #     if activities[j][1] > activities[i][2]:
    #         print(activities[j][0], end=" ")
    #         i = j


activities = [
    ['A1', 0, 6],
    ['A2', 3, 4],
    ['A3', 1, 2],
    ['A4', 5, 8],
    ['A5', 5, 7],
    ['A6', 8, 9]
]

result = activity_selection(activities)
print("Maximum set of activities :", result)