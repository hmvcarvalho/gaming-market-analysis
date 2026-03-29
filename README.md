# gaming-market-analysis
Data-Driven campaign planning for online games store

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Key Analysis Steps](#key-analysis-steps)
- [Key Findings](#key-findings)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

### Prerequisites
- Python 3.12 or higher (recommended: 3.12.10 for best package compatibility)
- Git (for cloning the repository)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/hmvcarvalho/gaming-market-analysis.git
   cd gaming-market-analysis
   ```

2. Create Virtual Environment
   ```bash
   # Create virtual environment
   python -m venv .venv

   # Activate virtual environment
   # On Windows:
   .venv\Scripts\activate

   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Deactivate Virtual Environment (when finished)
   ```bash
   deactivate
   ```

### Troubleshooting
- Ensure your virtual environment is activated before installing packages
- If you encounter dependency conflicts, try creating a fresh virtual environment
- For Windows users: If activation fails, try `venv\Scripts\activate.bat`
- **Python Version Issues**: Use Python 3.12.x for best compatibility with data science packages. Avoid 3.13+ until packages catch up.

## Usage

Run the analysis using Jupyter Notebook:
```bash
jupyter notebook
```

Open the notebooks in order:
1. `notebooks/01_data_preparation.ipynb`
2. `notebooks/02_eda_and_hypothesis.ipynb`

## Project Overview

This project analyzes video game sales data for **Ice**, an online video game store, to identify patterns that determine game success and plan effective advertising campaigns for 2017.

**Business Objective:** Identify potential successful games and optimize marketing strategies based on historical sales data, platform trends, regional preferences, and user ratings.

**Analysis Period:** Historical data from 1980 through 2016, with focus on 2010+ data for 2017 campaign planning.

## Dataset Description

The analysis uses the `games.csv` dataset containing video game sales and rating information.

**Dataset Size:** 16,713 games across 31 platforms, 12 genres, and 4 regions (1980–2016)

**Game Information:**
- `name` - Game title
- `platform` - Gaming platform (e.g., PS4, Xbox, PC)
- `year_of_release` - Release year
- `genre` - Game genre (Action, Sports, RPG, etc.)

**Sales Data (in millions):**
- `na_sales` - North American sales
- `eu_sales` - European sales
- `jp_sales` - Japanese sales
- `other_sales` - Other regions sales
- `total_sales` - Global sales (derived)

**Ratings:**
- `critic_score` - Professional critic scores (0–100)
- `user_score` - User ratings (0–10)
- `rating` - ESRB age rating (E, T, M, etc.)

## Project Structure

```
gaming-market-analysis/
├── .streamlit/
│   └── config.toml                  # Streamlit configuration (dashboard — planned)
├── data/
│   ├── raw/
│   │   └── games.csv                # Raw dataset
│   └── processed/
│       └── cleaned_games.csv        # Cleaned dataset
├── src/
│   ├── config.json                  # Project configuration and data paths
│   └── main.py                      # Application entry point (dashboard — planned)
├── utils/
│   ├── __init__.py                  # Package initialization
│   └── data_processing.py           # Helper functions (hierarchical imputation)
├── notebooks/
│   ├── 01_data_preparation.ipynb    # Data cleaning and preprocessing
│   └── 02_eda_and_hypothesis.ipynb  # EDA, regional analysis and hypothesis testing
├── requirements.txt                 # Dependencies
├── LICENSE                          # License file
├── .gitignore                       # Git ignore rules
└── README.md                        # Project documentation
```

## Key Analysis Steps

### 1. Data Preparation
- Standardized column names and data types
- Handled missing values with hierarchical imputation strategy for critic and user scores
- Replaced `tbd` user scores with NaN; treated missing ESRB ratings as "Not Rated"
- Engineered `total_sales` feature from regional sales columns

### 2. Temporal & Platform Analysis
- Identified platform lifecycle patterns (growth → peak → decline)
- Selected 2010+ as the relevant period for 2017 campaign planning
- Compared platform sales distributions via boxplot to assess commercial potential

### 3. Ratings vs Sales
- Analyzed correlation between critic/user scores and PS4 sales
- Found critic scores moderately correlated (r=0.34); user scores near zero (r≈-0.05)

### 4. Regional User Profiles (NA, EU, JP)
- Identified top 5 platforms and genres per region
- Analyzed ESRB rating impact on regional sales
- Defined region-specific campaign strategies

### 5. Hypothesis Testing
- **Test 1:** Average user scores for XOne and PC are the same → *Failed to reject H0* (p=0.294)
- **Test 2:** Average user scores for Action and Sports differ → *Rejected H0* (p≈1.74e-18)

### 6. General Conclusion
- Synthesized findings into actionable 2017 campaign recommendations per region

## Key Findings

- **PS4** is the strongest platform for NA and EU campaigns; Japan requires a separate strategy focused on Nintendo/portable platforms (3DS)
- **Shooter** games yield the highest average sales despite lower release volume; **Action** and **Sports** are strong volume plays
- **Critic scores** are a moderate predictor of sales; user scores are not reliable for forecasting
- **M-rated** titles dominate NA and EU sales; Japan is less influenced by age ratings
- NA and EU markets are similar enough to share campaign content; Japan needs dedicated genre and platform targeting

## Technologies Used

**Programming Language:**
- Python 3.12+

**Data Analysis Libraries:**
- pandas - Data manipulation and analysis
- numpy - Numerical computing
- matplotlib - Data visualization
- seaborn - Statistical data visualization
- scipy - Statistical analysis and hypothesis testing

**Development Tools:**
- Jupyter Notebook - Interactive development and analysis
- Git - Version control

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
