# Space Launch Tracker

A comprehensive space launch tracking application that monitors and analyzes launch data from  agencies like SpaceX and ISRO.

## Project Structure

```
Space Launch Tracker/
├── Dashboard/          # Streamlit dashboard application
├── Data/              # Data files and datasets
├── ETL/               # Data extraction, transformation, and loading scripts
├── venv311/           # Python virtual environment (ignored by git)
└── requirements.txt   # Python dependencies
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd "Space Launch Tracker"
```

### 2. Create Virtual Environment
```bash
python -m venv venv311
# On Windows:
venv311\Scripts\activate
# On macOS/Linux:
source venv311/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables Setup

Create a `.env` file in the root directory with the following variables:

```env
# AWS Configuration
AWS_ACCESS_KEY_ID=your_aws_access_key_here
AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key_here
AWS_REGION=your_aws_region_here
BUCKET_NAME=your_s3_bucket_name_here

# Database Configuration (if needed)
DATABASE_URL=your_database_connection_string_here

# API Keys (if needed)
API_KEY=your_api_key_here

# Application Configuration
DEBUG=True
SECRET_KEY=your_secret_key_here
```

**Important**: Never commit your actual `.env` file to version control. The `.gitignore` file is already configured to exclude it.

### 5. Run the Application

#### Dashboard
```bash
cd Dashboard
streamlit run app.py
```

#### ETL Scripts
```bash
cd ETL
python clean_data.py
python fetch_transformed.py
python upload_s3.py
```

## Security Notes

- The `.env` file contains sensitive information and is excluded from version control
- AWS credentials should be kept secure and never shared
- Consider using AWS IAM roles for production deployments
- Regularly rotate your API keys and credentials

## Data Sources

- SpaceX launch data
- ISRO launch data
- Global space exploration dataset

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add your license information here] 