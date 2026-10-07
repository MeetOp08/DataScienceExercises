import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))

csv_file = os.path.join(
    folder,
    "agriculture_rainfall_yield.csv"
)

print("CSV location:")
print(csv_file)

data = np.genfromtxt(
    csv_file,
    delimiter=",",
    names=True,
    dtype=None,
    encoding="utf-8"
)


# print(type(data))
# print(data.dtype.names)

rainfall_data = data['rainfall_mm']
yield_data = data['yield_t_ha']


# print(rainfall_data)
# print(yield_data)

print(rainfall_data.shape)
print(yield_data.shape)

# print(rainfall_data.size)
# print(yield_data.size)

rainfall_reshape = rainfall_data.reshape(20,10)
yield_reshape=yield_data.reshape(20,10)

# print(rainfall_reshape)
# print(yield_reshape)


#   1. Average rainfall per district and per year.
avg = np.mean(rainfall_reshape,axis = 1)
print('Average rainfall per district and per year:',avg)
#   2. Z-score of the yearly state-average rainfall. Mark years with z below −1 as drought years.
year_avg = np.mean(rainfall_reshape,axis = 0)
mean = np.mean(year_avg)
std = np.std(year_avg)
z_score = (year_avg - mean) / std
print('Z-score of the yearly state-average rainfall',z_score)
#   3. Fit yield = a × rain + b with np.polyfit over all 200 points. Report slope, correlation r and r².
rainfall_flat = rainfall_data.flatten()
yield_flat = yield_data.flatten()

print("Rainfall shape:", rainfall_flat.shape)
print("Yield shape:", yield_flat.shape)

a, b = np.polyfit(
    rainfall_flat,
    yield_flat,
    1
)

print("\nSlope:", a)
print("Intercept:", b)

correlation_matrix = np.corrcoef(
    rainfall_flat,
    yield_flat
)

print("\nCorrelation matrix:")
print(correlation_matrix)


r = correlation_matrix[0, 1]

print("\nCorrelation r:", r)


r_squared = r ** 2

print("R²:", r_squared)
#   4. Predict yield for rainfall of 500, 800 and 1100 mm.
rain_values = np.array([500, 800, 1100])

predicted_yield = a * rain_values + b

print("Rainfall:", rain_values)
print("Predicted yield:", predicted_yield)

for rain, yield_prediction in zip(
    rain_values,
    predicted_yield
):
    print(
        rain,
        "mm ->",
        yield_prediction,
        "t/ha"
    )
#   5. List districts whose yield fell by more than 25% in a drought year compared with the year before.
drought_years = np.where(z_score < -1)[0]
print("\nDistricts whose yield fell by >25% in a drought year compared to the year before:")

for year in drought_years:
    if year == 0:
        continue
    
    prev_yield = yield_reshape[:, year - 1]
    curr_yield = yield_reshape[:, year]
    
    drop_pct = (prev_yield - curr_yield) / prev_yield
    affected_districts = np.where(drop_pct > 0.25)[0]
    
    # Adding 1 to make district numbers 1-indexed
    print(f"  - In drought year {year}: Districts {affected_districts + 1}")
