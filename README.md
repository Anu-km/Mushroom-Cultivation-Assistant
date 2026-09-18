# Mushroom-Cultivation-Assistant

# 🍄 Mushroom Cultivation Assistant

A **Python-based Mushroom Cultivation Assistant** developed using **Tkinter GUI** to help mushroom growers with mushroom screening, substrate/material selection, problem diagnosis, cultivation guidance, and market price information.

The application provides a simple and user-friendly interface where users can select different mushroom varieties and get cultivation-related information.

---

## 📌 Project Overview

Mushroom cultivation requires proper selection of substrates, temperature, humidity, growth duration, disease/problem identification, and market awareness.

The **Mushroom Cultivation Assistant** provides these facilities through a desktop-based graphical user interface.

### Main Features

* 🍄 Mushroom Screening
* 🌾 Substrate/Material Selection
* 🌡️ Temperature and Humidity Information
* 📅 Expected Harvest Date
* 🧫 Problem Diagnosis
* 💡 Problem-Solving Suggestions
* 💰 Market Price Information
* 📈 Basic Market Recommendation
* 🖥️ User-friendly Tkinter GUI
* 📊 Quantitative and qualitative cultivation information

---

## 🎯 Objectives

The main objectives of this project are:

1. Help users select suitable mushroom cultivation materials.
2. Provide basic environmental requirements for different mushrooms.
3. Estimate the expected cultivation/harvest period.
4. Identify common mushroom cultivation problems.
5. Provide basic solutions for common cultivation issues.
6. Display approximate mushroom market prices.
7. Provide a simple desktop application for mushroom cultivation assistance.

---

## 🍄 Supported Mushroom Types

The application currently supports:

| Mushroom    | Temperature | Humidity | Expected Growth | Expected Yield |
| ----------- | ----------- | -------- | --------------: | -------------: |
| Paddy Straw | 30–35°C     | 80–90%   |         18 days |      1.0 kg/kg |
| Oyster      | 25–30°C     | 85–90%   |         20 days |      1.5 kg/kg |
| Milky       | 30–35°C     | 85–90%   |         22 days |      1.3 kg/kg |
| Button      | 18–22°C     | 85–95%   |         25 days |      1.2 kg/kg |

> **Note:** The values in this table are application data intended for educational/project purposes. Actual cultivation requirements and yields can vary depending on strain, substrate preparation, environmental conditions, and cultivation practices.

---

## 🌾 Substrate Selection

The application provides suitable substrate options for different mushroom types.

### Paddy Straw Mushroom

Suggested substrates:

* Paddy straw
* Banana leaves
* Sugarcane bagasse

### Oyster Mushroom

Suggested substrates:

* Paddy straw
* Sugarcane bagasse
* Sawdust

### Milky Mushroom

Suggested substrates:

* Wheat straw
* Sugarcane bagasse

### Button Mushroom

Suggested substrates:

* Composted manure
* Wheat straw

---

## 🧫 Problem Solver

The Problem Solver module recognizes common cultivation symptoms and provides basic suggestions.

Currently supported problems include:

| Problem            | Stress Type | Suggested Action                                  |
| ------------------ | ----------- | ------------------------------------------------- |
| White mold         | Biotic      | Reduce humidity and sterilize substrate           |
| Insect infestation | Biotic      | Use neem extract and maintain hygiene             |
| Slow growth        | Abiotic     | Adjust temperature and humidity                   |
| Dry caps           | Abiotic     | Lightly spray water and maintain humidity         |
| Bad smell          | Biotic      | Discard contaminated batch and sterilize the area |

The user enters a symptom in the input field.

Example:

```text
white mold
```

The application displays the problem type and suggested action.

---

## 💰 Market Alert

The Market Alert module displays a randomly generated example price for the selected mushroom.

Supported mushroom types:

* Paddy Straw
* Oyster
* Milky
* Button

The application also provides a basic suggestion based on the generated price.

Example:

```text
Current Price: ₹200/kg
Recommendation: Sell now! Good demand.
```

### Important

The current market module uses Python's `random` module to generate demonstration prices.

Therefore, the displayed price **is not a live market price**.

A future version can connect the application to a real-time agricultural/market API or database.

---

# 🖥️ Application Interface

The application contains three main tabs:

### 1. Screening

Provides:

* Mushroom type
* Suitable substrates
* Temperature
* Humidity
* Expected yield
* Growth duration
* Expected harvest date
* Cultivation reason
* Basic care information

### 2. Problem Solver

Provides:

* Symptom input
* Problem classification
* Biotic/Abiotic stress identification
* Suggested solution

### 3. Market Alert

Provides:

* Mushroom selection
* Example market price
* Basic selling recommendation
* Market monitoring tip

---

# 🛠️ Technologies Used

### Programming Language

* Python 3

### GUI Framework

* Tkinter
* ttk

### Python Libraries

```text
tkinter
datetime
random
```

All libraries used by the current version are part of the Python standard library.

---

# 📂 Project Structure

```text
Mushroom-Cultivation-Assistant/
│
├── mushroom_assistant.py
├── README.md
└── requirements.txt
```

---

# ⚙️ Installation

## Step 1: Install Python

Download and install Python 3 from:

https://www.python.org/

During Windows installation, make sure to enable:

```text
Add Python to PATH
```

---

## Step 2: Clone the Repository

Open Command Prompt or Terminal:

```bash
git clone https://github.com/YOUR_USERNAME/Mushroom-Cultivation-Assistant.git
```

Move into the project directory:

```bash
cd Mushroom-Cultivation-Assistant
```

---

## Step 3: Check Python Installation

Run:

```bash
python --version
```

Example:

```text
Python 3.11.x
```

---

# ▶️ How to Run

Run the following command:

```bash
python mushroom_assistant.py
```

The Mushroom Cultivation Assistant GUI will open.

---

# 🪟 Windows Users

If `python` does not work, try:

```bash
py mushroom_assistant.py
```

---

# 🐧 Linux Users

Install Tkinter if required.

For Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3-tk
```

Then run:

```bash
python3 mushroom_assistant.py
```

---

# 📦 Requirements

The project currently does not require external Python packages.

`requirements.txt`:

```text
# No external dependencies required
# Python 3.x with Tkinter
```

---

# 🔄 Application Workflow

```text
             ┌──────────────────────────┐
             │   Mushroom Cultivation   │
             │       Assistant          │
             └────────────┬─────────────┘
                          │
             ┌────────────┼─────────────┐
             │            │             │
             ▼            ▼             ▼
        Screening    Problem Solver   Market Alert
             │            │             │
             ▼            ▼             ▼
        Mushroom       Symptom        Mushroom
        Selection       Input         Selection
             │            │             │
             ▼            ▼             ▼
        Cultivation    Diagnosis      Example
        Information    & Solution      Price
             │            │             │
             └────────────┼─────────────┘
                          ▼
                    User Guidance
```

---

# 📊 Screening Workflow

The screening module works as follows:

```text
Select Mushroom
       ↓
Retrieve Mushroom Data
       ↓
Get Suitable Substrates
       ↓
Get Temperature
       ↓
Get Humidity
       ↓
Get Expected Yield
       ↓
Calculate Harvest Date
       ↓
Display Cultivation Information
```

---

# 🧫 Problem Solver Workflow

```text
Enter Symptom
      ↓
Convert Input to Lowercase
      ↓
Search Problem Database
      ↓
Problem Found?
    /       \
  Yes        No
   ↓          ↓
Show Type   Show Message
   ↓
Show Suggested Solution
```

---

# 💰 Market Alert Workflow

```text
Select Mushroom
       ↓
Generate Example Price
       ↓
Compare Price
       ↓
Generate Basic Recommendation
       ↓
Display Market Information
```

---

# 🧮 Harvest Date Calculation

The application automatically calculates the expected harvest date.

The calculation uses:

```python
harvest_date = start_date + datetime.timedelta(
    days=data['growth_days']
)
```

For example, if the growth duration is:

```text
20 days
```

the application adds 20 days to the current date.

---

# 🧠 Data Used in the Application

The application currently uses Python dictionaries for storing cultivation information.

Example:

```python
substrates = {
    "Oyster": {
        "substrate": [
            "Paddy straw",
            "Sugarcane bagasse",
            "Sawdust"
        ],
        "temp": "25–30°C",
        "humidity": "85–90%",
        "yield": "1.5 kg/kg",
        "growth_days": 20
    }
}
```

The problem database is also stored using a Python dictionary.

---

# 🔐 Current System Limitations

This is an educational/prototype application.

Current limitations include:

* Market prices are randomly generated.
* No live weather API is connected.
* No real-time humidity sensor is connected.
* No IoT hardware integration.
* No database.
* Problem recognition is based on predefined symptoms.
* No machine learning model is currently integrated.
* Cultivation recommendations are rule-based.
* No user login/account system.
* No cloud synchronization.

---

# 🚀 Future Improvements

The project can be expanded into a smart agriculture/mushroom farming platform.

### 🤖 1. AI-Based Disease Detection

Integrate a computer vision model to identify mushroom diseases from images.

Possible technologies:

* Python
* OpenCV
* TensorFlow
* PyTorch
* CNN
* YOLO

Example workflow:

```text
Upload Mushroom Image
        ↓
Image Processing
        ↓
AI Model
        ↓
Disease Detection
        ↓
Treatment Recommendation
```

---

### 🌡️ 2. IoT Environment Monitoring

Connect sensors to monitor:

* Temperature
* Humidity
* CO₂
* Light
* Moisture

Possible hardware:

* ESP32
* Arduino
* Raspberry Pi
* DHT11/DHT22
* Soil/moisture sensors

---

### 🌦️ 3. Weather API Integration

Connect a weather API to provide environmental recommendations based on the user's location.

---

### 💰 4. Real-Time Market Prices

Replace the random price generator with a real agricultural market API/database.

Possible features:

* Daily price
* Weekly price
* Price history
* Market comparison
* Price alerts
* Selling recommendations

---

### 📱 5. Mobile Application

The project can be converted into an Android application using:

* Kotlin
* Jetpack Compose
* Flutter
* React Native

---

### 🌐 6. Web Application

A web version can be developed using:

**Frontend:**

* HTML
* CSS
* JavaScript
* React

**Backend:**

* Python Flask
* FastAPI
* Node.js

---

### 🗄️ 7. Database Integration

A database can store:

* Farmers
* Mushroom batches
* Cultivation dates
* Harvest records
* Problems
* Market prices
* Environmental data

Possible databases:

* SQLite
* MySQL
* PostgreSQL
* MongoDB

---

### 📈 8. Smart Analytics Dashboard

Future versions can include:

* Production charts
* Yield analysis
* Market trends
* Cost calculation
* Profit estimation
* Batch monitoring

---

# 🎓 Academic Use

This project can be used as a:

* Python project
* GUI project
* Agriculture technology project
* Mushroom cultivation project
* Smart farming prototype
* Mini project
* Final-year project foundation

---

# 👨‍💻 Developer

**Vicky Kumar**

B.Tech Computer Science & Engineering
Cybersecurity Domain

### Areas of Interest

* Python
* Cybersecurity
* Artificial Intelligence
* Machine Learning
* Software Testing
* QA Testing
* GUI Application Development

---

# 📜 License

This project is intended for educational and demonstration purposes.

You may modify and extend the project according to your requirements.

---

# ⭐ Future Vision

The long-term goal is to transform this prototype into an **AI-powered smart mushroom cultivation assistant** that combines:

```text
AI
+
IoT Sensors
+
Weather Data
+
Disease Detection
+
Market Intelligence
+
Production Analytics
```

to provide intelligent assistance throughout the mushroom cultivation lifecycle.

---

## ⭐ If You Like This Project

If this project is useful, consider giving the repository a ⭐ on GitHub.

---

## 📌 Disclaimer

The cultivation values, recommendations, and example market prices provided by this application are for educational/demo purposes. Actual mushroom cultivation should be performed according to appropriate agricultural practices, local conditions, mushroom strain requirements, and expert guidance.

