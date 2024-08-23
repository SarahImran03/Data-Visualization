import matplotlib.pyplot as mlib
import pandas as pd
import seaborn as sbs

def visualize_data(data_sheet):
    # Line plot
    mlib.figure(figsize=(10,8))
    mlib.plot(data_sheet['Year'], data_sheet['Revenue'], marker='o', label='Revenue', color='blue')
    mlib.plot(data_sheet['Year'], data_sheet['Expenses'], marker='o', label='Expenses', color='purple')
    mlib.title('Revenue vs. Expenses Over Years')
    mlib.xlabel('Year')
    mlib.ylabel('Amount (x10^8)')
    mlib.legend()
    mlib.grid(True)
    mlib.show()

    # Histograms
    mlib.subplot(1, 2, 1)
    sbs.histplot(data_sheet['Revenue'], bins=5, kde=False, color='green')
    mlib.title('Revenue Distribution')
    mlib.xlabel('Revenue (x10^8)')
    mlib.ylabel('Frequency')

    mlib.subplot(1, 2, 2)
    sbs.histplot(data_sheet['Expenses'], bins=5, kde=False, color='blue')
    mlib.title('Expenses Distribution')
    mlib.xlabel('Expenses (x10^8)')
    mlib.ylabel('Frequency')
    mlib.show()

    # Area Charts
    mlib.figure(figsize=(10, 8))
    mlib.fill_between(data_sheet['Year'], data_sheet['Revenue'], color='green', alpha=0.5, label='Revenue')
    mlib.fill_between(data_sheet['Year'], data_sheet['Expenses'], color='red', alpha=0.5, label='Expenses')
    mlib.title('Revenue vs. Expenses Area Chart')
    mlib.xlabel('Year')
    mlib.ylabel('Amount (x10^8)')
    mlib.legend()
    mlib.grid(True)
    mlib.show()

    # Pair plot
    sbs.pairplot(data_sheet)
    mlib.suptitle('Pair Plot of Revenue and Expenses', y=1.02)
    mlib.show()

    return 0

def main():
    data_sheet = pd.read_csv('AI Research & Development Fellowship - Assessment Datasets - Question 2 - Data Visualization.csv')
    visualize_data(data_sheet)

    return 0

if __name__ == "__main__":
    main()