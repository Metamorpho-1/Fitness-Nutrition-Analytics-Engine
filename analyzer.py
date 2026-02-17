import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calculate_1rm(weight, reps):
    """
    Estimates 1-Rep Max using the Brzycki formula.
    Formula: Weight * (36 / (37 - Reps))
    """
    # using np.where to handle the edge case where reps == 1 (to avoid dividing by weird decimals)
    return np.where(reps == 1, weight, weight * (36.0 / (37.0 - reps)))

def run_analytics():
    print("Booting up fitness analytics engine...\n")
    
    try:
        workouts = pd.read_csv('workouts.csv')
        nutrition = pd.read_csv('nutrition_log.csv')
    except FileNotFoundError:
        print("Error: Couldn't find the CSV files. Did you run setup_data.py first?")
        return

    # Convert date strings to actual datetime objects so matplotlib sorts them correctly
    workouts['Date'] = pd.to_datetime(workouts['Date'])
    nutrition['Date'] = pd.to_datetime(nutrition['Date'])

    # --- Crunching the Workout Data ---
    # Apply our 1RM formula to every row instantly using vectorized numpy operations
    workouts['Estimated_1RM'] = calculate_1rm(workouts['Weight_kg'], workouts['Reps'])

    # We only care about the best set of the day for the 1RM trend
    # groupby 'Date' and 'Exercise' and grab the max 1RM
    daily_maxes = workouts.groupby(['Date', 'Exercise'])['Estimated_1RM'].max().reset_index()

    # Isolate the Bench Press data to track our primary pushing strength
    bench_data = daily_maxes[daily_maxes['Exercise'] == 'Bench Press']

    # --- Outputting some terminal stats ---
    print("--- 30 DAY SUMMARY ---")
    start_wt = nutrition['Bodyweight_kg'].iloc[0]
    end_wt = nutrition['Bodyweight_kg'].iloc[-1]
    print(f"Bodyweight Change: {start_wt}kg -> {end_wt}kg")
    
    avg_protein = nutrition['Protein_g'].mean()
    print(f"Average Protein Intake: {avg_protein:.1f}g / day")
    print("----------------------\n")

    # --- Building the Matplotlib Dashboard ---
    # Setting up a figure with 2 subplots (1 row, 2 columns)
    plt.style.use('dark_background') # dark mode looks way better for hackathon demos
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.canvas.manager.set_window_title('Quantified Self - Analytics Dashboard')

    # Plot 1: Bodyweight Trend
    ax1.plot(nutrition['Date'], nutrition['Bodyweight_kg'], color='#00ffcc', marker='o', linewidth=2)
    ax1.set_title('Bodyweight Trend (Cutting Phase)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Weight (kg)')
    ax1.grid(True, alpha=0.2)
    ax1.tick_params(axis='x', rotation=45)
    # Adding a dashed line for the ultimate 75kg goal to show context
    ax1.axhline(y=75, color='#ff3366', linestyle='--', alpha=0.7, label='Target: 75kg')
    ax1.legend()
    

    # Plot 2: Bench Press Strength Progression
    ax2.plot(bench_data['Date'], bench_data['Estimated_1RM'], color='#ff9900', marker='^', linewidth=2)
    ax2.set_title('Bench Press 1RM Progression', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Estimated 1-Rep Max (kg)')
    ax2.grid(True, alpha=0.2)
    ax2.tick_params(axis='x', rotation=45)
    

    # clean up the layout so the x-axis dates don't overlap
    plt.tight_layout()
    
    print("Displaying dashboard... Close the window to exit the script.")
    plt.show()

if __name__ == "__main__":
    run_analytics()