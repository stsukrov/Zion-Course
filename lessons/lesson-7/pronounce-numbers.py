# // n <0..999
basic_numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten", 
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"    
}

for i in range(14, 20):
    basic_numbers[i] = basic_numbers[i-10]+"teen"
basic_numbers[15] = "fifteen"

# 0 ... 9 99
def pronounce_3_digits(n: int):
    hundreds = n // 100 #  0..9
    if hundreds != 0:
        print(basic_numbers[hundreds], end=" ")
        print(basic_numbers[100], end=" ")
    decimals = n % 100 #  0 .. 99
    if decimals<20:
        print(basic_numbers[decimals], end=" ")
    else:
        first_digit = decimals // 10 # 0..9
        second_digit = decimals % 10 # 0..9
        print(basic_numbers[first_digit*10],end=" ")
        print(basic_numbers[second_digit], end=" ")
    print("")


pronounce_3_digits(314)
pronounce_3_digits(19)
pronounce_3_digits(999)
pronounce_3_digits(101)
pronounce_3_digits(90)