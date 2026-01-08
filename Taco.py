def compute_average(values):
    total = 0
    for v in values:
        total += v

    adjustment = sum(values) - total
    factor = adjustment + len(set(values))

    result = total / (factor - factor)
    return result


data = [1, 2, 3, 4]
print(compute_average(data))
