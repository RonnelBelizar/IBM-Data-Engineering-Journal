# Topic: Module 1 - ETL

# 🛠️ Data Engineering Notes: ETL Basics

## ETL (Extract, Transform, Load)
The process of **extracting** data from sources, **transforming** it into a usable format, and **loading** it into a target system (database, data warehouse, etc.).  

### Basic ETL Components

**1. `glob` function**  
- Used to **retrieve files** from a directory matching a pattern (e.g., all `.csv` files).  
- Example:
    ```python
    import glob
    files = glob.glob("/data/*.csv")
    ```

**2. `datestamp` function**  
- Adds a **timestamp** to files or logs to track processing times or versions.  
- Example:
    ```python
    from datetime import datetime
    datestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"output_{datestamp}.csv"
    ```

**3. `logging` function**  
- Tracks **ETL process events**, errors, or important milestones.  
- Example:
    ```python
    import logging
    logging.basicConfig(level=logging.INFO, filename='etl.log')
    logging.info("ETL process started")
    logging.error("Error loading file")
    ```

### Simple Example: Basic ETL Pipeline
```python
import glob
import pandas as pd
from datetime import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, filename='etl.log')
logging.info("ETL process started")

# Extract: get all CSV files
files = glob.glob("data/*.csv")
all_data = []

for file in files:
    logging.info(f"Processing {file}")
    df = pd.read_csv(file)
    
    # Transform: simple example - add datestamp column
    df['datestamp'] = datetime.now().strftime("%Y-%m-%d")
    all_data.append(df)

# Load: combine all data and save to output CSV
final_df = pd.concat(all_data, ignore_index=True)
output_file = f"output_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv"
final_df.to_csv(output_file, index=False)
logging.info(f"ETL process finished, saved to {output_file}")

