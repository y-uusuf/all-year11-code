def convert(x):
    try:
        char = chr(x)
        return char
    except ValueError:
        return "Invalid ASCII value."

# Example usage
value = int(input("Enter ASCII value: "))

print(f"ASCII Value: {value} | Conversion: {convert(value)}")
