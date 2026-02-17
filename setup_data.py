import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_mock_data():
    print("Generating simulated fitness data...")
    
    base_date = datetime.today() - timedelta(days=30)
    dates = [(base_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in range(30)]
    
    # Generate Nutrition Data
    np.random.seed(42)
    weight_trend = np.linspace(84.5, 83.0, 30) + np.random.normal(0, 0.2, 30)
    calories = np.random.normal(2400, 150, 30).astype(int)
    protein = np.random.normal(140, 10, 30).astype(int)
    
    nutrition_df = pd.DataFrame({
        'Date': dates,
        'Bodyweight_kg': weight_trend.round(1),
        'Calories': calories,
        'Protein_g': protein
    })
    nutrition_df.to_csv('nutrition_log.csv', index=False)
    print("-> Created nutrition_log.csv")

    # Generate Workout Data
    workout_records = []
    exercises = ['Bench Press', 'Squat', 'Deadlift', 'Overhead Press']
    workout_days = random.sample(dates, 16)
    
    for date in sorted(workout_days):
        session_exercises = random.sample(exercises, k=random.randint(2, 3))
        for ex in session_exercises:
            base_weight = {'Bench Press': 60, 'Squat': 80, 'Deadlift': 100, 'Overhead Press': 40}[ex]
            for s in range(3):
                reps = random.randint(5, 8)
                workout_records.append({
                    'Date': date,
                    'Exercise': ex,
                    'Set': s + 1,
                    'Reps': reps,
                    'Weight_kg': base_weight + (random.random() * 5)
                })
                
    pd.DataFrame(workout_records).to_csv('workouts.csv', index=False)
    print("-> Created workouts.csv")

if __name__ == "__main__":
    generate_mock_data()