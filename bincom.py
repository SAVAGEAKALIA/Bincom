#!/usr/bin/env python
""" Script to find the mean, median, mode and variance"""

import random


def color_code():
    """ FUnction to analyze data for color codes"""
    monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED',
              'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
    tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLUE', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED',
               'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']
    wednesday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED',
                 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']
    thursday = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED',
                'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
    friday = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 'WHITE', 'ORANGE', 'RED', 'RED', 'RED',
              'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']

    total_colors = monday + tuesday + wednesday + thursday + friday
    # Arrange by key value pair in a dictionary
    color_frequency = {}

    for color in total_colors:
        if color in color_frequency:
            color_frequency[color] += 1
        else:
            color_frequency[color] = 1

    # collect values for each color from dictionary

    list_values = []
    for key, value in color_frequency.items():
        # print(f"{key}: {value}")
        list_values.append(value)
    print(list_values)

    # Find the highest frequency
    mode_dataset = 0
    for value in range(len(list_values)):
        if mode_dataset > list_values[value]:
            pass
        elif list_values[value] > mode_dataset:
            mode_dataset = list_values[value]
        else:
            continue
    print(f'Mode: {mode_dataset}')

    # find the mean dataset
    mean_dataset = 0
    for value in list_values:
        mean_dataset += value
    mean = mean_dataset / len(list_values)
    print(f'Mean: {mean}')

    # find the median dataset
    sorted_list = sorted(list_values)
    number_index_list = len(sorted_list)

    if number_index_list % 2 == 0:
        print('list is even')
        first_index = (number_index_list // 2) - 1
        second_index = number_index_list // 2
        median_dataset = (sorted_list[first_index] + sorted_list[second_index]) / 2
        print(f'Median: {median_dataset}')
    else:
        print('list is odd')
        median_index = number_index_list // 2
        median_dataset = sorted_list[median_index]
        print(f'Median: {median_dataset}')

    # find the variance dataset
    variance_dataset = 0
    for value in list_values:
        variance_dataset += (value - mean) ** 2
    variance = variance_dataset / len(list_values)
    print(f'Variance: {variance}')

    # probability of red being selected
    probability_red = color_frequency['RED'] / len(list_values)
    print(f'Probability: {probability_red}')

    # import psycopg2
    #
    # conn = psycopg2.connect(
    #     dbname="your_database",
    #     user="your_username",
    #     password="your_password",
    #     host="your_host"
    # )
    #
    # cur = conn.cursor()
    #
    # # Create table
    # cur.execute("""
    #     CREATE TABLE IF NOT EXISTS color_frequencies (
    #         color VARCHAR(50) PRIMARY KEY,
    #         frequency INTEGER
    #     )
    # """)
    #
    # # Insert data
    # for color, count in color_counts.items():
    #     cur.execute("""
    #         INSERT INTO color_frequencies (color, frequency)
    #         VALUES (%s, %s)
    #         ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency
    #     """, (color, count))
    #
    # conn.commit()
    # cur.close()
    # conn.close()

    # generate random digits

    ran = ""
    for val in range(4):
        ran += str(random.choice([0, 1]))

    print(f'Random Number to Base 10: {int(ran, 2)}')

    # fibonacci sequence
    fib_sequence = [0, 1]
    for i in range(1, 50):
        # print(i)
        # print(fib_sequence[i])
        fib_sequence.append(fib_sequence[i] + fib_sequence[i - 1])

    fib_total = 0
    for val in fib_sequence:
        fib_total += val

    print(f'Sum of 50 Fibonacci Sequence: {fib_total}')


if __name__ == '__main__':
    color_code()
