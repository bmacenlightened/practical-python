# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    cost = 0.0
    with open('Data/portfolio.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows, start=1):
            record = dict(zip(headers,row))
            try:
                cost += int(record['shares']) * float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(str(cost))