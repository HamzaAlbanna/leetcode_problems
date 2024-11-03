class Solution:
    def romanToInt(self, s):
        sum = 0
        prev_value = 0
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for c in s:
            current_value = values[c]
            sum += current_value if current_value <= prev_value else current_value - 2 * prev_value
            prev_value = current_value

        return sum