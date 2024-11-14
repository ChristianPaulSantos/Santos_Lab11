loop = True
grades = []
entered_grade = 0
subjects = 0

while loop == True:
    input_grade = input("Enter grade: ")
    if(input_grade.isdigit()):
        input_grade = int(input_grade)
        if(input_grade >= 40 and input_grade <= 100):
          entered_grade += 1
          grades.append(input_grade)
        else:  
          print("Invalid grade, Please try again")    
          break
    elif(input_grade == str("done".lower())):
       loop = False
    else:
       print("Invalid input, Please try again.")    
       break      
else:
  sum =sum(grades)
  total = sum/entered_grade
  print("Average Grade: ", total)
  for input_grade in grades:
    if(input_grade >= 75):
      subjects += 1
       
  print("Passed Subjects: ", subjects)
  print("Passing percentage: ", (subjects/len(grades))* 100, "%")
  print("Grades: ", grades)
     
    