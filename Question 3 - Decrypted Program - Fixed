global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# process_numbers was not set up to accept "numbers" as an argument. Modifying it to process_numbers(numbers) makes it do so.
#global global_variable was removed from this block because it is not used in this function, and is therefore pointless to include.
# "numbers=my_set" didn't work because "numbers" had a hard-coded value (list) local to process_numbers()'s code block,
#which overrided numbers=my_set. given that the function is obviously intended to process my_set, it seemed best to remove that list.
def process_numbers(numbers):
	local_variable = 5

	while local_variable > 0:
		if local_variable % 2 == 0:
			numbers.remove(local_variable)
		local_variable -= 1

	return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

def modify_dict():
	local_variable = 10
	my_dict['key4'] = local_variable
# modify_dict(5) was changed to modify_dict() because it does not accept with integers as a parameter. It's unclear what modify_dict(5)
#was trying to do, so it seemed best to get rid of the impeding integer.
# key4 was renamed to key1 for legibility because keys 1-3 were removed.
modify_dict()

def update_global():
	global global_variable
	global_variable += 10
#The update_global() function was defined but never called. Calling it fixes that.
update_global()

# i += 1 was not doing anything in this function because it was placed after print(i). Moving it higher up in the code block
#causes it to modify i prior to output. Alternatively I could have just removed it so that the program would print
#"0 1 2 3 4 5 not found in the dictionary!" which looks neater, however, seeing as the program has only a demonstrative function,
#which is not impeded by either change, I figured that either option would be fine.
for i in range(5):
	i += 1
	print(i)

print(my_dict)
# Moved the below two lines underneath print(my_dict) to improve output legibility.
# I could have changed other parts of the program to get them to modify the other keys given that they currently output
# 'value1' etc, but it doesn't seem like other parts of the program are intended to provide new values for dictionary keys.
if my_set is not None and my_dict['key4'] == 10:
	print("5 not found in the dictionary!")
print(my_set)
#The update_global() function produced no output, so I made it print its results at the end.
print(global_variable)
