import random
import array

Digits = ['1','2','3','4','5','6','7','8','9','0']
Letter_LOW = ['a','b','c','d','e','f','g','h','j','k','l''m','n','o','p''q','r','s','t','u','v','w','x','y','z']
Spc = ['!','@','#','$','%','^','&','*','(',')','?','/','_']
Letter_UPP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
COMBINED = Digits + Letter_UPP + Spc + Letter_LOW
# print(COMBINED)
# len_pass = int(input("Length of your password: "))
len_pass =12
ran_digit = random.choice(Digits)
ran_upp = random.choice(Letter_UPP)
ran_low = random.choice(Letter_LOW)
ran_spc = random.choice(Spc)

temp = ran_digit + ran_low +ran_spc + ran_upp

# print(temp)

for i in range(len_pass - 4):
    temp = temp + random.choice(COMBINED)


    temp_pass_list = array.array('u', temp)
    random.shuffle(temp_pass_list)

password = ""
for i in temp_pass_list:
    password = password + i

print(password)