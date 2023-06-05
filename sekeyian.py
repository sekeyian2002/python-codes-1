subject_1=int(input("enter subject 1 marks"))
subject_2=int(input("enter subject 2 marks"))
subject_3=int(input("enter subject 3 marks"))
subject_4=int(input("enter subject 4 marks"))
average=(subject_1+ subject_2+ subject_3+ subject_4)/4
print(average)
if average>70<=100:
    print("A")
elif average>=60<70:
    print("B")
elif average>=50<60:
    print("C")
elif average>=40<50:
    print("D")
elif average>=0<40:
    print("FAIL")
    
