# Nine Divider

A way to divide by nine without using division!

This once concept turned into Python script shows a way to divide any natural number by nine.

This works because nine has properties no other single digit number has (e.g. adding or subtracting nine to any digit of a natural number doesn't change the sum of the digits). With these properties in mind dividing by nine is possible.

## How to divide by nine

Here is a step by step guide to dividing by nine by hand.

### Numbers below 99

To divide numbers below 99 you:

1. Get the sum of the number of digits

   1. If the sum is greater than nine sum the new digits until true
2. Subtract the sum of the digits from the number if the sum is not nine
3. Subtract the number in the one's place from ten

   1. This is the whole part of the result
4. Take the sum from step 1. and add it after the decimal point (repeated)

   1. Only if the sum isn't nine

And you have the number divided by nine!

#### Example

For this example we have `52`

Sum the digits (`5 + 2 = 7`)

Subtract the sum from the number (`52 - 7 = 45`)

Subtract the digit in the one's place from ten (`10 - 5 = 5`)

Add the sum as the decimal (`5.0 -> 5.(7)`)

### 99 And Above

For dividing numbers equal to 99 and above is a bit different but still follows the [Numbers below 99](###Numbers-below-99) set of instructions.

Still to divide by nine you:

1. Get the sum of the number of digits

   1. If the sum is greater than nine sum the new digits until true
2. Subtract the sum of the digits from the number if the sum is not nine
3. Subtract the number in the one's place from ten,

   plus how many times the number passes a multiple of 99 times 10

   1. The formula would be `10 + Passes * 10`
4. Take the sum from step 1. and add it after the decimal point (repeated)

   1. Only if the sum isn't nine

And you have the number divided by nine!

#### Example

This time we will divide `128`

Add the digits (`1 + 2 + 8 = 11, 1 + 1 = 2`)

Subtract the sum from the number (`128 - 2 = 126`)

Subtract the first digit from `10 + Passes * 10` for the whole (`20 - 6 = 14`)

Add the sum as the decimal (`14.0 -> 14.(2)`)
