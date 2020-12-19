# sort number with start from beginning and go 'til the end. if the selected smaller than the last one so their place will replace.

numbers = [  # Random number from the (randomNumberForNumbersFrom1To1000) Function
]
sorted_numbers = []


def randomNumberForNumbersFrom1To1000(From, To, HowMany):
    import random
    for i in range(0, HowMany):
        n = random.randint(From, To)
        numbers.append(n)
    print(numbers)


def sortTheList(self):
    lengthOfList = len(numbers)
    sorted_numbers.append(numbers[0])
    for currentIndex in range(1, lengthOfList):
        currentNumber = numbers[currentIndex]
        for previousIndex in range(currentIndex):
            previousNumber = sorted_numbers[previousIndex]
            if currentNumber > previousNumber:
                if previousIndex == currentIndex - 1 or currentIndex == 0:
                    sorted_numbers.append(currentNumber)
                else:
                    continue  # didn't reach the end of the list to decide
            else:
                if currentNumber not in sorted_numbers:
                    sorted_numbers.append(currentNumber)
                (sorted_numbers[previousIndex], sorted_numbers[-1]) = (sorted_numbers[-1], previousNumber)
    return sorted_numbers


print(randomNumberForNumbersFrom1To1000(1, 500, 20))
print(sortTheList('self'))
