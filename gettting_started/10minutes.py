import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20200101", periods=6)
print(dates)

rn = np.random.randn(2, 3)
print(rn)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))