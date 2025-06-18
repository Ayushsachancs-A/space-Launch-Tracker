import pandas as pd

isro_df = pd.read_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\Space Launch Tracker\Data\isro_data.csv")
spacex_df = pd.read_csv(r"C:\Users\imean\OneDrive\Desktop\projecttss\Space Launch Tracker\Data\space_x.csv")


launchpad_mapping = {
    "5e9e4502f5090995de566f86": "Cape Canaveral LC-40",
    "5e9e4501f509094ba4566f84": "Vandenberg SLC-4E",
    "5e9e4501f509094188566f88": "Kennedy LC-39A",
    "5e9e4501f509094354066f85": "Kwajalein Atoll",
    "5e9e4502f509092b78566f87": "Starbase Boca Chica"
}

isro_clean= pd.DataFrame()
isro_cleaned = pd.DataFrame()
isro_cleaned['mission_name'] = isro_df['Mission Name']
isro_cleaned['launch_date'] = pd.to_datetime(isro_df['Year'], errors='coerce').dt.strftime('%Y-01-01')  # Convert year to YYYY-01-01
isro_cleaned['launch_site'] = isro_df['Launch Site']
isro_cleaned['success'] = isro_df['Success Rate (%)'].apply(lambda x: True if x >= 50 else False)  # Convert to boolean
isro_cleaned['agency'] = 'ISRO'
isro_cleaned['mission_type'] = isro_df['Mission Type']

spacex_cleaned = pd.DataFrame()
spacex_cleaned['mission_name'] = spacex_df['name']
spacex_cleaned['launch_date'] = pd.to_datetime(spacex_df['date_utc'], errors='coerce').dt.date
spacex_cleaned['launch_site'] = spacex_df['launchpad'].map(launchpad_mapping)
spacex_cleaned['success'] = spacex_df['success']
spacex_cleaned['agency'] = 'SpaceX'
spacex_cleaned['launch_site'].fillna("Unknown", inplace=True)
spacex_cleaned['success'].fillna(False, inplace=True)  # Or leave as NaN for NULL
spacex_cleaned['mission_type'].fillna("N/A", inplace=True)

# --- Save Cleaned CSVs ---
isro_cleaned.to_csv('clean_isro.csv', index=False)
spacex_cleaned.to_csv('clean_spacex.csv', index=False)