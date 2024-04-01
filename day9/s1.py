file = open("input.txt")
predictions = []
for line in file:
    data = [int(reading) for reading in line.split()]
    prediction = data[-1]
    while any(data):
        data = [data[i + 1] - data[i] for i in range(len(data) - 1)]
        prediction += data[-1]
    predictions.append(prediction)
print(sum(predictions))
