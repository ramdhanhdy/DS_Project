# Data Science Project with Flask Deployment

Advancing Public Transportation in Malang Using Data Drivent Techniques

## Project Structure

- `data/`: Contains raw, processed, and external data
- `models/`: Stores trained models
- `notebooks/`: Jupyter notebooks for data preparation, EDA, and modeling
- `src/`: Source code for the project
- `tests/`: Unit tests
- `app/`: Flask application for deployment
- `config/`: Configuration files
- `docs/`: Project documentation

## Setup

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Usage

1. Data Preparation:
   - Place raw data in `data/raw/`
   - Run the `notebooks/01_data_preparation.ipynb` notebook
2. Exploratory Data Analysis:
   - Run the `notebooks/02_exploratory_data_analysis.ipynb` notebook
3. Modeling:
   - Run the `notebooks/03_modeling.ipynb` notebook
   - Alternatively, run `python src/models/train_model.py` to train the model
4. Run the Flask app:
   ```
   cd app
   python app.py
   ```
5. Open a web browser and go to `http://localhost:5000`


