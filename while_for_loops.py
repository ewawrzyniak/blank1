#while loop = excute some code WHILE some condition remains true 
# while loops and for loops are forms of itteration, itteration is the form of process of epeating or looping through a set of steps or instructions to iterate the verb form of itteration, be careful of infinate loops, they will crash your program and you will have to reatart it. Infinate loops are loops that never end 

# name= input("Enter yout name")
# # if name ==' ':
# #     print('you did not enter yout name ')
# # else:
# #     print(f'Hello {name}')

# while name == '':
# #while is ismilar to if but it keeps happning 
#      print('you did not enter yout name ')
#      name = input ('Enter your name')
#      #if there was not a promp then it would be an "infinite loop"

# print (f'hello {name}')
# # its not tabbed so its putsid of the loop
# # opny happens after loop ends 

# age = int(input('enter your age'))

# while age <0:
#     print ('age cant be negative')
#     age = int(input('enter your age'))

# print(f'You are {age} years old ')

# food = input('enter a food you like (q to quit)')

# while not food == 'q' :
#     print(f'you like {food}')
#     food = input('enter a food you like (q to quit)')

# print ('bye')




####################################################################
# for loops = excute a block of code a fixed number of times. You can itterate over a range, string, sequence, etc. 

#if something is not eneraable, 

# for x in reversed(range(1, 11, 2)):
#     #fist one is start, seond one is end, third on is the skiupped 

#     #what ever you want to be exacuted, this is what you put here to be repeated 
#     print(x)

# # print ('HAPPY NEW YEAR')

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)

for x in range (1, 21):
    if x == 13 or x == 15 or x ==19:
        # continue #skips and continue
        break #ends program
    else:
        print(x)

horrorMovies = ['the excorcist', 'the shining', 'the conjouring', 'the ring']
#loop through the list of hooro movies 
#if the name is 'the signing', print 'the signing". otherwise, print "the signing is not found' and prin t" out yhr pothetr mnames using a link 

for movies in horrorMovies:
    if movies == 'the shining':
        print("the shining is found ")
        print(movies)
    else:
        print("the shining is not found ")
        print(movies)

#challange 2 
#create a list of your favorite horror movie directors. Loop through the list of characters. If the name 'freddy Kruger" is used, skip over it. otherwise, print out the name of the character 
        
horrorCharacters = ['freddy kruger', 'meg3n', 'pennywise']

for character in horrorCharacters:
    if character== 'freddy kruger':
        continue

#challange 3 
#create a list of your favorite horror movie monsters. Loopp through the list . 
# if th nam ei , for example, 'swamp things', replace it with a diffrent name 
horrorMonster = ['swamp monster', 'air monster', 'water monster', 'ghost thing']

for monster in horrorMonster:
    if monster== 'swamp monster':
        newMonster= input("Input a new monster")
        
    else:
        print (monster)