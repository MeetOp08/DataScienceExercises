# Data Science Exercises

Today’s exercise for the data science batch on analyzing Rainfall in India.

## Dataset
**Source**: [Rainfall India](https://www.data.gov.in/catalog/rainfall-india)

## Exercise Objectives

The `Exe1.py` script implements the following NumPy operations on the rainfall dataset:

- Load the rainfall CSV using `np.genfromtxt()`.
- Print the `type()` of the loaded NumPy object.
- Print its `shape`, `ndim`, `size`, and `dtype`.
- Print the first 5 records.
- Print the last 5 records.
- Access the rainfall record at index 0.
- Access the rainfall record at index 5.
- Access the last rainfall record using negative indexing.
- Slice and display the first 10 records.
- Slice and display records from index 10 to 20.
- Display every second record using slicing.
- Display the records in reverse order.
- Extract the annual rainfall column into a separate NumPy array.
- Add 100 to every value in the annual rainfall array.
- Multiply every annual rainfall value by 2.
- Divide every annual rainfall value by 2.
- Calculate the difference between the rainfall of two selected years.
- Calculate the average annual rainfall using `np.mean()`.
- Find the highest annual rainfall using `np.max()`.
- Find the lowest annual rainfall using `np.min()`.
- Find the total annual rainfall using `np.sum()`.
- Find the median annual rainfall using `np.median()`.
- Find the standard deviation using `np.std()`.
- Find the variance using `np.var()`.
- Find the index of the year having the highest rainfall using `np.argmax()`.
- Find the index of the year having the lowest rainfall using `np.argmin()`.
- Sort the annual rainfall values from lowest to highest using `np.sort()`.
- Create a copy of the annual rainfall array using `.copy()`, modify the copy, and check the original.
- Create a slice of the annual rainfall array and modify the slice. Check whether the original array is affected.
- Randomly select 5 rainfall values from the dataset using `np.random.choice()`.
