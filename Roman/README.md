# Roman Numeral Converter

This exercise practices converting between Roman numerals and integers. The implementation is in [`roman.py`](roman.py), and the automated tests are in [`test_roman.py`](test_roman.py).

## Supported Functions

### `roman_to_integer(roman)`

Converts a Roman numeral string into an integer.

```python
from roman import roman_to_integer

roman_to_integer("XVI")       # 16
roman_to_integer("iv")        # 4
roman_to_integer("MMMCMXCIX") # 3999
```

The function accepts lowercase input by converting it to uppercase first. It raises `ValueError` when the input is empty, contains an unknown character, breaks a Roman numeral rule, or represents a number outside the range 1 through 3999.

### `integer_to_roman(number)`

Converts an integer into Roman numeral notation.

```python
from roman import integer_to_roman

integer_to_roman(4)    # "IV"
integer_to_roman(2026) # "MMXXVI"
```

The converter uses the values below, from largest to smallest:

| Value | Symbol |
| ----: | :----- |
|  1000 | M      |
|   500 | D      |
|   100 | C      |
|    50 | L      |
|    10 | X      |
|     5 | V      |
|     1 | I      |

It also handles the standard subtractive values `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`.

## Rules Applied

1. Only `I`, `V`, `X`, `L`, `C`, `D`, and `M` are valid symbols.
2. `I`, `X`, `C`, and `M` may be repeated at most three times in a row.
3. `V`, `L`, and `D` cannot be repeated.
4. A smaller value can come before a larger value only in an approved subtractive pair: `IV`, `IX`, `XL`, `XC`, `CD`, or `CM`.
5. The final numeral must be in canonical form. For example, `IIII` is rejected because `IV` is the correct representation of 4.
6. Values must be between 1 and 3999.

## How the Conversion Works

For Roman-to-integer conversion, the function compares each symbol with the symbol immediately after it:

- if the current value is smaller, it is subtracted;
- otherwise, it is added.

For example, `XIV` becomes $10 + (5 - 1) = 14$. After calculating the total, the function converts that total back to Roman notation. If the result does not exactly match the original normalized input, the input is rejected as non-canonical.

For integer-to-Roman conversion, the function repeatedly takes the largest Roman value that fits into the remaining number. For example, 944 becomes `CM` + `XL` + `IV`, or `CMXLIV`.

## Running the Tests

From this folder, run:

```bash
python3 -m pytest
```

The tests cover normal values, lowercase input, subtractive notation, boundary values, repeated symbols, invalid symbols, and invalid subtraction patterns.
