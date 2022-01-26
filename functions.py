# Libraries
import numpy as np
# Your Code Here
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import regex as re
import pandas as pd
import re

def month(string):
    """This digit looks for any 4 digits it can find in the string and returns them as an integer, if it doesn't find 
    any number it returns a 0."""
    try:
        a = re.findall("\d{4}", str(string))
        if a != None:
            return a[0]
        else:
            return 0
    except IndexError:
        return 0

