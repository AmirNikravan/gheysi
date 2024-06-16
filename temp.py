output = [
    'temp=[27', '95', '13', '15', '12]',
    'press=[67', '25', '80', '58', '89]',
    'keys=[false', 'false', 'false', 'true', 'false]',
    'lamps=[true', 'true', 'false', 'true', 'true]',
    'rounds=[10', '98', '89', '29', '2]',
    'daste=[73', '43', '13', '99', '7]'
]

# Iterate through each item in the output
for i in range(30):
    # Remove single quotes between numbers
    print(output[i])
    output[i] = output[i].replace("\'", "d")

print(output)
