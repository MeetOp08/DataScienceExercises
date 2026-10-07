# PROBLEM 1: Rainfall and crop yield (Agriculture, Level 1 · Foundation, 60 min)

A state agriculture department has ten years of rainfall and yield records for 20 districts. It needs to know how strongly yield depends on rain and which years were droughts, before it sets crop insurance rates.

**FILES:** agriculture_rainfall_yield.csv

## DATA NOTES
- **rainfall:** (20, 10) mm. Normal with mean 800 and std 150, from default_rng(2). Rows are districts, columns are years.
- **drought years:** Years with index 3 and 7: multiply that column of rainfall by 0.6.
- **yield_t_ha:** 1.2 + 0.0025 × rainfall plus normal noise (mean 0, std 0.25). Compute it after the drought step.

## NUMPY TASKS
1. Average rainfall per district and per year.
2. Z-score of the yearly state-average rainfall. Mark years with z below -1 as drought years.
3. Fit yield = a × rain + b with np.polyfit over all 200 points. Report slope, correlation r and r².
4. Predict yield for rainfall of 500, 800 and 1100 mm.
5. List districts whose yield fell by more than 25% in a drought year compared with the year before.
