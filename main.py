from source.OptiparmBasic import Optiparm

"""
Expected hierarchy:
    root/
        pd_model.csv
        ING_PD_ratings/
            main.py
            test_datastorage.py
            source/
                DataEntry.py
                DataStorage.py
                OptiparmBasic.py
            utils/
                variables.py
"""

algorithm = Optiparm()

algorithm.init_classes()

algorithm.write_input()

print("")   # new line

algorithm.write_output()