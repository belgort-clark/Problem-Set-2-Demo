# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 2
# Body Mass Index

import os.path
import sys
from problem_2 import main
from tud_tests import *

def test_problem_2():

    try:
        exists = os.path.exists("problem_2.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input([170,70])
    main()
    output = get_display_output()

    assert output == [
            "Calculate BMI\n",
            "Enter the weight in pounds: ",
            "Enter the height in inches: ",
            "\nDetails",
            "\tWeight:\t\t 170.00 pounds\t\t\t 77.11 kilograms",
            "\tHeight:\t\t 70.00 inches\t\t\t 1.78 meters",
            "\tBMI:\t\t 24.39"
    ]
