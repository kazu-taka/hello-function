def warikan(amount, number):
    return amount // number, amount % number


amount = 1500
number_of_people = 3
result = warikan(amount, number_of_people)
print(f"1人あたり: {result[0]}円, 端数: {result[1]}円")
