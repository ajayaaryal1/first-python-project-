print("Celsius Fahrenheit")
print("------------------")


for celsius in range(21):
    fahrenheit = (celsius * 9/5) + 32
    fahrenheit_rounded = round(fahrenheit)
    print(f"{celsius:7} {fahrenheit_rounded:10}")