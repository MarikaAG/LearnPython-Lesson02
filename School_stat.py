#Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
#Посчитать и вывести средний балл по всей школе.
#Посчитать и вывести средний балл по каждому классу.

SCHOOL_LOG=[{'school_class':'4a', 'scores':[3,4,4,5,2]},
            {'school_class':'4b', 'scores':[2,5,4,3,3,5]},
            {'school_class':'5a', 'scores':[1,3,5,5,4,4,2]}]


#MAIN
sum_school=0 #sum of scores for the whole school
num_school=0 #sum of students for the whole school

for sch_class in SCHOOL_LOG: #FOR for all dicts in SCHOOL_LOG - for each class
    sum_class=0 #sum of scores for one class
    num_class=0 #sum of students in one class
    for score in sch_class['scores']: #FOR for scores of one class
        sum_class+=score
        num_class+=1
        sum_school+=score
        num_school+=1
    avg_class=sum_class/num_class
    #print(sch_class['school_class'])
    #fortest= sch_class['school_class']
    #print(f'School_class {fortest}:')  
    print(f'School_class {sch_class["school_class"]} \nSum of scores: {sum_class}, Num of students: {num_class}. Average: {avg_class}')

avg_school=sum_school/num_school
print(f'The school: \nSum of scores: {sum_school}, Num of students: {num_school}. Average: {avg_school}.')
