# # # # # # # number = int(input('enter the number'))	
# # # # # # # i = 1
	
# # # # # # # while i<11:
# # # # # # # 	print(number,'*',i,'=',number * i)
# # # # # # # i += 1
# # # # # # for i in range(1,11):
# # # # # #     print("fawad zeran")
  
# # # # # for i in range(1,10):
# # # # #      print ('*')
# # # # #      i +=j
# # # # # for j in range(j,i):
# # # # #      j +=i
# # # # #      print('')
      
# # # # import random
# # # # jackpot = random.randint(1,100)

# # # # guess = int(input('guess karo'))
# # # # counter = 1
# # # # while guess != jackpot:
# # # #   if guess < jackpot:
# # # #     print('galat!guess higher')
# # # #   else:
# # # #     print('galat!guess lower')

# # # #   guess = int(input('guess karo'))
# # # #   counter += 1

# # # # else:
# # # #   print('correct guess')
# # # #   print('attempts',counter)

# # # menu = input(
# # #     """
# # # Hi how can i help you?
# # # 1. Press 1 for Balnce check.
# # # 2.Press 2 for code chanege.
# # # 3.Press 3 for pin change.
# # # 4.Press 4 money check.
# # # """
# # # )
# # # if menu=='1':
# # #     print('Change your Pin')
# # # elif menu=='2':
# # #     print('Update your code')
# # #     print ('you can enter you')
# # # elif menu=='3':
# # #     print('change your pin code')
# # # elif menu=='4':
# # #     print('check your mone ')

# # # # menu = input("""
# # # # Hi! how can I help you.
# # # # 1. Enter 1 for pin change
# # # # 2. Enter 2 for balance check
# # # # 3. Enter 3 for withdrawl
# # # # 4. Enter 4 for exit
# # # # """)

# # # # if menu == '1':
# # # #   print('pin change')
# # # # elif menu == '2':
# # # #   print('balance')
# # # # else:
# # # #   print(
# #   password 
# # password = input (
# #     """
# # 1. change password.
# # 2.remove password.
# # """
# # )
# # if password=='1':
# #     print('change password ')
# #     if password=='12345':
# #         print("enter new password")
# # else:
# #     print('remove password')'
 

# # rows= int (input("enter the nio of rows"))
# # for i in range (1,rows+1):
# #     for j in range (1,i+1):
# #         print ('*', end ='')
# #     print()

# rows= int (input("enter the nio of rows"))
# for i in range (1,rows+1):
#     for j in range (1,i+1):
#         print (j, end ='')
#         for k in range(i-1,0,-1):
#          print(k,end='')

#         print()

lower= int(input("enter the lower no "))
upper= int(input("enter the upper no "))
for i in range(lower,upper+1):
    for j in range(2,i):
        if i%j== 0:
            break
        else:
            print(i)
  


