import rasterio
import numpy as np

raster_path = r"C:\Users\....RZSM_NOAH_anomaly_recent_2013_2024_minus_legacy_2000_2012_clim12_AOI.tif"

# Optional: set month band (1–12). Leave as None to compute across all months.
month_band = None  # e.g. 7 for July, or None for all bands

with rasterio.open(raster_path) as ds:
    nodata = ds.nodata

    if month_band is None:
        arr = ds.read().astype("float64")      # shape: (bands, rows, cols)
        label = "ALL bands"
    else:
        arr = ds.read(month_band).astype("float64")  # shape: (rows, cols)
        label = f"Band {month_band}"

print("Raster:", raster_path)
print("Read:", label)
print("ds.nodata:", nodata)
print("Shape:", arr.shape)

# Build valid mask
valid = ~np.isnan(arr)

# Remove explicit nodata (only meaningful if nodata is not NaN)
if nodata is not None and not (isinstance(nodata, float) and np.isnan(nodata)):
    valid &= (arr != nodata)

values = arr[valid]

print("Valid count:", values.size)
print("Min/Max/Mean:", float(values.min()), float(values.max()), float(values.mean()))

p5  = float(np.percentile(values, 5))
p50 = float(np.percentile(values, 50))
p95 = float(np.percentile(values, 95))

# Symmetric scaling for diverging anomaly maps
limit = max(abs(p5), abs(p95))
vmin = -limit
vmax =  limit

print("P5 :", p5)
print("P50:", p50)
print("P95:", p95)
print("Suggested QGIS scale (symmetric):")
print("  Min (vmin):", vmin)
print("  Max (vmax):", vmax)
