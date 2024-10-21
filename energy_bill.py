previous_meter_reading = int(input("Enter the previous meter reading: "))
current_meter_reading = int(input("Enter the current meter reading rounded down: "))
calorific_value = 39.3

units_used  = current_meter_reading - previous_meter_reading

kwh = units_used * 1.022 * (calorific_value / 3.6)

cost = (0.0284 * kwh)

print(cost)