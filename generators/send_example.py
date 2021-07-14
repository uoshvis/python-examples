def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False


def infinite_palindromes():
    num = 0
    while True:
        if is_palindrome(num):
            #  i takes the value that is yielded
            #  it allows you to .send() a value back to the generator
            i = (yield num)
            # i could be None if next() is called on the generator object
            if i is not None:
                # If i has a value, then you update num with the new value
                num = i
        # regardless of whether or not i holds a value,
        # you’ll then increment num and start the loop again
        num += 1


def main():
    #  yields a value once a palindrome is found
    pal_gen = infinite_palindromes()
    for i in pal_gen:
        digits = len(str(i))
        # brings execution back into the generator logic and assigns 10 ** digits to i
        pal_gen.send(10 ** (digits))
        print(i)


if __name__ == '__main__':
    main()
