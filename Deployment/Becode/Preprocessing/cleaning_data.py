import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# this function will take the user input as a JSON than it will convert it dataframe


def user_input():

    data = {}
    data["living_area"] = input("Enter the living area: ")
    data["property-type"] = input("Enter the property type: ")
    data["number_of_rooms"] = input("Enter the number of rooms: ")
    data["garden"] = input("Is there a garden? (yes = 1 / no = 0): ")
    data["fully_equipped_kitchen"] = input(
        "Is the kitchen equipped? (yes = 1 / no = 0): ")
    data["furnished"] = input(
        "Is the property furnished? (yes = 1 / no = 0): ")
    data["terrace"] = input("Is the property furnished? (yes = 1 / no = 0): ")
    data["garden"] = input("Is the property furnished? (yes = 1 / no = 0): ")
    data["garden"] = input("Is the property furnished? (yes = 1 / no = 0): ")
    data["region"] = input("Enter the region: ")

    df = pd.DataFrame(data, index=[0])

    return df
