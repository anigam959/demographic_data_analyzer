# demographic_data_analyzer
Analyzes the Adult Census Income dataset to uncover demographic insights on income, education, age, occupation, and work hours. Combines data cleaning, exploration, visualization, and unit-tested Python functions to answer key socioeconomic questions effectively.


# 📊 Census Income Data Analysis and Visualization

This project analyzes the **Adult Census Income** dataset to extract demographic insights related to income distribution. It includes data cleaning, exploration, visualization, and unit testing using modular Python code.

---

## 📁 Project Structure

census+income/
├── adult.data # Raw dataset
├── demographic_data_analyzer.py # Core Python functions for analysis
├── test_module.py # Unit tests for validation
├── analysis_notebook.ipynb # Full EDA and visualization notebook
└── README.md # Project documentation

yaml
Copy code

---

## 📌 Key Features

- ✅ Clean and preprocess census data
- 📈 Analyze age, education, hours worked, and income
- 🌎 Compare income distribution across countries
- 🔬 Modular Python functions for reusability
- 🧪 Unit tests using `unittest` framework

---

## 📊 Sample Analysis Goals

- Average age of men and women
- % with Bachelor's or advanced degrees earning >50K
- Country with highest % of high earners
- Most common occupation for rich individuals in India

---

## ⚙️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/census-income-analysis.git
cd census+income
2. Install dependencies
bash
Copy code
pip install pandas numpy matplotlib seaborn
3. Run notebook for full analysis
Open analysis_notebook.ipynb in Jupyter or VS Code and run all cells.

4. Run unit tests
bash
Copy code
python test_module.py
🧪 Unit Testing
Tests are written in test_module.py and validate the core functions in demographic_data_analyzer.py.

Example:

python
Copy code
def test_average_age_of_women(self):
    result = analyze_age_distribution(df)
    self.assertTrue(result > 0)
📂 Dataset
The dataset used is adult.data, which contains demographic data including:

Age, sex, education, occupation, etc.

Income group: <=50K or >50K
