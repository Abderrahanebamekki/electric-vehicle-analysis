# Electric Vehicle Population Analysis

Data cleaning and dashboard project using Python and Power BI.
Master 1 SDSI, Advanced Business Intelligence module (University of Constantine 2).

## What I did
- Downloaded the real Electric Vehicle Population dataset (CSV) from [data.gov](https://catalog.data.gov/dataset/electricvehicle-population-data)
- Cleaned it with Python (pandas): removed missing values and duplicates
- Split it into 3 clean tables: `dim_vehicle`, `dim_location`, `fact_table`
- Built a Power BI dashboard from those tables

## Tools
Python (pandas), Power BI, CSV

## Project files
| File | Description |
|------|-------------|
| `clean_data.py` | Python cleaning script |
| `data/` | Clean CSV files |
| `dashboard.pbix` | Power BI dashboard |
| `images/` | Dashboard screenshots |
| `BIA.pdf` | Full project report |

## Results
- Electric vehicles (BEV) are the majority compared to plug-in hybrids (PHEV)
- King County has the most vehicles
- Average electric range is higher in hot regions than cold regions

![Dashboard](images/dashboard.png)

## Author
Bamekki Abderrahmane
[LinkedIn](https://www.linkedin.com/in/bamekki-abderrahmane-a372a940b/) | [GitHub](https://github.com/Abderrahanebamekki)
