def main():
    with open('input.txt', 'r') as f:
        input_raw = f.readlines()
        f.close()

    sum_digits = 0

    for ln in input_raw:
        temp_left = ln.split(' | ')[0].split(' ')
        temp_right = ln.split(' | ')[1].split(' ')
        temp_right[3] = temp_right[3].replace('\n','')

        temp_sum = ''
        leftupper_mid_unknown = ''
        fives = []
        sixes = []

        for digit in temp_left:
            if len(digit) == 2: 
                digit_1 = ''.join(sorted(digit))
            elif len(digit) == 3:
                digit_7 = ''.join(sorted(digit))
            elif len(digit) == 4:
                digit_4 = ''.join(sorted(digit))
            elif len(digit) == 7:
                digit_8 = ''.join(sorted(digit))
            elif len(digit) == 5:
                fives.append(''.join(sorted(digit)))
            elif len(digit) == 6:
                sixes.append(''.join(sorted(digit)))
        
        for i in digit_4:
            if i not in digit_1:
                leftupper_mid_unknown = leftupper_mid_unknown + i

        for letter in fives[0]:
            mid_counter = 0

            if letter not in digit_7 and letter in leftupper_mid_unknown:
                for i in fives:
                    if letter in i:
                        mid_counter += 1
            
            if mid_counter == len(fives):
                mid = letter

        for i in leftupper_mid_unknown:
            if i not in mid:
                leftupper = i

        for digit in fives:
            if digit_1[0] in digit and digit_1[1] in digit:
                digit_3 = ''.join(sorted(digit))
            elif leftupper in digit:
                digit_5 = ''.join(sorted(digit))
            else: digit_2  = ''.join(sorted(digit))
        
        for digit in sixes:
            if mid not in digit:
                digit_0 = ''.join(sorted(digit))
            elif digit_1[0] in digit and digit_1[1] in digit:
                digit_9 = ''.join(sorted(digit))
            else: digit_6  = ''.join(sorted(digit))

        digit_dict = {
            digit_0:0, 
            digit_1:1, 
            digit_2:2, 
            digit_3:3, 
            digit_4:4, 
            digit_5:5, 
            digit_6:6, 
            digit_7:7, 
            digit_8:8, 
            digit_9:9}

        for digit in temp_right:
            temp_sum = temp_sum + str(digit_dict[''.join(sorted(digit))])

        sum_digits += int(temp_sum)

    return sum_digits

if __name__ == '__main__':
    print(main())