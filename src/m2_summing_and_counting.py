"""
This module lets you practice the ACCUMULATOR pattern in classic forms:
   SUMMING:    total = total + number
   COUNTING:   count = count + 1

A subsequent module lets you practice the ACCUMULATOR pattern in another classic form:
   IN GRAPHICS:   x = x + pixels

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Dominic Yurkanin.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_more_cosines()
    run_test_count_sines_from()
    run_test_count_sines_vs_cosines()


def run_test_sum_more_cosines():
    """ Tests the   sum_more_cosines   function. """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this TEST function.
    #   It TESTS the  sum_more_cosines  function defined below.
    #   Include at least **   3   ** tests (we wrote one for you).
    #
    # To implement this TEST function, use the same 4 steps as before:
    #
    #   Step 1: Read the doc-string of  sum_more_cosines  below.
    #     Understand what that function SHOULD return.
    #
    #   Step 2:  Pick a test case:  numbers that you could send as
    #     actual arguments to the  sum_more_cosines  function.
    #
    #   Step 3: Figure out (by hand, or by trusting a test case that
    #     your instructor provided in the doc-string)
    #     the CORRECT (EXPECTED) answer for your test case.
    #
    #   Step 4: Write code that prints both the EXPECTED answer
    #     and the ACTUAL answer returned when you call the function.
    #     Follow the same form as in the test case we provided below.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_more_cosines   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 0.00198582  # This is APPROXIMATELY the correct answer.
    answer = sum_more_cosines(5, 17)
    print('Test 1 expected:', expected, '(approximately)')
    print('       actual:  ', answer)

    # ------------------------------------------------------------------
    # TO DO: 2 (continued).
    # Below this comment, add 2 more test cases of your own choosing.
    # ------------------------------------------------------------------
    expected = -0.519481
    answer = sum_more_cosines(0, 4)
    print('Test 2 expected:', expected, '(approximately)')
    print('       actual:  ', answer)


    expected = -1.235818
    answer = sum_more_cosines(1, 5)
    print('Test 3 expected:', expected, '(approximately)')
    print('       actual:  ', answer)


def sum_more_cosines(m, n):
    """
    What comes in:  The two arguments are integers m and n, with m <= n.
    What goes out:  Returns the sum
       cos(m) + cos(m+1) + cos(m+2) +  ...  cos(n)
    Side effects:   None.
    Examples:
      -- sum_more_cosines(0, 3)  returns
            cos(0) + cos(1) + cos(2) + cos(3)
         which is approximately 0.13416
      -- sum_more_cosines(-4, 1)  returns
            cos(-4) + cos(-3) + cos(-2) + cos(-1) + cos(0) + cos(1)
         which is approximately 0.02082.
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    # IMPORTANT: In this and all other problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    #   That is, no fair using   range(m, n)   or anything like that.
    #   Just   range(blah)   where blah is a single variable.
    #   Reason: To ensure that you get more practice using variables.
    # ------------------------------------------------------------------
    total = 0
    for k in range(n-m+1):
        total = total + (math.cos(k+m))

    return total

def run_test_count_sines_from():
    """ Tests the   count_sines_from   function. """
    # ------------------------------------------------------------------
    # DONE: 4. Implement this TEST function.
    #   It TESTS the  count_sines_from  function defined below.
    #   Include at least **   6   ** tests (we wrote one for you).
    #              ** Yes, 6 (six) tests. **
    #     ** Counting problems are harder to test than summing. **
    # Use the same 4-step process as for previous TEST functions.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_sines_from   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 5
    answer = count_sines_from(3, 9)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    # ------------------------------------------------------------------
    # TO DO: 4 (continued).
    # Below this comment, add 5 more test cases of your own choosing.
    # ------------------------------------------------------------------
    expected = 5
    answer = count_sines_from(4, 10)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    expected = 7
    answer = count_sines_from(2, 11)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    expected = 13
    answer = count_sines_from(2, 20)
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    expected = 4
    answer = count_sines_from(3, 8)
    print('Test 5 expected:', expected)
    print('       actual:  ', answer)

    expected = 4
    answer = count_sines_from(1, 6)
    print('Test 6 expected:', expected)
    print('       actual:  ', answer)
def count_sines_from(m, n):
    """
    What comes in:  The two arguments are integers m and n, with m <= n.
    What goes out:  Returns the number of integers from m to n,
       inclusive, whose sine is less than 0.5.
    Side effects:   None.
    Examples:
    Since:  sine(3) is about 0.14
            sine(4) is about -0.76
            sine(5) is about -0.96
            sine(6) is about -0.28
            sine(7) is about 0.66
            sine(8) is about 0.99
            sine(9) is about 0.41
      -- count_sines_from(3, 9)  returns  5
      -- count_sines_from(4, 6)  returns  3
      -- count_sines_from(7, 7)  returns  0
      -- count_sines_from(9, 9)  returns  1
    """
    # ------------------------------------------------------------------
    # DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPORTANT: As in previous problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    # ------------------------------------------------------------------
    count = 0
    for k in range(n-m+1):
        if math.sin(k+m) < 0.5:
            count = count + 1

    return count
def run_test_count_sines_vs_cosines():
    """ Tests the   count_sines_vs_cosines   function. """
    # ------------------------------------------------------------------
    # TODO: 6. Implement this TEST function.
    #   It TESTS the  count_sines_vs_cosines  function defined below.
    #   Include at least **   6   ** tests (we wrote one for you).
    #              ** Yes, 6 (six) tests. **
    #     ** Counting problems are harder to test than summing. **
    # Use the same 4-step process as for previous TEST functions.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   count_sines_vs_cosines   function:')
    print('--------------------------------------------------')

    # Test 1:
    expected = 100
    answer = count_sines_vs_cosines(101)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 19
    answer = count_sines_vs_cosines(19)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    expected = 12
    answer = count_sines_vs_cosines(11)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

    expected = 213
    answer = count_sines_vs_cosines(215)
    print('Test 4 expected:', expected)
    print('       actual:  ', answer)

    expected = 32
    answer = count_sines_vs_cosines(33)
    print('Test 5 expected:', expected)
    print('       actual:  ', answer)

    expected = 50
    answer = count_sines_vs_cosines(51)
    print('Test 6 expected:', expected)
    print('       actual:  ', answer)


    # ------------------------------------------------------------------
    # TO DO: 6 (continued).
    # Below this comment, add 5 more test cases of your own choosing.
    # ------------------------------------------------------------------


def count_sines_vs_cosines(m):
    """
    What comes in:  The sole argument is a non-negative integer m.
    What goes out:  Returns the number of integers from -m to m,
       inclusive, whose sine is greater than its cosine.
    Side effects:   None.
    Examples:
    Since:  sine(-5) is about  0.96  and cosine(-5) is about  0.28
            sine(-4) is about  0.76  and cosine(-4) is about -0.65
            sine(-3) is about -0.14  and cosine(-3) is about -0.99
            sine(-2) is about -0.91  and cosine(-2) is about -0.42
            sine(-1) is about -0.84  and cosine(-1) is about  0.54
            sine(0)  is about  0.00  and  cosine(0) is about  1.00
            sine(1)  is about  0.84  and  cosine(1) is about  0.54
            sine(2)  is about  0.91  and  cosine(2) is about -0.42
            sine(3)  is about  0.14  and  cosine(3) is about -0.99
            sine(4)  is about -0.76  and  cosine(4) is about -0.65
            sine(5)  is about -0.96  and  cosine(5) is about  0.28
      -- count_sines_vs_cosines(5) returns 6
      -- count_sines_vs_cosines(3) returns 4
      -- count_sines_vs_cosines(0) returns 0
      -- count_sines_vs_cosines(1) returns 1
      -- Also:  count_sines_vs_cosines(101) returns 100 (trust me!)
    """
    # ------------------------------------------------------------------
    # TODO: 7. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #
    # IMPORTANT: As in previous problems in this session,
    #   you must NOT use the 2 or 3-parameter versions
    #   of the RANGE expression, if you happen to know them.
    # ------------------------------------------------------------------
    count = 0
    for k in range(2*m):
        if math.sin(k-m) > math.cos(k-m):
            count = count + 1
    return count

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
