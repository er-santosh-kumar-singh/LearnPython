#if else conditions

def printGrade(marks):
    if(marks >= 90 and marks <= 100):
        print('Congratulation! Your EXCELLENT student','Your score is',marks)

    elif (marks >= 80 and marks <= 89):
        print('Congratulation! Your SUPPER student', 'Your score is', marks)

    elif (marks >= 60 and marks <= 79):
        print('Congratulation! Your GREAT student', 'Your score is', marks)

    elif (marks >= 50 and marks <= 59):
        print('Congratulation! Your PASSED student', 'Your score is', marks)

    else:
        print('Bad! Your are FAILED. You need to do hard work', 'Your score is', marks)
