import argparse
from constants import *
import math
import matplotlib.pyplot as plt
import pandas as pd

from debug_tools import functionLogger





# Parent class will allow weather and soccer parser derived classes to find the finimum span.  The arguments 
# to the read_csv() functino in pandas are passed in but not by user through a dictionary defined in the config 
# file.
# - findMinSpan():
#   ---- Inputs ----
#   None
#   ---- Outputs ----
#   stores minimum span and the id to class member variable for later use
#
# - finalOutput()
#   ---- Inputs ----
#   boolean flag that indicates if the result is plotted using matplotlib
#   ---- Outputs ----
#   prints the minimum span and its ID to STDOUT
#
# - plotOutput()
#   ---- Inputs ----
#   None
#   ---- Outputs ----
#   Plot of bounds of the data is generated
#############################################################################################################
class MinSpanDataParser():
    # arguments are stored to read in data with pandas read_csv in derived classes
    @functionLogger
    def __init__(self, arguments):
        self.arguments = arguments

    # both derived classes use this same find minimum span function
    @functionLogger
    def findMinSpan(self):
        self.minimum_span_id = None
        self.minimum_span = math.inf
        self.low=None
        self.high=None
        for _, row in self.df.iterrows():
            span = abs(row[BOUND1] - row[BOUND2])
            if span < self.minimum_span:
                self.minimum_span = span
                self.minimum_span_id = row[ID]
                self.low=row[BOUND1]
                self.high=row[BOUND2]
         

    # Out put will always print results to terminal and have the option to print to an output file
    # and also has the option to display a graph
    @functionLogger
    def finalOutput(self, plot_ouput):
        print(self.minimum_span_id, self.minimum_span)

        if plot_ouput:
            self.plotOutput()

    # plot is conditional 
    @functionLogger
    def plotOutput(self):
        print("plotted")
        fig, ax = plt.subplots( nrows=1, ncols=1, figsize = (10,5) ) 
        ax.set_title(self.plot_title) # Setting the title
        ax.set_ylabel(self.plot_y)
        ax.set_xlabel(self.plot_x)
        ax.yaxis.grid() # Setting up the horizontal grid lines in the background

        u = plt.plot(self.df[ID], self.df[BOUND1], '#FF9100', linewidth = 1, alpha=0.75, label = self.upper)
        l = plt.plot(self.df[ID], self.df[BOUND2], '#80D8FF', linewidth = 1, alpha=0.75, label = self.lower)
        plt.fill_between(self.df[ID], self.df[BOUND1], self.df[BOUND2], facecolor='#EEEEEE')
        plt.plot((self.minimum_span_id, self.minimum_span_id), (self.high, self.low), 'r', label = MIN_LABEL)
        plt.legend(loc = 1).get_frame().set_edgecolor('white') 

        if self.dataset == SOCCER:
            plt.xticks(self.df[ID], ha='right', rotation=45)
            plt.gcf().subplots_adjust(bottom=0.25)
        plt.show()





# Soccer class has a string ID and integer bounds.  Extends MinSpanDataParser to inhereit findMinSpan()
# - parseDataSet():
#   ---- Inputs ----
#   None
#   ---- Outputs ----
#   stores cleaned data into the member variable 'df'
#############################################################################################################
class SoccerParser(MinSpanDataParser):
    @functionLogger
    def __init__(self, arguments):
        super(SoccerParser, self).__init__(arguments)
        self.dataset = SOCCER
        self.plot_x = SOCCER_X
        self.plot_y = SOCCER_Y
        self.plot_title = SOCCER_TITLE
        self.upper = SOCCER_UPPER_LABEL
        self.lower = SOCCER_LOWER_LABEL
    
    @functionLogger
    def parseDataSet(self):
        # print("soccer")
        self.df = pd.read_csv(**self.arguments)
        self.df.rename(inplace=True, columns={1: ID, 6: BOUND1, 8: BOUND2}) # columns are given names for easier access
        self.df[[BOUND1, BOUND2]] = self.df[[BOUND1, BOUND2]].apply(pd.to_numeric)






# Weather class has int ID and int bounds.  Extends MinSpanDataParser to inhereit findMinSpan()
# - parseDataSet():
#   ---- Inputs ----
#   None
#   ---- Outputs ----
#   stores cleaned data into the member variable 'df'
#############################################################################################################
class WeatherParser(MinSpanDataParser):
    @functionLogger
    def __init__(self, arguments):
        super(WeatherParser, self).__init__(arguments)
        self.dataset = WEATHER
        self.plot_x = WEATHER_X
        self.plot_y = WEATHER_Y
        self.plot_title = WEATHER_TITLE
        self.upper = WEATHER_UPPER_LABEL
        self.lower = WEATHER_LOWER_LABEL

    @functionLogger
    def parseDataSet(self):
        # print("weather")
        self.df = pd.read_csv(**self.arguments)
        self.df.rename(inplace=True, columns={0: ID, 1: BOUND1, 2: BOUND2}) # columns are given names for easier access
        self.df=self.df.replace('\*','',regex=True)
        self.df[[ID, BOUND1, BOUND2]] = self.df[[ID, BOUND1, BOUND2]].apply(pd.to_numeric) 

 




#################################################################################################################################
# The program can perform both the both tasks for the two data sets using the same code thanks to OOP.
# Both program executions on the data have the ability to provide output to a file and to display graphs of the 
# datasets because decorators can deck out the processing functions to do multiple different things.
# Admittidly, graphs and output files are not required but they are a great way to show how decorators can be used
# in data science.
@functionLogger
def main():
    
    # First the CLI args are parsed.  the soccer data set and the weather data set can only be processed one at a time in a
    # program execution.  This is not necessary and the program could run both tasks in the same execution, however, i thought
    # the readability of the code would be better if only 1 was being run at a time. 
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-s', '--soccer', action='store_true', help='Find team with points scored For:Against ratio closest to 1')
    group.add_argument('-w', '--weather', action='store_true', help='Find day with the smallest temperature spread')
    
    parser.add_argument('-g', '--graph', action='store_true', help='Include a graph in final result')
    parser.add_argument('-c', '--clearlog', action='store_true', help='Clear that messy output log before running the script')
    # parser.add_argument('-o', '--outfile', action='store_true', help='Output results to a file')

    args = parser.parse_args()

    # The user has the option to clear the log before running the script to get a better look under the hood
    if args.clearlog:
        with open('debug.log', 'w'):
            pass

    # The data parser is initialized depending on the user input specifying which dataset to process.  If no arguments are passed,
    # the initializer will default to processing the first task; the Weather dataset.  Only the columns that are needed are
    # extracted from the dataset.  In both cases, this is only 3 columns.
    if args.soccer:
        # data_parser = MinSpanDataParser(data=SOCCER)
        data_parser = SoccerParser(SOCCER_ARGS)
    elif args.weather:
        # data_parser = MinSpanDataParser(data=WEATHER)
        data_parser = WeatherParser(WEATHER_ARGS)
    else:
        data_parser = WeatherParser(WEATHER_ARGS) # Default is Weather Dataset

    # Both tasks are very similar and can be run using the same function.  The find the minimum difference of columns 1 and 2 (0 indexed)
    # First both data sets are parsed into 3 columns: The Identifier, and two value columns
    data_parser.parseDataSet()

    # Main processing and task execution
    data_parser.findMinSpan()

    # Finally print the output and create output file and display graphs (if applicable)
    data_parser.finalOutput(args.graph)






# file is importable or can be ran directly from this file
if __name__ == "__main__":
    main()

