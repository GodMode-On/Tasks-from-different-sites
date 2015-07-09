class RomanNumerals:
    
    
    arab_nums_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_nums_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_nums = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    arab_nums = [1000, 500, 100, 50, 10, 5, 1]

    def to_roman(self, arab):
        res = ''
        index = 0
        while arab:
            if arab >= self.arab_nums_list[index]:
                res += self.roman_nums_list[index]
                arab -= self.arab_nums_list[index]
            else:
                index += 1
        return res
        
    def from_roman(self, roman):
        roman_values = dict(zip(self.roman_nums, range(7)))
        roman_arab = dict(zip(self.roman_nums, self.arab_nums))
        res = 0
        roman = roman[::-1]
        for i, roman_digit in enumerate(roman):
            if i == 0:
                res += roman_arab[roman_digit]
            else:
                if roman_values[roman_digit] <= roman_values[roman[i-1]]:
                    res += roman_arab[roman_digit]
                else:
                    res -= roman_arab[roman_digit]
        return res
