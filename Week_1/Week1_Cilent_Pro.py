# Calculating Avrage Temperature in Celsius and Fahrenheit

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

# Display the highest, lowest and average temperature in celsius and fahrenheit.
print("\nStatistics")
print(f"Highest Temperature: {max(celsius_list)}°C ,{max(fahrenheit_list):.2f}°F")
print(f"Lowest Temperature: {min(celsius_list)}°C ,{min(fahrenheit_list):.2f}°F")
print(f"Average Temperature: {sum(celsius_list)/len(celsius_list):.2f}°C ,{sum(fahrenheit_list)/len(fahrenheit_list):.2f}°F")