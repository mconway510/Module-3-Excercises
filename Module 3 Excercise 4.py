#Module 3 Excercise 4

#number of classes held:
total = int(input("How many clases are held : "))

#number of classes attended:
attended = int(input("How many classes have you attended : "));

#percentage of classes
percentage = ((attended/total)*100);

if percentage < 75:
    print("You can not take part in the exam");
else:
    print("You are free to take part in the exam");