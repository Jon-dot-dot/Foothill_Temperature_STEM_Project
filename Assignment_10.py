"""
STEM Temperature Project
Submitted by Jonathan Lopez

Assignment 9: This sections we load in the data

Assignment 8: The TempDataset class for managing temp data (separate from this project)

Assignment 7: This assignment we added print_filter, change_filter. and then we test it out with the 3rd option, test run is at the bottom.

Assignment 6: The bubble sort with the sensor list but using recursion

Assignment 5: The recursion project (separate from the main project)

Assigment 4: This is creating a sensor list and filter list

Assignment 3: This is when we implement the Menu

Assignment 2: This assignment adds code to tell the user for a temperature in Celsius and then converts that temperature to a specified different temp unit.

Assignment 1: This program demostrates  printing lines of text to the screen
"""
import math


current_unit = 0

UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}

def choose_unit():
    """
    lets the user to select a new temp unit, reports the current unit, prints the menu using the UNITs dict
    """
    global current_unit


    print(f"\nCurrent unit is {UNITS[current_unit][0]}")


    while True:
        print("Choose new unit:")
        for key in UNITS
            print(f"{key} - {UNITS[key][0]}")
        print()


        choice = input("Which unit? ")


        if not choice.isdigit():
            print("Please enter a number only\n")
            continue


        choice = int(choice)


        if choice not in UNITS:
            print("Please choose a unit from the list\n")
            continue


        current_unit = choice
        break





def print_header():
    """
    This is to show what the project is and who made it
    :return:
    """
    print("STEM Center Temperature Project")
    print("Jonathan Lopez")




def convert_units(celsius_value, units):
    """
    This section is for converting to the different units that was chosen by a user
    :param celsius_value:
    :param units:
    :return:
    """
    if units == 0:
        return float(celsius_value)
    elif units == 1:
        return float(celsius_value * 9/5 + 32)
    elif units == 2:
        return float(celsius_value + 273.15)
    else:
        print("Please chose either 0, 1, or 2")
    exit()


def print_menu():
    print()
    print("Main Menu")
    print("----------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by data and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


def new_file(dataset):
    """
    This is to open a new file
    """
    print("New File Function Called")


def Choose_units():
    """
    This is the option for Choose units
    :return:
    """
    print("You chose, Choose units")


def change_filter(sensor_list, active_sensors):
    """
    This is to change the filter
    :return:
    """
    print("You chose, Edit room filter")


def print_summary_statistics(dataset, active_sensors):
    """
    This is to get the summary
    :param dataset:
    :param active_sensors:
    :return:
    """
    print("You chose, Show Summary statistics")


def print_temp_by_day_time(dataset, active_sensors):
    """
    This is for show temperature by date and time
    :param dataset:
    :param active_sensors:
    :return:
    """
    print("You chose, Show Temperature by date and time")


def print_histogram(dataset, active_sensors):
    """
    This is for the histogram
    :param dataset:
    :param active_sensors:
    :return:
    """
    print("You chose, Show histogram of temperatures")


def recursive_sort(list_to_sort, key):
    """
    This is the recursive sort function
    :param list_to_sort:
    :param key:
    :return:
    """
    lst = list_to_sort.copy()
    if len(lst) <= 1:
        return lst

    swapped = False
    for i in range(len(lst) - 1):
        if lst[i][key] > lst[i + 1][key]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            swapped = True

    if not swapped:
        return lst

    return recursive_sort(lst[:-1], key) + [lst[-1]]



def print_filter(sensor_list, filter_list):
    """
    prints the list of sensors and shows which ones are active or inactive
    :param sensor_list:
    :param filter_list:
    :return:
    """
    for room_num, room_name, sensor_num in sensor_list:
        if sensor_num in filter_list:
            print(f"{room_num}: {room_name} [ACTIVE]")
        else:
            print(f"{room_num}: {room_name} [INACTIVE]")


def change_filter(sensors, sensor_list, filter_list):
    """
    This is the function that changes the filter
    :param sensors:
    :param sensor_list:
    :param filter_list:
    :return:
    """
    while True:
        print()
        print_filter(sensor_list, filter_list)
        user_input = input("\nType the sensor to toggle (e.g. 4201) or x to end ").strip()


        if user_input.lower() == "x":
            break

        if user_input not in sensors:
            print("\nInvalid Sensor")
            continue

        sensor_num = sensors[user_input][1]

        if sensor_num in filter_list:
            filter_list.remove(sensor_num)
        else:
            filter_list.append(sensor_num)


class TempDataset:
    _object_count = 0

    @property
    def name(self):
        """
        this returns the name of the temp dataset
        """
        return self._name


    @name.setter
    def name(self, new_name):
        """
        this sets the name of the temp dataset and confirms it
        """
        if not isinstance(new_name, str):
            raise ValueError("Name must be a string")
        if len(new_name) < 3 or len(new_name) > 20:
            raise ValueError("Name must be between 3 and 20 characters")
        self._name = new_name


    def __init__(self):
        """
        Initialize dataset object with defaults
        """
        self._data_set = None
        self._name = ""
        TempDataset._object_count += 1


    def process_file(self, filename):
        """
        Load temp data from CSV file
        """
        try:
            with open(filename, "r") as file:
                self._data_set = []

                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        parts = line.split(",")
                        if len(parts) != 5:
                            continue

                        day = int(parts[0])
                        time_float = float(parts[1])
                        sensor = int(parts[2])
                        reading_type = parts[3]
                        value = float(parts[4])

                        if reading_type != "TEMP":
                            continue

                        hour = math.floor(time_float * 24)

                        self._data_set.append((day, hour, sensor, value))
                    except ValueError:
                        continue
            return True

        except FileNotFoundError:
            return False
        except Exception:
            return False




    def get_loaded_temps(self):
        if self._data_set is None:
            return None
        return len(self._data_set)




    def get_summary_statistics(self, filter_list):
        """
        Returns None if dataset empty, else placeholder tuple
        """
        if self._data_set is None:
            return None

        temps = [row[3] for row in self._data_set if row[2] in filter_list]

        if not temps:
            return None

        return (min(temps), max(temps), sum(temps) / len(temps))


    def get_avg_temperature_day_time(self, filter_list, day, time):
        """
        Returns None if dataset empty, else placeholder 0
        """
        if self._data_set is None:
            return None

        temps = [
            row[3]
            for row in self._data_setif row[2] in filter_list and row[0] == day and row[1] == time
        ]
        return None if not temps else sum(temps) / len(temps)

    def get_num_temps(self, filter_list, lower_bound, upper_bound):
        """
        Returns None if dataset empty, else placeholder 0
        """
        if self._data_set is None:
            return None
        return 0


    @classmethod
    def get_num_objects(cls):
        """
        Return number of TempDataset objects created
        """
        return cls._object_count



def new_file(dataset_obj):
    """
    loads data file and prompts for dataset name
    """
    filename = input("Please enter the filename of the new dataset: ")

    if not dataset_obj.process_file(filename):
        print("Unable to load file")
        return

    count = dataset_obj.get_loaded_temps()
    print(f"Loaded {count} samples\n")

    while True:
        name = input("Please provide a 3 to 20 character name for the dataset: ")
        try:
            dataset_obj.name = name
            break
        except ValueError:
            print("Invalid name. Please try again")




def main():
    """This is the Main function to run the Menu  """
    print_header()
    """
    the zero is for it loops at least once
    """
    choice = 0
    """
    These are the None values 
    """
    dataset = TempDataset()

    active_sensors = filter_list





    """
    The loop is going to keep running until the users chooses 7 so that it can quit
    """
    while choice != 7:
        print_menu()

        try:
            user_input = input("what is your choice? ")
            choice = int(user_input)

            if choice == 1:
                new_file(dataset)
            elif choice == 2:
                Choose_units()
            elif choice == 3:
                change_filter(sensors, sensor_list, filter_list)
            elif choice == 4:
                print_summary_statistics(dataset, active_sensors)
            elif choice == 5:
                print_temp_by_day_time(dataset, active_sensors)
            elif choice == 6:
                print_histogram(dataset, active_sensors)
            elif choice == 7:
                pass
            else:
                print("Please only chose one of the options\n")

        except ValueError:
            """
            This is for, when a user puts a non-integer like a letter or a word
            """
            choice = 0
            print("You can only chose numbers only")
    print("Thank you for using the STEM Center Temperature Project\n")





"""
The sensors dictionary for the different sensors
"""

sensors = {
    "4213": ("STEM Center", 0),
    "4201": ("Foundations Lab", 1),
    "4204": ("CS Lab", 2),
    "4218": ("Workshop Room", 3),
    "4205": ("Tiled Room", 4),
    "Out": ("Outside", 5)
}

"""
Sensor_list for the sensors, list of tuples (number, Descriptions, number
"""
sensor_list = [(k, v[0], v[1]) for k, v in sensors.items()]

"""
filter_list : list of all sensors numbers (int)
"""
filter_list = [v[1] for v in sensors.values()]


print("\nOriginal unsorted list\n", sensor_list)
print("\nList sorted by room number\n", recursive_sort(sensor_list, 0))
print("\nList sorted by room name\n", recursive_sort(sensor_list, 1))
print("\nOriginal unsorted list\n", sensor_list)


print("Testing sensors: ")
if sensors["4213"][0] == "STEM Center" and sensors["Out"][1] == 5:
    print("Pass")
else:
    print("Fail")

print("Testing sensor_list length: ")
if len(sensor_list) == 6:
    print("Pass")
    print("Testing sensor_list content: ")
    for item in sensor_list:
        if item[1] != sensors[item[0]][0]:
            print("Fail")
            break
    else:
        print("Pass")
else:
    print("Fail")

print("Testing filter_list length:")
if len(filter_list) == 6:
    print("Pass")
else:
    print("Fail")

print("Testing filter_list content: ")
if sum(filter_list) == 15:
    print("Pass")
else:
    print("Fail")


    celsius_value = float(input("Please enter the temperature in Celsius: \n"))
    units = int(input("Please enter the conversion: 0 = Celsius, 1 = Fahrenheit, 2 = Kelvin: "))

    converted_temp = convert_units(celsius_value, units)

    if units == 0:
        print(f"That's {converted_temp:.2f} degrees Celsius.")
    elif units == 1:
        print(f"That's {converted_temp:.2f} degrees Fahrenheit.")
    elif units == 2:
        print(f"That's {converted_temp:.2f} degrees Kelvin.")


if __name__ == "__main__":
    main()

r"""
C:\Users\Jonat\PycharmProjects\CybersecurityProjects\.venv\Scripts\python.exe C:\Users\Jonat\PycharmProjects\CybersecurityProjects\Assignment_9.py 

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]

List sorted by room number
 [('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4205', 'Tiled Room', 4), ('4213', 'STEM Center', 0), ('4218', 'Workshop Room', 3), ('Out', 'Outside', 5)]

List sorted by room name
 [('4204', 'CS Lab', 2), ('4201', 'Foundations Lab', 1), ('Out', 'Outside', 5), ('4213', 'STEM Center', 0), ('4205', 'Tiled Room', 4), ('4218', 'Workshop Room', 3)]

Original unsorted list
 [('4213', 'STEM Center', 0), ('4201', 'Foundations Lab', 1), ('4204', 'CS Lab', 2), ('4218', 'Workshop Room', 3), ('4205', 'Tiled Room', 4), ('Out', 'Outside', 5)]
Testing sensors: 
Pass
Testing sensor_list length: 
Pass
Testing sensor_list content: 
Pass
Testing filter_list length:
Pass
Testing filter_list content: 
Pass
STEM Center Temperature Project
Jonathan Lopez

Main Menu
----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by data and time
6 - Show histogram of temperatures
7 - Quit
what is your choice? 1
Please enter the filename of the new dataset: Temperatures_2025-11-07.csv
Loaded 11724 samples

Please provide a 3 to 20 character name for the dataset: z
Invalid name. Please try again
Please provide a 3 to 20 character name for the dataset: jonathanjonathanjonathanjonathan
Invalid name. Please try again
Please provide a 3 to 20 character name for the dataset: jonathansdata.csv

Main Menu
----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by data and time
6 - Show histogram of temperatures
7 - Quit
what is your choice? 1
Please enter the filename of the new dataset: Myjonathandata
Unable to load file

Main Menu
----------
1 - Process a new data file
2 - Choose units
3 - Edit room filter
4 - Show summary statistics
5 - Show temperature by data and time
6 - Show histogram of temperatures
7 - Quit
what is your choice? 7
Thank you for using the STEM Center Temperature Project


Process finished with exit code 0

"""