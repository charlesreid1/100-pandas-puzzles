# 100 pandas puzzles

### [Puzzles notebook](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles.ipynb)
### [Solutions notebook](https://github.com/ajcr/100-pandas-puzzles/blob/master/100-pandas-puzzles-with-solutions.ipynb)

Inspired by [100 Numpy exerises](https://github.com/rougier/numpy-100), here are 100* short puzzles for testing your knowledge of [pandas'](http://pandas.pydata.org/) power.

Since pandas is a large library with many different specialist features and functions, these excercises focus mainly on the fundamentals of manipulating data (indexing, grouping, aggregating, cleaning), making use of the core DataFrame and Series objects. Many of the excerises here are straightforward in that the solutions require no more than a few lines of code (in pandas or NumPy - don't go using pure Python!). Choosing the right methods and following best practices is the underlying goal.

The exercises are loosely divided in sections. Each section has a difficulty rating; these ratings are subjective, of course, but should be a seen as a rough guide as to how elaborate the required solution needs to be.

Good luck solving the puzzles!

*\* the list of puzzles is not yet complete! Pull requests or suggestions for additional exercises, corrections and improvements are welcomed.*

## Overview of puzzles

| Section Name  | Description |  Difficulty |
| ------------- | ------------- | ------------- |
| Importing pandas  | Getting started and checking your pandas setup  | Easy |
| DataFrame basics  | A few of the fundamental routines for selecting, sorting, adding and aggregating data in DataFrames  | Easy  |
| DataFrames: beyond the basics  | Slightly trickier: you may need to combine two or more methods to get the right answer  | Medium |
| DataFrames: harder problems  | These might require a bit of thinking outside the box...  | Hard |
| Series and DatetimeIndex  | Exercises for creating and manipulating Series with datetime data  | Easy/Medium |
| Cleaning Data  | Making a DataFrame easier to work with  | Easy/Medium |
| Using MultiIndexes  | Go beyond flat DataFrames with additional index levels  | Medium |
| Minesweeper | Generate the numbers for safe squares in a Minesweeper grid | Hard |
| Plotting | Explore pandas' part of plotting functionality to see trends in data | Medium |

## Setting up

To tackle the puzzles on your own computer, you'll need a Python 3 environment with the dependencies (namely pandas) installed.

One way to do this is as follows. I'm using a bash shell, the procedure with Mac OS should be essentially the same. Windows, I'm not sure about.

1. Check you have Python 3 installed by printing the version of Python:
```
python -V
```

2. Clone the puzzle repository using Git:

```
git clone https://github.com/ajcr/100-pandas-puzzles.git
```

3. Install the dependencies (**caution**: if you don't want to modify any Python modules in your active environment, consider using a virtual environment instead):

```
python -m pip install -r requirements.txt
```

4. Launch a jupyter notebook server:

```
jupyter notebook --notebook-dir=100-pandas-puzzles
```

You should be able to see the notebooks and launch them in your web browser.

## Contributors

This repository has benefitted from numerous contributors, with those who have sent puzzles and fixes listed in [CONTRIBUTORS](https://github.com/ajcr/100-pandas-puzzles/blob/master/CONTRIBUTORS.md).

Thanks to everyone who has raised an issue too.

## Puzzles

- [Problem 1](puzzles/problem_001.py) — Import pandas under the name `pd`.
- [Problem 2](puzzles/problem_002.py) — Print the version of pandas that has been imported.
- [Problem 3](puzzles/problem_003.py) — Print out all the version information of the libraries required by pandas.
- [Problem 4](puzzles/problem_004.py) — Create a DataFrame from a dictionary with a given index.
- [Problem 5](puzzles/problem_005.py) — Display a summary of the basic information about a DataFrame and its data.
- [Problem 6](puzzles/problem_006.py) — Return the first 3 rows of a DataFrame.
- [Problem 7](puzzles/problem_007.py) — Select just the 'animal' and 'age' columns from a DataFrame.
- [Problem 8](puzzles/problem_008.py) — Select the data in rows [3, 4, 8] and in columns ['animal', 'age'].
- [Problem 9](puzzles/problem_009.py) — Select only the rows where the number of visits is greater than 3.
- [Problem 10](puzzles/problem_010.py) — Select the rows where the age is missing, i.e. is NaN.
- [Problem 11](puzzles/problem_011.py) — Select rows where the animal is a cat and the age is less than 3.
- [Problem 12](puzzles/problem_012.py) — Select the rows where the age is between 2 and 4 (inclusive).
- [Problem 13](puzzles/problem_013.py) — Change the age in row 'f' to 1.5.
- [Problem 14](puzzles/problem_014.py) — Calculate the sum of all visits.
- [Problem 15](puzzles/problem_015.py) — Calculate the mean age for each different animal.
- [Problem 16](puzzles/problem_016.py) — Append a new row to a DataFrame, then delete it.
- [Problem 17](puzzles/problem_017.py) — Count the number of each type of animal.
- [Problem 18](puzzles/problem_018.py) — Sort by age descending, then by visits ascending.
- [Problem 19](puzzles/problem_019.py) — Replace 'yes'/'no' strings with boolean True/False.
- [Problem 20](puzzles/problem_020.py) — Change 'snake' entries to 'python' in the animal column.
- [Problem 21](puzzles/problem_021.py) — Create a pivot table of mean age by animal and number of visits.
- [Problem 22](puzzles/problem_022.py) — Filter out rows that contain the same integer as the row immediately above.
- [Problem 23](puzzles/problem_023.py) — Subtract the row mean from each element in the row.
- [Problem 24](puzzles/problem_024.py) — Find which column of numbers has the smallest sum.
- [Problem 25](puzzles/problem_025.py) — Count how many unique rows a DataFrame has.
- [Problem 26](puzzles/problem_026.py) — For each row, find the column containing the third NaN value.
- [Problem 27](puzzles/problem_027.py) — For each group, find the sum of the three greatest values.
- [Problem 28](puzzles/problem_028.py) — Group by bins of 10 consecutive integers and sum another column.
- [Problem 29](puzzles/problem_029.py) — Count the difference back to the previous zero in a Series.
- [Problem 30](puzzles/problem_030.py) — Find the row-column index locations of the 3 largest values.
- [Problem 31](puzzles/problem_031.py) — Replace negative values with the group mean.
- [Problem 32](puzzles/problem_032.py) — Implement a rolling mean over groups with window size 3, ignoring NaN.
- [Problem 33](puzzles/problem_033.py) — Create a DatetimeIndex of business days in 2015 and index a Series.
- [Problem 34](puzzles/problem_034.py) — Find the sum of values for every Wednesday.
- [Problem 35](puzzles/problem_035.py) — Find the mean of values for each calendar month.
- [Problem 36](puzzles/problem_036.py) — For each group of four consecutive months, find the date of the highest value.
- [Problem 37](puzzles/problem_037.py) — Create a DateTimeIndex of the third Thursday in each month for 2015–2016.
- [Problem 38](puzzles/problem_038.py) — Interpolate missing flight numbers and convert to integer column.
- [Problem 39](puzzles/problem_039.py) — Split a column of strings on an underscore into two columns.
- [Problem 40](puzzles/problem_040.py) — Standardise city name capitalisation so only the first letter is uppercase.
- [Problem 41](puzzles/problem_041.py) — Delete a column and attach a temporary DataFrame in its place.
- [Problem 42](puzzles/problem_042.py) — Extract airline names from strings with extra punctuation and symbols.
- [Problem 43](puzzles/problem_043.py) — Expand a column of lists into separate columns named delay_1, delay_2, etc.
- [Problem 44](puzzles/problem_044.py) — Construct a MultiIndex from the product of two lists and index a Series.
- [Problem 45](puzzles/problem_045.py) — Check that a MultiIndex is lexicographically sorted.
- [Problem 46](puzzles/problem_046.py) — Select specific labels from the second level of a MultiIndex.
- [Problem 47](puzzles/problem_047.py) — Slice a MultiIndexed Series on both levels.
- [Problem 48](puzzles/problem_048.py) — Sum values for each label in the first level of a MultiIndex.
- [Problem 49](puzzles/problem_049.py) — Perform a level-based sum without the level keyword argument.
- [Problem 50](puzzles/problem_050.py) — Swap MultiIndex levels and sort the result.
- [Problem 51](puzzles/problem_051.py) — Generate a DataFrame of every coordinate in a 5×4 Minesweeper grid.
- [Problem 52](puzzles/problem_052.py) — Add a column of random mines with probability 0.4.
- [Problem 53](puzzles/problem_053.py) — Compute the number of adjacent mines for each square.
- [Problem 54](puzzles/problem_054.py) — Set the adjacent count to NaN for squares that contain a mine.
- [Problem 55](puzzles/problem_055.py) — Convert the DataFrame to a grid of adjacent mine counts.
- [Problem 56](puzzles/problem_056.py) — Make a scatter plot with black X markers.
- [Problem 57](puzzles/problem_057.py) — Make a scatter plot incorporating four DataFrame features via color and size.
- [Problem 58](puzzles/problem_058.py) — Make a bar plot of revenue with a line plot of advertising on a secondary axis.
- [Problem 59](puzzles/problem_059.py) — Generate random stock data and aggregate to hourly OHLC summaries.
- [Problem 60](puzzles/problem_060.py) — Plot a candlestick chart from OHLC stock data.
- [Problem 61](puzzles/problem_061.py) — For each unique value in a column, find the row index of the maximum in another column.
- [Problem 62](puzzles/problem_062.py) — Compute a running cumulative maximum of a column.
- [Problem 63](puzzles/problem_063.py) — Rank scores in descending order with ties receiving the same rank.
- [Problem 64](puzzles/problem_064.py) — Extract numeric digits from strings and return as integers.
- [Problem 65](puzzles/problem_065.py) — Replace values above the column mean with 'high' and others with 'low'.
- [Problem 66](puzzles/problem_066.py) — Find the row with the most recent date for each group.
- [Problem 67](puzzles/problem_067.py) — Compute the percentage change between each row and the previous row.
- [Problem 68](puzzles/problem_068.py) — Perform an outer merge and fill resulting NaN values with 0.
- [Problem 69](puzzles/problem_069.py) — Split comma-separated values into separate rows.
- [Problem 70](puzzles/problem_070.py) — Bin values into quartiles and label them Q1–Q4.
- [Problem 71](puzzles/problem_071.py) — Convert datetime strings and extract the day of the week name.
- [Problem 72](puzzles/problem_072.py) — Pivot a DataFrame from long to wide format and melt it back.
- [Problem 73](puzzles/problem_073.py) — Forward-fill NaN values within each group independently.
- [Problem 74](puzzles/problem_074.py) — Number each row within its group.
- [Problem 75](puzzles/problem_075.py) — Compute the z-score for each value in a numeric column.
- [Problem 76](puzzles/problem_076.py) — Compute the Euclidean distance between two Series.
- [Problem 77](puzzles/problem_077.py) — Find all columns where more than 25% of values are NaN.
- [Problem 78](puzzles/problem_078.py) — Create a word count column from a column of text.
- [Problem 79](puzzles/problem_079.py) — Find duplicate rows and their counts.
- [Problem 80](puzzles/problem_080.py) — Compute each value as a percentage of its category's total.
- [Problem 81](puzzles/problem_081.py) — Compute a rolling sum with a window of 3.
- [Problem 82](puzzles/problem_082.py) — Transpose a DataFrame so rows become columns.
- [Problem 83](puzzles/problem_083.py) — Find the length of lists in a column and filter by length.
- [Problem 84](puzzles/problem_084.py) — Extract year, month, day, hour, and minute from a timestamp column.
- [Problem 85](puzzles/problem_085.py) — Perform a left join and identify unmatched rows using an indicator.
- [Problem 86](puzzles/problem_086.py) — Normalize all values to 0–1 using min-max normalization.
- [Problem 87](puzzles/problem_087.py) — Apply multiple aggregation functions to a grouped column.
- [Problem 88](puzzles/problem_088.py) — Find all rows where a string matches an email address pattern.
- [Problem 89](puzzles/problem_089.py) — Shift a column and compute the difference (manual diff).
- [Problem 90](puzzles/problem_090.py) — Flatten a hierarchical column MultiIndex by joining level names.
- [Problem 91](puzzles/problem_091.py) — Replace outliers (>2 std from mean) with the column mean.
- [Problem 92](puzzles/problem_092.py) — Create a cross-tabulation of two categorical columns.
- [Problem 93](puzzles/problem_093.py) — Pad strings with leading zeros to a fixed width.
- [Problem 94](puzzles/problem_094.py) — Find the pair of columns with the highest absolute correlation.
- [Problem 95](puzzles/problem_095.py) — Resample to weekly frequency and compute sum and count.
- [Problem 96](puzzles/problem_096.py) — Use apply to return the data type of each column.
- [Problem 97](puzzles/problem_097.py) — Compute an exponentially weighted moving average with span 3.
- [Problem 98](puzzles/problem_098.py) — Filter rows using isin and its negation.
- [Problem 99](puzzles/problem_099.py) — Create a column with the element-wise maximum of two columns.
- [Problem 100](puzzles/problem_100.py) — Write a DataFrame to CSV, read it back, and verify equality.

## Other links

If you feel like reading up on pandas before starting, the official documentation useful and very extensive. Good places get a broader overview of pandas are:

- [10 minutes to pandas](http://pandas.pydata.org/pandas-docs/version/0.17.0/10min.html)
- [pandas basics](http://pandas.pydata.org/pandas-docs/version/0.17.0/basics.html)
- [tutorials](http://pandas.pydata.org/pandas-docs/stable/tutorials.html)
- [cookbook and idioms](http://pandas.pydata.org/pandas-docs/version/0.17.0/cookbook.html#cookbook)
- [Guilherme Samora's pandas exercises](https://github.com/guipsamora/pandas_exercises)

There are may other excellent resources and books that are easily searchable and purchaseable.
