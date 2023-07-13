import statistics

def calculate_standard_deviation():
    num_values = int(input("Enter the number of values: "))
    values = []

    for i in range(num_values):
        value = float(input("Enter a value: "))
        values.append(value)

    standard_deviation = statistics.stdev(values)
    
    print("Standard Deviation:", standard_deviation)
    
    print("Values =:", values)


calculate_standard_deviation()
