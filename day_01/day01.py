input_file = "../input/input.txt"

freq =0
with open(input_file) as f_input:
	for data in f_input.read().strip().splitlines():
		freq += int(data)
print(freq)

