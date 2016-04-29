import pandas as pd

#filename = 'memetracker/test.txt'
filename = 'memetracker/quotes_2008-08.txt'

links = []

with open(filename) as f:
    content = [x.strip('\n') for x in f.readlines()]
    lines = content.__iter__()
    df_rows = []
    for line in lines:
        x = line.split('\t')
        if x[0] == 'P':
            post_url = x[1]
        elif x[0] == 'T':
            date = x[1]
        elif x[0] == 'L':
            hyperlink = x[1]
            row = [post_url, date, hyperlink]
            df_rows.append(row)
    df = pd.DataFrame(df_rows, columns=['Post URL', 'Date', 'Hyper Link'])
    df['Date'] = pd.to_datetime(df['Date'])


if __name__ == '__main__':
    print("len(df = ",len(df))
    i = 0
    with open(filename) as f:
        content = [x.strip('\n') for x in f.readlines()]
        for line in content:
            if line.split('\t')[0] == 'L': i += 1
    print("Number of lines starting with 'L' = ",i)