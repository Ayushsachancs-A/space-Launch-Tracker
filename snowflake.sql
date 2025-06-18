CREATE OR REPLACE DATABASE space

USE DATABASE space


--File format
CREATE OR REPLACE FILE FORMAT csv_format
TYPE = 'CSV'
FIELD_OPTIONALLY_ENCLOSED_BY ='"'
SKIP_HEADER =1
ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE;


--Storage Integration
CREATE OR REPLACE STORAGE INTEGRATION my_S3_integration
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED= TRUE
STORAGE_AWS_ROLE_ARN = 'YOUR ROLE ARN'
STORAGE_ALLOWED_LOCATIONS=('s3://space-data/');

DESC INTEGRATION my_s3_integration;


--Create Stage for Data 
CREATE OR REPLACE STAGE s3_isro_stage
URL = 's3://space-data/isro'
STORAGE_INTEGRATION = my_s3_integration
FILE_FORMAT = csv_format;

CREATE OR REPLACE STAGE s3_spacex_stage
URL = 's3://space-data/spacex'
STORAGE_INTEGRATION = my_s3_integration
FILE_FORMAT = csv_format;


--Create Table
CREATE OR REPLACE TABLE isro_missions (
  mission_name STRING,
  launch_date DATE,
  launch_site STRING,
  success STRING,
  agency STRING,
  mission_type STRING
);

CREATE OR REPLACE TABLE spacex_missions (
  mission_name STRING,
  launch_date DATE,
  launch_site STRING,
  success STRING, 
  agency STRING,
  mission_type STRING
);


-- Load data from s3 to snowflake Table

COPY INTO isro_missions
FROM @s3_isro_stage
FILE_FORMAT = (FORMAT_NAME = csv_format)
ON_ERROR= 'skip_file';

COPY INTO spacex_missions
FROM @s3_spacex_stage
FILE_FORMAT = (FORMAT_NAME = csv_format)
ON_ERROR = 'skip_file';



--Merge Both table
CREATE OR REPLACE VIEW unified_missions AS
SELECT
  mission_name,
  launch_date,
  launch_site,
  success , 
  agency ,
  mission_type
FROM isro_missions

UNION ALL

SELECT
  mission_name,
  launch_date,
  launch_site,
  success , 
  agency ,
  mission_type
FROM spacex_missions;



-- count of mission per agency
SELECT agency, COUNT(*) AS total_missions
FROM unified_missions
GROUP BY agency;


--Success rate by agency
SELECT
  agency,
  COUNT(*) AS total_missions,
  COUNT_IF(LOWER(success) = 'true') AS successful_missions,
  ROUND(
    100.0 * COUNT_IF(LOWER(success) = 'true') / COUNT(*),
    2
  ) AS success_rate_percent
FROM unified_missions
GROUP BY agency;


--year wise Launch count
SELECT
  YEAR(launch_date) AS year,
  agency,
  COUNT(*) AS launches
FROM unified_missions
GROUP BY year, agency
ORDER BY year;







