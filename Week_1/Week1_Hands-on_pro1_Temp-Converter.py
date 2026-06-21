# Temperature Converter: Celsius to Fahrenheit

# Take input in celsius from the user
n = int(input("How many temperatures? : "))
celsius_list = []
for i in range(n):
    temp = float(input(f"Enter temperature {i+1}: "))
    celsius_list.append(temp)

# convert celsius to fahrenheit
fahrenheit_list = []
for c in celsius_list:
    fahrenheit_list.append((c * 9/5) + 32)

# Print the all temperatures in celsius and fahrenheit as report.
print("\nTemperature Report")
print("-" * 30)
for c, f in zip(celsius_list, fahrenheit_list):
    print(c,"°C","->",f,"°F")