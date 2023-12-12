
# CPICs pipeline workshop repository

This repository captures the developmental stage of the CPICs pipeline after a workshop with the CPICs team. The environment for this repository is managed using a virtual environment.

## Project Overview
This project facilitates the management of raw data, processing, and import into Ecotaxa, ease project management workflows. The entry point of the repository is `test_project.py`, which orchestrates the CPICsProject and associated functionalities.

### Project Workflow
The `test_project.py` script orchestrates the CPICs project workflow:
1. **Project Creation**: Creates a new CPICs project.
2. **Data Processing**: Copies raw data and processes it to generate TSV and vignette for export.
3. **Importing into Ecotaxa**: Imports processed data into Ecotaxa for further analysis.

### TODO
1. Allow to copy all or sync or juste add if new cast
2. Extract objid and sample id subsample id sample/subsample
3. Read geolocation by integrating castoverview.py tho the process.
4. Read sysLOG : Get image segmentation parameters found and the fps per minute by integarting readSysLog.py to the process.
5. Create architectue split_by_sample_and_subsample
6. Automatic import_in_ecotaxa

## Usage Notes
- Adjust the paths in the script according to your system setup.
- Ensure necessary permissions and configurations for the paths and file operations.
- You need do manually import the created project into EcoTaxa.

**Note**: This repository is in WIP stage and may not be realable.

## Running the Project

### Prerequisites
Python 3.7 or higher

### Setup

1. Clone this repository.
2. Navigate to the project directory.
3. Setup **raw_data_path** and **dest_data_path** in test_project.py
4. Create the virtual environment:
    ```
    python3 -m venv workshop_VENV
    ```
5. Activate the virtual environment:
    - For MacOS/Linux:
      ```
      source workshop_VENV/bin/activate
      pip install -r requirements
      ```
    - For Windows:
      ```
      workshop_VENV\Scripts\activate
      pip install -r requirements
      ```
6. Run the project:
    ```
    python3 test_project.py
    ```
