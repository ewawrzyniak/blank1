##Yao and Emily W 


#question 3

member = input( 'Are you a premium member? Yes or No:') #Asks if they are members or not 
cart = int(input('What is your total cart value?:')) #What is their total cart value and converted into int

if member == "Yes" or member == "yes": # If they are members = True but if not, equals to False 
    member = True 
else: 
    member = False
    
if member == True: # here checks if they are members and see what is there deserved discount based on their value. 
    if cart >= 100:
        discount = cart * 0.2
    elif cart >= 50 and cart < 100:
        discount = cart * 0.1 
    elif cart < 50: 
        print('No dicount for cart value below $50.')

if member == False:
# here checks if they are not members and see what is there deserved discount based on their value.
    if cart >= 100:
        discount = cart * 0.1
    elif cart >= 50 and cart < 100:
        print('No discount for non-premium member with cart value below $100')
    
finalPrice = cart - discount
print('$' + (str(finalPrice)))
    


#question 9 
years= int(input("How many years have you been working?"))
# years is for how long somoen has been working 
position = input("Are you Manager or Staff?")
if position == ('Manager') or ('manager'):
    position = True
else:
    position = False
    #the if statement tomake a boolean is so that it is easier to see true vs falsehere insted of in the code and having a bunch of variations. All the booleans assignemnts are heere. 
warnings = input('Do you have any warnings? (Y or N)')
if warnings == ('Y') or ('y'):
    warnings = True
else: 
    warnings = False
#Same reason for boolean here, its so that there arnt so many variations in te main section of the text 
    
if position == True:
        if years >= 5:
        #you create a nestloed 'if' here because you need 2 outcomes if greater or less then 5 years. 
            if warnings == False:
            #you need anohter if statment here because these only apply if yoiu have been working for over 5 years, so you are only using this conditional if the other ones are met. 
                print('Bonus of $1000')
            else:
                print('Bonus of $700')
        else:
        #The paper didnt say what to do if there was less then 5 years, so I had to improvise. 
            print('You havent been working here long enough as a manager')
else:
    if years >= 3 and warnings == ('N'):
    #this only needs one 'if' statment because the warnings only matte rif you also have 3 years of experience, so insted of leading to the samre thing twice, you can just use 'and'
        print('Bonus of $500')
    else:
        print("Bonus of $300")