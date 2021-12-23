import pandas as pd

df = pd.read_csv('data/enrolment_2.csv')

course = df['course name'].value_counts()
Auditorium = list(course[course >= 80].index)
Large_room = list(course[(course < 80) & (course >= 40)].index)
Medium_room = list(course[(course < 40) & (course >= 15)].index)
Small_room = list(course[(course < 15) & (course >= 5)].index)

for course in Auditorium:
    df.loc[df['course name'] == course, 'room assignment'] = "Auditorium"

for course in Large_room:
    df.loc[df['course name'] == course, 'room assignment'] = "Large room"

for course in Medium_room:
    df.loc[df['course name'] == course, 'room assignment'] = "Medium room"
    
for course in Small_room:
    df.loc[df['course name'] == course, 'room assignment'] = "Small room"

df.loc[df["status"] == "not allowed", "room assignment"] = "not assigned"
# 정답 출력
df