sequence = input()
longest = 0
current_length = 0
active_letter = ''
for letter in sequence:
    if (letter != active_letter):
        active_letter = letter
        current_length = 1
    else:
        current_length += 1
    if (current_length > longest):
        longest = current_length
print(longest)
