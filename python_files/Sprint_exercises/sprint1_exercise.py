import csv

def load_file(filename):
    data=[]
    with open(filename,'r') as f:
        reader=csv.DictReader(f)

        for row in reader:
            data.append(row)
        
    return data

def summarize_data(data):

    if not data:
        print('No data found.')
    
    # print top 5 rows
    print('Top 5 rows')

    for row in data[:5]:
        print(row)

    # Row count
    print(f'Row count: {len(data)}')

    # compute average

    numeric_cols=[]
    first_row=data[0]

    for key,value in first_row.items():
        try:
            float(value)
            numeric_cols.append(key)
        except ValueError:
            continue

    if numeric_cols:
        print('Columns Average -')
        for col in numeric_cols:
            total=sum(float(row[col]) for row in data)
            avg=total/len(data)
            print(f'{col}: {avg:.2f}')
    else:
        print('No numeric values found in data set.')


import argparse

def main():

    parser=argparse.ArgumentParser(description='Load csv and print summary')
    parser.add_argument('file_path',help='C:/Users/igoel/Desktop/AI_Learning/practise_code/csv_files/test_case_s1.csv')
    args=parser.parse_args()

    data=load_file(args.file_path)
    summarize_data(data)

if __name__=='__main__':
    main()

