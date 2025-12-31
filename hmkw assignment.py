import matplotlib.pyplot as plt
# Creating blank lists to store all the data
month = []
recordHighF = []
recordLowF = []
avgSnowIn = []
avgHigh = []
# Creating the color tuple
my_colors=("#fbf8cc","#fde4cf","#ffcfd2","#f1c0e8","#cfbaf0",
            "#a3c4f3","#90dbf4","#8eecf5","#98f5e1","#b9fbc0",
             "#ffd6a5","#caffbf"
           )


def file1 ():
    """
    This function reads in the first file and splits it into separate lists
    """
    with open("flatbush_extremes.csv", "r") as f:
        # Skipping the header line
        f.readline().strip()
        for line in f:
            line = line.strip()
            if line != "":
                # Appending each column to a different list
                parts = line.split(",")
                month.append(parts[0])
                recordHighF.append(int(parts[1]))
                recordLowF.append(int(parts[2]))
                avgSnowIn.append(float(parts[3]))


def file2 ():
    """This function reads in the second file and grabs only the second column of information
    which is the only one we need"""
    with open("weather_data_flatbush.csv", "r") as f:
        f.readline().strip()  # skip the header
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                # Appending the average Highs the the list
                avgHigh.append(int(parts[1]))


def plot1 ():
    """This function creates a bar graph showing the average high temperatures per month"""
    plt.title("Average High per Month")
    # Calculating the x values
    left_edge = range(len(month))
    # The y values
    heights = avgHigh
    bar_width = 0.5
    # Drawing the bar graph
    plt.bar(left_edge, heights, bar_width,
             color=my_colors)
    # Placing ticks
    plt.xticks(left_edge, month)

    #Labeling the axis
    plt.xlabel("Months")
    plt.ylabel("Average High")

    # Creating a grid and printing the graph
    plt.grid(True)
    plt.show()

    # Calculating the max
    greatest = max(avgHigh)
    i = avgHigh.index(greatest)
    print(f"The month with the highest average is: {month[i]}")

    #Calculating the min
    smallest = min(avgHigh)
    s = avgHigh.index(smallest)
    print(f"The month with the lowest average is: {month[s]}")

    #Calculating the average
    print(f"The average value is: {sum(avgHigh) / 12}")


def plot2():
    """This function draws a line graph that shows average snowfall per month"""
    plt.title("Average Snowfall per Month")

    # The x values
    left_edge = range(len(month))

    plt.xticks(left_edge, month)

    plt.xlabel("Months")
    plt.ylabel("Snowfall")

    plt.grid(True)
    plt.plot(left_edge, avgSnowIn, color=my_colors[4] , marker="o")
    plt.show()

    greatest = max(avgSnowIn)
    i = avgSnowIn.index(greatest)
    print(f" The month with the highest value is: {month[i]}")

    smallest = min(avgSnowIn)
    s = avgSnowIn.index(smallest)
    print(f"The month with the lowest value is: {month[s]}")

    print(f"The average value is: {sum(avgSnowIn) / 12}")


def plot3():
    """This function draws a line graph showing the record highs and lows"""
    plt.title("Record Highs versus Record lows")
    left_edge = range(len(month))

    # Plotting two different lines - one for the highs and one for the lows
    plt.plot(left_edge, recordHighF, color=my_colors[2], marker='o', label='Record High')


    plt.plot(left_edge, recordLowF, color=my_colors[3], marker='o', label='Record Low')
    plt.xticks(left_edge, month)

    plt.xlabel("Months")
    plt.ylabel("Record High vs. Low")

    plt.grid(True)
    plt.legend()
    plt.show()

    greatest = max(recordHighF)
    i = recordHighF.index(greatest)
    print(f"The month with the highest value is: {month[i]}")

    smallest = min(recordLowF)
    s = recordLowF.index(smallest)
    print(f"The month with the lowest value is: {month[s]}")

    print(f"The average of all the values is:{(sum(recordHighF) + sum(recordLowF))/ 12}")


def plot4():
    """This function calculates the temperature ranges between the record highs and lows and then graphs it on a bar graph"""
    temperature_ranges = []

    # Calculating the ranges for grphing
    for i in range(len(recordHighF)):
        temp_range = recordHighF[i] - recordLowF[i]
        temperature_ranges.append(temp_range)

    plt.title("Temperature Ranges")

    # x values
    left_edge = range(len(month))
    bar_width = 0.5
    plt.bar(left_edge, temperature_ranges, bar_width,
             color=my_colors)

    plt.xticks(left_edge, month)

    plt.xlabel("Months")
    plt.ylabel("Total Difference")

    plt.grid(True)
    plt.show()

    greatest = max(temperature_ranges)
    i = temperature_ranges.index(greatest)
    print(f"The month with the highest value is: {month[i]}")

    smallest = min(temperature_ranges)
    s = temperature_ranges.index(smallest)
    print(f"The month with the lowest value is: {month[s]}")

    print(f"The average of the values is: {sum(temperature_ranges)/12}")


if __name__ == '__main__':
    file1()
    file2()
    plot1()
    plot2()
    plot3()
    plot4()

"""
REFLECTIONS:
GRAPH 1 and GRAPH 2:
This graph shows the average snowfall per month throughout the year. 
The trend I noticed is that the average snowfall steadily decreases as the weather gets warmer, 
which makes sense since it normally only snows when it is ver cold. 
What surprises me about the graph is that the month of April still shows an average amount of snowfall, 
even though snow it doesn't really snow during that time. This shows that occasionally there can be snow
in the early spring, even though it is uncommon. Overall, the graph highlights how closely snowfall 
patterns are connected to changes in temperature and to the seasons.

GRAPH 3:
This graph shows the record high temperatures compared to the record low temperatures throughout the year. 
One trend that I noticed is that the difference between the two temperatures gradually gets smaller as the 
months progress. Both of the curves follow a similar path, rising and falling around the same points in the year. 
One interesting detail I noticed is that the line for the low temperatures has a greater slope than the line for 
the high temperatures. This suggests that the low temperatures change more sharply between seasons, 
while the high temperatures remain more consistent.

GRAPH 4:
This graph shows which month has the largest temperature range. One trend I noticed is that the curve rises, 
dips in the middle, and then rises again. This pattern indicates that temperature differences are smallest 
during the summer months. It shows that summer days and nights have more consistent temperatures compared 
to other seasons. Overall, the graph highlights how temperature ranges are wider in colder months and 
narrower during warmer periods.

"""