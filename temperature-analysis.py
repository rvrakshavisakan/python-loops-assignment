# Name: Raksha Visakan R V
# Roll Number: IITP_AIMLTN_2602276
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
small=temperatures[0]
large=temperatures[0]
for i in temperatures:
    if i>large:
        large=i
    if i<small:
        small=i
print("Highest Temperature=",small)
print("Lowest Temperature=",large)


print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
c=0
for i in temperatures:
    if i>30:
        c+=1
print("Hot Days (>30°C):",c)


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
d=0
for i in range(len(temperatures)):
    if temperatures[i]>=40:
        a=i+1
        break
    if temperatures[i]>30:
        d+=1
    
print("Hot Days before alert:",d)
print("Alert! Extreme temperature 40°C detected on Day",a)