###############################################################################
### Lab 8, IT- Scripting
### Zac Huron
### 2023_03_11
### Description:This script takes a users radio call sign and returns
###             the state in which the call sign was issued and the
###             license class.
### 
###############################################################################

state_names = ["Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", 
               "District of Columbia", "Delaware", "Florida", "Georgia", "Iowa", "Idaho", 
               "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", 
               "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", 
               "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", 
               "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", 
               "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", 
               "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", 
               "West Virginia", "Wyoming"]


######################################################################################
user_radio = input('\nEnter your call sign: ')
radio_sign = list(user_radio)
print(radio_sign)
radio_sign2 = []
sign_index = 0
slice_index = 0
radio_class = '0'

for i in radio_sign:
    isInt = True
    try:
       int(i)
    except ValueError:
       isInt = False

    if isInt:
       x = int(i)
       radio_sign2.append(x)
    else:
       radio_sign2.append(i)

for i in radio_sign2:
   if type(i) is int:
      state_code = i
   else:
      pass
   
element = state_code
slice_index = radio_sign2.index(element)

print(radio_sign2)
print(state_code)
print(slice_index)

prefix = radio_sign2[:slice_index]
suffix = radio_sign2[(slice_index + 1):]

print(prefix)
print(suffix)
######################################################################################

######################################################################################
if len(prefix) == 2 and len(suffix) == 3:
   radio_class = "Group D"

elif len(prefix) == 1 and len(suffix) == 3:
   radio_class = "Group C"

else:
   len(prefix) == 2 and len(suffix) == 2
   if prefix[0] == "A":
      radio_class = "Group A"
   else:
      radio_class = "Group B"
   
print(radio_class)
######################################################################################