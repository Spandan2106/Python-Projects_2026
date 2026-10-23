#Make use of Python program that creates two Dictionaries, One that stores conversion valuefrom meter to centimeter and Second stores conversion value from centimeter to meter.
meter_to_centimeter = {i: i * 100 for i in range(1, 11)}
centimeter_to_meter = {i: i / 100 for i in range(100, 1100, 100)}
print("Meter to Centimeter Conversion Dictionary:", meter_to_centimeter)
print("Centimeter to Meter Conversion Dictionary:", centimeter_to_meter)