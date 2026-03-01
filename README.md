# Data Cleaning with Pandas

This project demonstrates how to clean and preprocess a messy real-world dataset using Python and Pandas.
The goal is to transform inconsistent, poorly formatted data into a structured and analysis-ready format.

It covers common data cleaning tasks such as fixing column names, handling missing values, converting data types, and removing unwanted characters from numeric fields.

---

## 📌 Project Overview

Raw datasets often contain problems like:

* Inconsistent column naming
* Currency symbols mixed with numbers
* Percentage values stored as strings
* Incorrect or missing dates
* Duplicate records
* Missing quantities

This script automates the cleaning process and produces a standardized dataset that can be used for analysis or machine learning.

---

## ⚙️ Features

* Standardizes column names (lowercase, snake_case)
* Converts date columns into proper datetime format
* Cleans currency fields and converts them to numeric values
* Normalizes tax percentage values
* Handles missing quantities with default values
* Removes duplicate rows
* Outputs cleaned data preview

---

## 🧰 Technologies Used

* Python 3
* Pandas
* NumPy

---

## 📂 Project Structure

```
Data-Cleaning-with-Pandas/
│── clean.py
│── messy_dataset.csv
│── requirements.txt
│── .gitignore
│── LICENSE
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/jayeshkoli-1402/Data-Cleaning-with-Pandas
cd Data-Cleaning-with-Pandas
```

### 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

Activate:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run the Script

```
python clean.py
```

---

## 📊 Example Cleaning Tasks Performed

Some transformations handled by the script include:

| Raw Value       | Cleaned Value |
| --------------- | ------------- |
| `$120 USD`      | `120.0`       |
| `5%`            | `0.05`        |
| `NaN quantity`  | `1`           |
| `" Ship Date "` | `ship_date`   |

---

## 🎯 Learning Objectives

This project was created to practice:

* Data preprocessing with Pandas
* Handling messy datasets
* Writing reusable data cleaning logic
* Preparing data for analysis workflows
* Using Git for version control

---

## 🔮 Future Improvements

Possible extensions:

* Export cleaned dataset to a new CSV file
* Add data validation checks
* Create automated cleaning functions
* Build a visualization dashboard
* Integrate with a web interface

---

## 👤 Author

**Jayesh Koli**

Computer Science Engineering Student
Interested in Data Science, AI/ML, and Software Development

---

## 📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

⭐ If you found this useful, consider giving the repository a star.
