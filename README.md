# 🦠 COVID-19 REPORT

## 📊 COVID-19 Data Analysis and Visualization System

A Python-based COVID-19 Report project that allows users to explore, clean, analyze, and visualize COVID-19 data using Pandas, Matplotlib, and Seaborn. It provides information about total deaths, average deaths, maximum deaths, and minimum deaths through statistical analysis and graphical representation.

---

## 1. Features

- **Explore Data**
  - Display Top 5 Records.
  - Display Last 5 Records.
  - Show Dataset Information.
  - Check Data Types.

- **Clear Data**
  - Check Missing Values.
  - Delete Missing Data.
  - Fill Missing Data.
  - Check Duplicate Records.

- **Perform Data Analysis**
  - Calculate Total Deaths.
  - Calculate Average Deaths.
  - Find Maximum Deaths.
  - Find Minimum Deaths.

- **Data Visualization**
  - Bar Graph.
  - Line Graph.
  - Pie Graph.
  - Histogram Graph.
  - Scatter Graph.

- **Data Analysis Report**
  - Generate a summary of COVID-19 death statistics.

---

## 2. Technologies Used

- **Python** – Main Programming Language.
- **Pandas** – Data Cleaning and Data Analysis.
- **Matplotlib** – Data Visualization.
- **Seaborn** – Statistical Data Visualization.
- **CSV** – Data Storage Format.

---

## 3. Concepts Used

- Python Conditional Statements (`if`, `elif`, `else`).
- User Input (`input()`).
- Type Conversion (`int()`).
- Pandas DataFrame.
- CSV File Handling.
- Data Exploration.
- Missing Data Handling.
- Duplicate Data Checking.
- Statistical Functions:
  - `sum()`
  - `mean()`
  - `max()`
  - `min()`
- Data Visualization:
  - `plot.bar()`
  - `plot.line()`
  - `plot.pie()`
  - `plot.hist()`
  - `plot.scatter()`

---

## 4. How to Use

1. Run the Python program.
2. Select an option from the main menu.
3. Enter your COVID-19 CSV file name.
4. Select the required operation.
5. View the results in the terminal or graphical window.

### Main Menu

1. Explore Data
2. Clear Data
3. Perform Data Analysis
4. Visualization Data
5. Data Analysis Report

---

## 5. Installation

**Step 1: Install Python**

Download and install Python from:

https://www.python.org/downloads/

**Step 2: Install Required Libraries**

Open your terminal or command prompt and execute:

```bash
pip install pandas
pip install matplotlib
pip install seaborn
```

**Step 3: Download or Clone the Project**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 4: Open the Project Folder**

```bash
cd COVID-19-Report
```

**Step 5: Run the Python Program**

```bash
python covid.py
```

**Step 6: Enter Your CSV File Name**

```text
Enter The File Name Eg(covid.csv) :- covid.csv
```

---

## 6. Example Output

### Main Menu

```text
====================
COVID-19 REPORT
====================

1. Explore Data
2. Clear Data
3. Perform Data Analysis
4. Visualization Data
5. Data Analysis Report

Enter The Number Between (1-5) :- 5

===== Load Data =====

Enter The File Name Eg(covid.csv) :- covid.csv

Data Added Successfully!

===== DATA ANALYSIS REPORT =====

1. Total Deaths   :- 100000
2. Average Deaths :- 1000
3. Maximum Deaths :- 5000
4. Minimum Deaths :- 10
```

*Note: The numbers above are sample values for demonstration. Actual results depend on your CSV dataset.*

---

## 7. Project Structure

```text
MP.C19/
│
├── covid.py
│
├── covid.csv
│
└── README.md
```

---

## 8. Author

Dev Thakkar