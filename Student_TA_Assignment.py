######################################################################################
##Create a random/Shuffle list of students assigned to Teacher assistant for grading##
######################################################################################

import random
import pandas as pd
import sys
import os

desktop = "'"+ os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')+"'"
#desktop
#desktop.replace("\\", '\'')

Students  = ['Archana Rajagopalan','Chandler Parrott','Chrison Mills','Clinton Waters','Daniel Jo',
'Elena Katicheva','Erika DeLeon','Felix Ochieng','Harold Flack','Jorge Torres','Joseph Bero','Joseph Orona','Joseph Rafferty','Kahsay Gebreyowhance','Karl Parvez','Kolanjiappan Kaliyaperumal','Monica Topicz','Nell Meier',
'Nicole Nanton','Radhakishore Donthi','Shaquille Woods','Sneha Reddy','Zack Capets']

#Student list container
Studentx =[]

#Sort list of Students and random order
for Student in sorted(Students,key=lambda _: random.random()):
    Studentx.append(Student)
FullStudentList = pd.DataFrame(Studentx)
FullStudentList.columns=['StudentName']

#Build list of Teaching Assistants 
TAs = pd.DataFrame(['Camir','Brian','Amanda'])
TAs.columns =['Teaching Assistant']

#Repeat TA List to match Each Student
ta =pd.concat([TAs]*round(len(Students)/len(TAs)),0)

#Join Rotating student list to the TA's
HomeworkAssignment = pd.concat([FullStudentList.reset_index(drop=True),ta.reset_index(drop=True)],axis=1)
HomeworkAssignment = HomeworkAssignment.dropna(axis=0)
#HomeworkAssignment
#filename = '\tafile.xls'
export_excel = HomeworkAssignment.to_excel(r'C:\Users\Camir Inshiqaq\Desktop\tafile.xlsx', index = None, header=True)

#desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

#Print Output
#Grouped = HomeworkAssignment.dropna(axis=0)
# .groupby('Teaching Assistant')[Students].apply(HomeworkAssignment)
#df.groupby('a')['b'].apply(list)
#print(sys.path)

print(export_excel)
