
$ '"C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\powershell.exe" -Command "@'"'"'
# rs-conservation-py

Python scripts for remote sensing image processing and statistical analysis in conservation workflows.

## Contents
- "'"'"'`scripts/` – standalone analysis scripts
- `data/` – small sample data (optional)
- `outputs/` – generated figures/tables (optional)

## Requirements
- Python 3.10+
- Common geospatial stack (e.g., rasterio, numpy, geopandas)

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
Scripts are designed to run directly:
```bash
python scripts/compute_global_percentiles.py
```

## Notes
- Large datasets are not stored in this repository.
- Paths in scripts may need to be updated for your machine.

## License
MIT 
'"'"'"'"'"'@ | Set-Content -Encoding ASCII README.md"'
