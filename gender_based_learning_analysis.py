import pandas as pd
import sys
import os

def analyze_student_performance(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Quick overview
    print("\nDataset Overview:")
    print(df.head())
    print("\nBasic Statistics:")
    print(df.describe())
    print("\nData Information:")
    print(df.info())

    # Check basic gender distribution
    print("\nGender Distribution:")
    print(df['gender'].value_counts())

    # Find average scores by gender
    print("\nAverage Scores by Gender:")
    print(df.groupby('gender')[['math score', 'reading score', 'writing score']].mean())

    # Check correlations between numeric scores
    print("\nCorrelations between Scores:")
    numeric_columns = ['math score', 'reading score', 'writing score']
    print(df[numeric_columns].corr())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gender_based_learning_analysis.py <input_file_path>")
        print("Example: python gender_based_learning_analysis.py StudentsPerformance.csv.xls")
        sys.exit(1)
    
    input_file = sys.argv[1]
    analyze_student_performance(input_file)
