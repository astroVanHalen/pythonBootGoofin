###############################################################################
### Lab 8, IT- Scripting
### Zac Huron
### 2023_03_11
### Description:This script takes a users radio call sign and returns
###             the state in which the call sign was issued and the
###             license class.
### 
###############################################################################

def get_state_code(radio_sign):
   '''
   This function looks through the call sign for any character that can be converted to an integer.
   This will tell us the state code identifier.
   '''
   try:
      for i in radio_sign:
          isInt = True
          try:
             state_code = int(i)
          except ValueError:
             pass
      return state_code
   except:
      print('Invalid call sign.  Try again.')
      exit()


def get_state(state_code):
   '''
   This function creates a dictionary with region codes as keys and states as values.
   The state code is passed in and checked against the keys and returns the value.
   '''
   state_dict = {
   '1': ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont'],
   '2': ['New Jersey', 'New York'],
   '3': ['Delaware', 'District of Columbia', 'Maryland', 'Pennsylvania'],
   '4': ['Alabama', 'Florida', 'Georgia', 'Kentucky', 'North Carolina', 'South Carolina', 'Tennessee', 'Virginia'],
   '5': ['Arkansas', 'Louisiana', 'Mississippi', 'New Mexico', 'Oklahoma', 'Texas'],
   '6': ['California'],
   '7': ['Arizona', 'Idaho', 'Montana', 'Nevada', 'Oregon', 'Utah', 'Washington', 'Wyoming'],
   '8': ['Michigan', 'Ohio', 'West Virginia'],
   '9': ['Illinois', 'Indiana', 'Wisconsin'],
   '0': ['Colorado', 'Iowa', 'Kansas', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'South Dakota'],
   }
   for k, v in state_dict.items():
      if k == state_code:
         state = v
      else:
         pass
   return state


def get_license(radio_sign, state_code):
   '''
   This function checks the index of the state code within the radio sign.
   This gives us an index to use when slicing the list into a prefix and suffix.
   Then, by checking the length of the prefix and suffix, and the letter combinations,
   a license class is determined.
   '''
   
   slice_index = radio_sign.index(state_code)                                             # these three variables slice the call sign
   prefix = radio_sign[:slice_index]                                                      # into state code, prefix and suffix
   suffix = radio_sign[(slice_index + 1):]                                                # 


   if len(prefix) == 2 and len(suffix) == 3:
      if prefix[0] == 'k' or prefix[0] == 'w':
         radio_class = "Novice, Club and Military Recreations Station"
      else:
         print('\nInvalid call sign.  Try again.')
         exit()

   elif len(prefix) == 1 and len(suffix) == 3:
      if prefix[0] == 'k' or prefix[0] == 'n' or prefix[0] == 'w':
         radio_class = "General, Technician, and Technician Plus Classes"
      else:
         print('\nInvalid call sign.  Try again.')
         exit()


   elif len(prefix) == 2 and len(suffix) == 2:
      if prefix[0] == "a":
         radio_class = "Amateur Extra Class"
      else:
         if prefix[0] == 'a' or prefix[0] == 'k' or prefix[0] == 'n' or prefix[0] == 'w':   #  This whole section of if elif else statements
            radio_class = "Advanced Class"                                                  #  uses conditional statements based off of the
         else:                                                                              #  fcc website to determine which license
            print('\nInvalid call sign.  Try again.')                                       #  was ordered.  The rules are based from
            exit()                                                                          #  prefix and suffix length, and also what the
                                                                                            #  first letter of the call sign is.
   elif len(prefix) == 2 and len(suffix) == 1:                                              #
         if prefix[0] == 'a' or prefix[0] == 'n' or prefix[0] == 'k' or prefix[0] == 'w':   #   
            radio_class = "Amateur Extra Class"
         else:
            print('\nInvalid call sign.  Try again.')
            exit()

   elif len(prefix) == 1 and len(suffix) == 2:
         if prefix[0] == 'n' or prefix[0] == 'k' or prefix[0] == 'w':
            radio_class = "Amateur Extra Class"
         else:
            print('\nInvalid call sign.  Try again.')
            exit()

   else:
            print('\nInvalid call sign.  Try again.')
            exit()
            
   return radio_class


######################################################################################
# This next section declares variables and calls the functions.
######################################################################################
user_radio = input('\nEnter your call sign: ')
user_radio = user_radio.lower()
radio_sign = list(user_radio)
state_code = str(get_state_code(radio_sign))
state_list = get_state(state_code)
state =  ', '.join(state_list)
radio_class = get_license(radio_sign, state_code)

print(f'\nLicense Class: {radio_class} \nState(s) Issued: {state}')
######################################################################################