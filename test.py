from volatility import volest
from volatility import data

# data
symbol = 'JPM'
bench = '^GSPC'
data_file_path = 'tests/JPM.csv'
bench_file_path = 'tests/BENCH.csv'
estimator = 'GarmanKlass'


# estimator windows
window = 30
windows = [30, 60, 90, 120]
quantiles = [0.25, 0.75]
bins = 100
normed = True

# use the yahoo helper to correctly format data from finance.yahoo.com
jpm_price_data = data.yahoo_helper(symbol, data_file_path)
spx_price_data = data.yahoo_helper(bench, bench_file_path)

# initialize class
vol = volest.VolatilityEstimator(
    price_data=jpm_price_data,
    estimator=estimator,
    bench_data=spx_price_data
)

# call plt.show() on any of the below...
_, plt = vol.cones(windows=windows, quantiles=quantiles)
_, plt = vol.rolling_quantiles(window=window, quantiles=quantiles)
_, plt = vol.rolling_extremes(window=window)
_, plt = vol.rolling_descriptives(window=window)
_, plt = vol.histogram(window=window, bins=bins, normed=normed)

_, plt = vol.benchmark_compare(window=window)
_, plt = vol.benchmark_correlation(window=window)
plt.show()