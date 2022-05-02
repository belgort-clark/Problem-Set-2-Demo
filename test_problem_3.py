# DO NOT MODIFY THE CODE IN THIS FILE

# Tests for Problem 3
# Travel Time

import os.path
import sys
from problem_3 import main
from tud_tests import *

def test_problem_2():

    try:
        exists = os.path.exists("problem_3.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input(["Portland","Seattle",174])
    main()
    output = get_display_output()

    assert output == [
            "Calculate Trip Duration\n",
            "Enter the starting location: ",
            "Enter the ending location: ",
            "Enter the distance between the locations: ",
            "\nDetails",
            "\tStart:\t\t Portland",
            "\tEnd:\t\t Seattle",
            "\tDistance:\t 174 miles",
            "\tDuration:\t 2.90 hours"
    ]
