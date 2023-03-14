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
   for i in radio_sign:
       isInt = True
       try:
          state_code = int(i)
       except ValueError:
          pass
   return state_code


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
   slice_index = radio_sign.index(state_code)
   prefix = radio_sign[:slice_index]
   suffix = radio_sign[(slice_index + 1):]
   if len(prefix) == 2 and len(suffix) == 3:
      radio_class = "Group D"

   elif len(prefix) == 1 and len(suffix) == 3:
      radio_class = "Group C"

   elif len(prefix) == 2 and len(suffix) == 2:
      if prefix[0] == "A":
         radio_class = "Group A"
      else:
         radio_class = "Group B"
   else:
         radio_class = "Group A"
   return radio_class



user_radio = input('\nEnter your call sign: ')
radio_sign = list(user_radio)
state_code = str(get_state_code(radio_sign))
state_list = get_state(state_code)
state =  ', '.join(state_list)
radio_class = get_license(radio_sign, state_code)

print(f'\nLicense Class: {radio_class}\nState(s) Issued: {state}')
######################################################################################