def get_letter_grade():
    letter_grade = int(input('Enter a number score grade: '))
    if letter_grade >= 90:
        # print('Your letter grade is: A')
        return 'Your grade is A'
    elif letter_grade >= 80:
         return 'Your letter grade is: B'
    elif letter_grade >= 70:
         return 'Your letter grade is: C'
    elif letter_grade >= 60:
         return 'Your letter grade is: D'
    else:
        return 'Your letter grade is: F'
    
    import json
    profiles = json.load(open('profiles.json'))