# 🏋️‍♂️ Quantified Self: Fitness & Nutrition Analytics Engine
## 🎯 The Mission
This project was born out of a personal desire to move beyond basic logging apps and visualize the mathematical relationship between nutrition, body weight, and strength progression. I built this engine to handle real-world physiological datasets using the Python Data Science stack. It doesn't just display numbers; it uses established sports science formulas to predict performance and track long-term health trends.
## 🧠 Core Technical Features
* **Algorithmic 1RM Estimation:** Instead of just tracking raw weights, the engine implements the Brzycki Formula to calculate an estimated 1-Rep Max (1RM) for every set. This allows for an "apples-to-apples" comparison of strength across varying rep ranges.
* **Vectorized Data Processing:** Leveraging `numpy` and `pandas`, the engine processes thousands of rows of workout and nutrition data instantly. By avoiding slow Python loops, the dashboard remains scalable across years of user data.
* **Neural Dark-Mode Dashboard:** A custom-styled `matplotlib` interface providing a high-contrast visual story of two critical metrics:
    * **Weight Flux Analysis:** Tracks body weight against a target goal (e.g., 75kg) to visualize the effectiveness of caloric deficits or surpluses.
    * **Strength Velocity:** A visual trend line of Bench Press 1RM to identify plateaus or periods of peak performance.
* **Automated Data Simulation:** Includes a custom `setup_data.py` script that utilizes Normal Distribution and Linear Trends to generate 30 days of realistic, "messy" fitness data (including protein misses and weight fluctuations) for testing and demonstration.
## 🧮 The Logic Behind the Data
The engine focuses on the principle of Progressive Overload. By cleaning and grouping data by muscle group and date, the system identifies whether total "Volume" or "Intensity" is increasing over time. This enables data-driven decisions on when to increase weight or focus on recovery.
## 🚀 Getting Started
### Prerequisites
```bash
pip install pandas numpy matplotlib
```
### Installation & Usage
**1. Clone the repository:**
```bash
git clone https://github.com/Metamorpho-1/fitness-analytics-engine.git
cd fitness-analytics-engine
```
**2. Generate the sample data:**
```bash
python setup_data.py
```
**3. Launch the Analytics Dashboard:**
```bash
python analyzer.py
```
## 📈 Engineering Takeaways
* **Data Sanitization:** Mastered handling missing entries and converting string dates into sortable datetime objects for accurate time-series plotting.
* **Mathematical Vectorization:** Applied `numpy.where` and broadcasting to execute complex formulas across entire columns simultaneously.
* **Scientific Visualization:** Crafted multiple subplots using `dark_background` styles to create a professional-grade UX for data-heavy environments.
