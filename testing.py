#question 9 
years= int(input("How many years have you been working?"))
position = input("Are you Manager or Staff?")
if position == ('Manager') or ('manager'):
    position = True
else:
    position = False
warnings = input('Do you have any warnings? (Y or N)')
if warnings == ('Y') or ('y'):
    warnings = True
else: 
    warnings = False

if position == True:
        if years >= 5:
            if warnings == False:
             print('Bonus of $1000')
            else:
                print('Bonus of $700')
        else:
            print('You havent been working here long enough as a manager')
else:
    if years >= 3 and warnings == ('N'):
        print('Bonus of $500')
    else:
        print("Bonus of $300")