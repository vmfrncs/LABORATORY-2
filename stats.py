def mean(numbers):
    """Compute the average of a set of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    """Compute the median of a set of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if len(numbers) == 0:
        return 0

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        # Even number of elements, average the two middle ones
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        # Odd number of elements, return the middle one
        return sorted_numbers[n // 2]


def mode(numbers):
    """Compute the mode of a set of numbers."""
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    if len(numbers) == 0:
        return []

    count_dict = {}
    max_count = 0
    modes = []

    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
        if count_dict[num] > max_count:
            max_count = count_dict[num]
            modes = [num]
        elif count_dict[num] == max_count:
            modes.append(num)

    # Remove duplicates from modes and return sorted
    return sorted(set(modes)) if max_count > 1 else []


def main():
    """Test the mean, median, and mode functions."""
    numbers = [4, 9, 3, 7, 5, 8, 6, 2, 1, 4, 7, 7]
    print("Numbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode(s):", mode(numbers))


if __name__ == "__main__":
    main()
