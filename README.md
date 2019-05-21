# data_extraction
This project is a simple data extraction program for two datasets, showcasing my understanding of OOP, inheritance and polymorphic concepts, data manipulation and visualization, testing, and good coding practices over all.  Written in python but most concepts such as decorators, OOP, overloading, and testing, I can transfer over into languages C, C++, Java and JavaScript.  I hope you enjoy.

## Backgroud and Program Description
This program has the ability to open both the soccer data file and the weather data file using their own parsing classes inhereted from a minimum parsing base class which provides the functionality to calculate the datas minimum spreads in column 1 and 2 (0 indexed). It also has the ability to calculate minimum spreads of other datasets simply by creating the dataset's own parsing class that inherits the minimum spread function and calling the `findMinSpan()` function.  By using Pandas, data frame parsing and slicing is made very easy and straight forward.  Any newly created parsing classes should implement a `parseDataSet()` and store into `self.df` a data frame that is composed of 3 columns: `0: The Identifier`, `1: Bound 1`, and `2: Bound 2`.  If these constraints are adhered to, then this program is very useful in finding minimum spreads across many datasets and over many columns.

The program also provides the capability to log function execution specifics such as functions that ran and the class they ran from and the times they were executed.  Additionally, the user can specify to plot the output using `matplotlib` functionality.


## Program execution

### Run Soccer Dataset 
The program has the ability to run both tasks (minimum spread for weather and soccer) at the same time but I chose to make the functions mutually exclusive to make the code more readable.  To find the minimum spread of the `soccer` data set, run:

`python3 min_span.py -s`


### Run Weather Dataset
To find the minimum spread of the `weather` run the following command:

`python3 min_span.py -s`


### Clear Logging Output
The `min_span.py` script logs during exection all of functions that ran and the classes that they are members of.  The user has the option to clear `debug.log` file by including the cli flag `-c`.  For example, the following output will clear the log file, run the minimum span for the soccer dataset and then store the ouput in a fresh `debug.log` file.  T

`python3 min_span.py -s -c`

### Plot the Output
This program gives the user the option of graphing the output of both datasets (separately) using `matplotlib` using the following command:

`python3 min_span.py -s -g`
or
`python3 min_span.py -w -g`


### Other Execution Possibilities
The following commands are also possible to both graph the output and clear the log file:

`python3 min_span.py -s -g -c`
or
`python3 min_span.py -w -g -c`

The following commands are not possible and the compiler will complain as execution of the soccer dataset and the weather dataset is not currently accepted and they are treated as mutually exclusive command flags:

`python3 min_span.py -s -w -c`
or
`python3 min_span.py -w -s -g`
