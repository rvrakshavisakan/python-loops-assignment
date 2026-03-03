def process_scores(students):
    d={}
    for name in students:
        sum=0
        for i in students[name]:
            sum+=i
        avg=sum/5
        d[name]=avg
    return d

def classify_grades(averages):
    d={}
    for name in averages:
        if (averages[name]>=90):
            t=(averages[name],'A')
        elif (averages[name]>=75 and averages[name]<90):
            t=(averages[name],'B')
        elif (averages[name]>=60 and averages[name]<75):
            t=(averages[name],'C')
        else:
            t=(averages[name],'F')
        d[name]=t
    return d
        
def generate_report(classified, passing_avg=70):
    print("=====Student Grade Report====")
    c=0
    d=0
    for name in classified:
        if classified[name][0]>=passing_avg:
            print(f"{name}\Avg: {classified[name][0]:.2f} | Grade: {classified[name][1]} | Status: PASS")
            c=c+1
        else:
            print(f"{name}\Avg: {classified[name][0]:.2f} | Grade: {classified[name][1]} | Status: FAIL")
            d=d+1
    print("================================")
    print("Total Students :",len(classified))
    print("Passed         :",c)
    print("Failed         :",d)


students={}
n=int(input("Enter the no of elements in the dictionary:"))
for i in range(n):
    a=input("Enter the name of the student:")
    marks=[]
    for j in range(5):
        b=int(input("Enter the marks:"))
        marks.append(b)
    students[a]=marks
averages=process_scores(students)

classified=classify_grades(averages)
generate_report(classified, 60)