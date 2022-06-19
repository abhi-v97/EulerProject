"""


If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def num_to_words(n):
        if n < 20:
            return ones[n]
        elif 20 <= n < 100:
            return tens[n // 10] + (ones[int(repr(n)[-1])] if (n % 10 != 0) else "")
        elif 100 <= n < 1000:
            return  ones[int(repr(n)[0])] + "hundred" + ("and" + num_to_words(n%100)if n%100 != 0 else "")
        elif n == 1000:
            return "onethousand" #fix this


#print(tens[21 //10])
#print(ones[21[-1]])
def compute():
    ans = sum(len(num_to_words(i)) for i in range(1,1001))
    return str(ans)


if __name__ == "__main__":
    print(compute())
