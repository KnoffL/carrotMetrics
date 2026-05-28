# carrotMetrics
A reporting tool for tracking carrot quality - or anything really ;)

I did not use AI in this project. That does not mean that this project is of higher quality than my other projects (probably quite the opposite), but I believe in also making sure one can still code a little without AI. This is me making sure of that.

So far, the project fetches data from a csv file or returns an empty data frame if the file does not exist. There is also a function (addSupermarket()) to add and save new data to the data frame, as well as a function (addColumn()) to add a new attribute to the data frame along with a default value that is then applied to all pre-existing rows.
However, there are no tests in this project yet.

Dependencies:
pandas (imported as pd)