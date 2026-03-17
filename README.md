# gaming-market-analysis
Data-Driven campaign planning for online games store

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Project Structure](#project-structure)
- [Key Analysis Steps](#key-analysis-steps)
  - [1. Data Exploration & Preprocessing](#1-data-exploration--preprocessing)
  - [2. Exploratory Data Analysis (EDA)](#2-exploratory-data-analysis-eda)
  - [3. Statistical Analysis](#3-statistical-analysis)
  - [4. Hypothesis Testing](#4-hypothesis-testing)
  - [5. Insights & Recommendations](#5-insights--recommendations)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

### Prerequisites
- Python 3.9 or higher
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
   venv\Scripts\activate

   # On macOS/Linux:
   source venv/bin/activate
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

## Usage

Run the analysis using one of the following options:

- **Streamlit Dashboard** (interactive web app):
  ```bash
  streamlit run main.py
  ```

- **Jupyter Notebook** (for exploratory analysis):
  ```bash
  jupyter notebook
  ```

- **Console Script** (basic execution):
  ```bash
  python main.py
  ```

Results will be displayed in the console, web browser (for Streamlit), or notebook interface.

## Project Overview

This project analyzes video game sales data for **Ice**, an online video game store, to identify patterns that determine game success and plan effective advertising campaigns for 2017.

**Business Objective:** Identify potential successful games and optimize marketing strategies based on historical sales data, user ratings, and market trends.

**Analysis Period:** Historical data through 2016, with insights for 2017 campaign planning.

## Dataset Description
The analysis uses the `games.csv` dataset containing video game sales and rating information with the following key features:

**Game Information:**
- `name` - Game title
- `platform` - Gaming platform (e.g., PS4, Xbox, PC)
- `year_of_release` - Release year
- `genre` - Game genre (Action, Sports, RPG, etc.)
- `publisher` - Game publisher

**Sales Data (in millions):**
- `na_sales` - North American sales
- `eu_sales` - European sales  
- `jp_sales` - Japanese sales
- `other_sales` - Other regions sales

**Ratings:**
- `critic_score` - Professional critic scores
- `user_score` - User ratings
- `rating` - ESRB age rating (E, T, M, etc.)

**Dataset Size:** Contains thousands of games across multiple platforms and years.

## Project Structure

```
gaming-market-analysis/
├── .streamlit/
│   └── config.toml              # Streamlit configuration
├── data/
│   └── raw/
│       └── games.csv            # Raw dataset
├── src/
│   └── config.json              # Project configuration
├── utils/
│   ├── __init__.py              # Package initialization
│   └── [modules to be added]    # Helper functions
├── main.py                      # Main application entry point
├── requirements.txt             # Dependencies
├── LICENSE                      # License file
└── README.md                    # Project documentation
```

## Key Analysis Steps

### 1. Data Exploration & Preprocessing
- **Initial Data Investigation**: Check dataset size, shape, and basic information
- **Data Quality Assessment**: Identify and handle missing values, duplicates, and inconsistencies
- **Data Cleaning**: 
  - Standardize column names (convert to lowercase)
  - Handle missing values in critic_score, user_score, and year_of_release
  - Remove or impute incomplete records
- **Feature Engineering**: Create total_sales column (sum of regional sales)

### 2. Exploratory Data Analysis (EDA)
- **Temporal Analysis**: Examine sales trends over years (focus on recent data for 2017 planning)
- **Platform Analysis**: Identify leading, growing, and declining gaming platforms
- **Genre Performance**: Analyze which game genres perform best in different regions
- **Publisher Insights**: Evaluate top-performing publishers and their market share

### 3. Statistical Analysis
- **Correlation Analysis**: Examine relationships between critic scores, user scores, and sales
- **Regional Comparison**: Compare gaming preferences across NA, EU, JP, and other markets
- **Platform Lifecycle**: Analyze platform performance patterns and market saturation

### 4. Hypothesis Testing
- **User vs Critic Ratings**: Test if professional and user ratings equally predict success
- **Genre Performance**: Statistical testing of genre preferences by region
- **Platform Impact**: Analyze if platform choice significantly affects sales performance

### 5. Insights & Recommendations
- **Success Patterns**: Identify key factors that determine game success
- **Market Segmentation**: Define target audiences for 2017 campaigns
- **Campaign Strategy**: Develop data-driven recommendations for advertising focus

## Technologies Used

**Programming Language:**
- Python 3.9+

**Data Analysis Libraries:**
- pandas - Data manipulation and analysis
- numpy - Numerical computing
- matplotlib - Data visualization
- seaborn - Statistical data visualization
- scipy - Statistical analysis and hypothesis testing

**Web Application:**
- streamlit - Interactive dashboard and data app

**Development Tools:**
- Jupyter Notebook - Interactive development and analysis
- Git - Version control

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m 'Add feature'`.
4. Push to branch: `git push origin feature-name`.
5. Open a Pull Request.

For issues or suggestions, open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [https://github.com/your-username]

## Contributing