#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:02:15 2023

@author: brunykrijgsman
"""

# Make an Python repository and publish it on https://github.com or https://gitlab.com/ or a 
# similar website that uses git. The Python package will contain one function cheat(). 
# The cheat() function should take one argument specifying which exercise of any previous Python 
# assignment the user of your package wants to cheat on. Given the exercise number, your 
# cheat()function tells the user the correct solution. The cheat function should work for at least 4 exercises.

# You can also create a README file for your Python repository using Markdown.

# You are free to reuse this function in the exam :).


def cheat(assignment):
    if (not type(assignment) == str):
        raise Exception("The input must be a 'string'.")
    elif (assignment == "1.2P.10"):
        print(
        """
            np.random.seed(1234) # Set the random seed.
            speed_sec = np.zeros(10)
            sim_speed = np.random.uniform(size=5) # Speed simulation in seconds 
            speed_sec[0:5] = sim_speed * np.random.uniform(low=0.5, high=10, size=5) 
            speed_sec[5:10] = sim_speed
    
            # Creating variables to put in dictionary.
            language = np.repeat([["R"],["Python"]], 5) # Language variable.
    
            code_type = list(map(lambda x: f'forloop{x}', range(1,6))) * 2 # Code type variable. 
    
            # Making dictionary before creating the dataframe.
            dict = {"language": language, 
                    "code_type": code_type, 
                    "speed": speed_sec}
    
            # Creating dataframe
            my_dataframe = pd.DataFrame.from_dict(dict) 
            print(my_dataframe))
        """
        )
    elif (assignment == "2.2P.1"):
        print(
        """
            # Creating time variable
            current_time = int(time.strftime("%H"))
    
            # If statement 
            if (current_time >= 1) and (current_time <= 4):
                print("Go to sleep")
            elif (current_time >= 8) and (current_time <= 9):
                print("Eet je hageslag!")
            else:
                print("Gut gemacht")
        """
        )
    elif (assignment == "2.2P.2"):
        print(
            """
                # Numeric vector of four elements
                numeric_vec = np.random.uniform(low=0, high=100, size=4)
                weight_sum = 2*0
    
                for i in range(len(numeric_vec)):
                    if i%2 == 0:
                        weight_sum = weight_sum + numeric_vec[i] 
                    else: 
                        weight_sum = weight_sum + numeric_vec[i] * 2
                    
    
                weight_avg = weight_sum / (np.size(numeric_vec) * 1.5)
                print(weight_avg)
            """
            )
    elif (assignment == "2.2P.4"):
            print(
            """
                input = np.array([1,2,5,6,2,2,1,6,5,7])
    
                def special(input):
                    my_unique_values = []
                    if (isinstance(input, np.ndarray) == False):
                        raise Exception("The input is not a 'numpy vector'.")
                    for i in input:
                        if (not i in my_unique_values):
                            my_unique_values = np.append(my_unique_values, i)
                        if (len(input) == len(my_unique_values)):
                            warnings.warn(" All values are special!")
                    return my_unique_values
    
                uniq = special(input)
                print(uniq)
            """
            )



cheat("2.2P.4")

    
        