import random
import json

def generate_random_values(val):
	#[115, 137, 117, 78, 90, 180, 97, 142, 147, 95, 33, 132, 
	# 6, 165, 179, 59, 14, 104, 179, 59, 114, 158, 67, 70, 173 ...]
	list = []
	for i in range(val):
		random_value = random.randint(0,231)
		list.append(random_value)
	return list

def get_values_between(scores, minVal, maxValue):
	#Returns a list of the values in scores between given min and max
	values = []
	for e in scores:
		if e >= minVal and e <= maxValue:
			values.append(e)
	return values

def get_summary(scores, dict_length):
	num_elements = len(scores)

	#Start the loop with only one block, min and max
	mini = min(scores)
	maxi = max(scores)
	dictionary = {}
	add_block(dictionary, get_values_between(scores, mini, maxi))
	allDone = False

	while not allDone and len(dictionary) < dict_length and len(dictionary) != num_elements:		
		
		dict_sorted = sorted(dictionary, key=dictionary.get, reverse=True)
		i = 0

		for key in dict_sorted:
			i+=1
			atts = key.split("-")
			mini = int(atts[0])
			maxi = int(atts[1])
			margin = maxi - mini

			#If there is enough margin to make the division...
			if margin >= 1:
				medium = mini + int(margin / 2)

				#Deletes old key and sets two new blocks
				del dictionary[key]
				add_block(dictionary, get_values_between(scores, mini, medium))
				add_block(dictionary, get_values_between(scores, medium+1, maxi))

				#Break the for loop to reorder the dictionary
				break
			
			if len(dict_sorted) == i:
				#All keys of the dictionary are indivisible
				allDone = True

	return dictionary

def add_block(dictionary, values):
	#Adds a block to the dictionary. Ex: "190-200":50
	key = str(min(values)) + "-" + str(max(values))
	dictionary[key] = len(values)

def main():
	response_max_length = 20
	num_elements = 200

	values = generate_random_values(num_elements)
	summary = get_summary(values, response_max_length)
	
	json_response = json.dumps(summary, indent = 4)   
	print(json_response) 
	print("Verification:", sum(summary.values())==num_elements)

main()