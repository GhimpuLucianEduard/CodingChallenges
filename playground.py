def build_n(n):
    n_str = str(n)
    rez = ""

    current_digit = n_str[0]
    current_digit_sum = 0
    for digit in n_str:
        if digit == current_digit:
            current_digit_sum += 1
        else:
            rez = rez + str(current_digit_sum) + current_digit
            current_digit = digit
            current_digit_sum = 1
    rez = rez + str(current_digit_sum) + current_digit
    return rez

def main():
    print(build_n(11))

if __name__ == '__main__':
    main()
