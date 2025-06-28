import pandas as pd

def clean_data():
    df = pd.read_csv('data.csv')

    df = df.dropna()

    df.to_csv('cleaned_data.csv', index=False)

    print("✅ Data cleaned and saved to 'cleaned_data.csv'.")

if __name__ == '__main__':
    clean_data()
