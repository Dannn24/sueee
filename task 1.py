user = int(input("Enter a grades : "))


def grade(grades):
    if grade >= 90 and grade <= 100:
        return("Exellent!you did a great job! ")
    elif grade >= 80 and grade <= 89:
        return("Good job!,Keep it up!")
    elif grade >= 70 and grade <= 79:
       return("You passed, but there's room for improvements. ")
    elif grade <= 69:
        return("You failed. Better luck next time ")
        
    else:
        return("invalid input")
        
     
    user = int(input("Enter a grades : "))
    print(check_grade(user))