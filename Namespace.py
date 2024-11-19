calls = 0

def count_calls():
   global calls
   calls = calls + 1

def string_info(string):
   omg = (len(string), string.lower(), string.upper())
   count_calls()
   return omg

def is_contains(calls, string):
   checker = 0
   for n in string:
      if calls == string[0:]:
         checker = checker + 1
   if checker > 0:
      truth = True
   else:
      truth = False
   count_calls()
   return truth



print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)