input_file = "input.txt"
output_file = "output.txt"

with open(input_file, 'r') as file:
    lines = file.read().splitlines()

with open(output_file, 'w') as file:
    for line in reversed(lines):
        file.write(line + '\n')

print("File reversed successfully.")
