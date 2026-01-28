import rasterio
import numpy as np

raster_path = r"C:\Users\....\RZSM_NOAH_legacy_2000_2012_clim12_AOI.tif"

with rasterio.open(raster_path) as ds:
    arr = ds.read(7).astype("float64")   # change to specific month, for instance (7) = July, or leave blank to compute across all months
    nodata = ds.nodata

print("ds.nodata:", nodata)
print("Shape:", arr.shape)
print("NaN count:", np.isnan(arr).sum())

# Build a clean "valid values" mask:
mask = np.ones(arr.shape, dtype=bool)

# 1) remove NaNs
mask &= ~np.isnan(arr)

# 2) remove explicit nodata (if defined)
if nodata is not None:
    mask &= (arr != nodata)

values = arr[mask]

print("Valid count:", values.size)
print("Min/Max/Mean:", values.min(), values.max(), values.mean())

p5  = np.percentile(values, 5)
p50 = np.percentile(values, 50)
p95 = np.percentile(values, 95)

print("P5 :", p5)
print("P50:", p50)
print("P95:", p95)
