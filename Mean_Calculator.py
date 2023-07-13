import statistics

def calculate_mean():
    num_values = int(input("Enter the number of values: "))
    values = []

    for i in range(num_values):
        value = float(input("Enter a value: "))
        values.append(value)

    mean = statistics.mean(values)
    print("Mean:", mean)


calculate_mean()
