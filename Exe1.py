import numpy as np
import random

data = np.genfromtxt(
    "Sub_Division_IMD_2017.csv",
    delimiter=",",
    skip_header=1,
    dtype=[
        ("subdivision", "U50"),
        ("year", "i4"),
        ("jan", "f8"),
        ("feb", "f8"),
        ("mar", "f8"),
        ("apr", "f8"),
        ("may", "f8"),
        ("jun", "f8"),
        ("jul", "f8"),
        ("aug", "f8"),
        ("sep", "f8"),
        ("oct", "f8"),
        ("nov", "f8"),
        ("dec", "f8"),
        ("annual", "f8"),
        ("jan_feb", "f8"),
        ("mar_may", "f8"),
        ("jun_sep", "f8"),
        ("oct_dec", "f8")
    ],
    encoding="utf-8"
)

print("Data type:", type(data))
print("Data shape:", data.shape)
print("Data ndim:", data.ndim)
print("Data size:", data.size)
print("Data dtype:", data.dtype)

print("Top 5 records of data:", data[:5])
print("Bottom 5 records of data:", data[-5:])
print("0 Index record of data:", data[0])
print("5 Index record of data:", data[5])
print("Last record using negative indexing:", data[-1])

print("First 10 records of data:", data[:10])
print("10 to 20 records of data:", data[10:20])
print("Every 2nd record of data:", data[::2])
print("Reverse order of records of data:", data[::-1])

annual = data["annual"]

print("\nAnnual rainfall:", annual)
print("Add 100 to annual rainfall:", annual + 100)
print("Multiply annual rainfall by 2:", annual * 2)
print("Divide annual rainfall by 2:", annual / 2)
print("Difference between rainfall of two selected years:", annual[1] - annual[0])

print("Calculate the average annual rainfall using np.mean():", np.mean(annual))
print("max:", np.max(annual))
print("min:", np.min(annual))
print("sum:", np.sum(annual))
print("median:", np.median(annual))
print("std:", np.std(annual))
print("var:", np.var(annual))

print("argmax :", np.argmax(annual))
print("argmin:", np.argmin(annual))
print("sort :", np.sort(annual))

copy_annual = np.copy(annual)
copy_annual[0] = 99999
print("Original annual array after modifying copy (should remain unchanged):", annual[0])
print("Copy after modification:", copy_annual[0])

# Create a slice of the annual rainfall array and modify the slice. Check whether the original array is affected.
slice_annual = annual[1:4]
slice_annual[0] = 1000
print("Original array after modifying slice (index 1 should be 1000):", annual[1])
print("slice after modification:", slice_annual)

random_values = np.random.choice(annual, size=5, replace=False)
print("Randomly select 5 records from the data array:", random_values)
