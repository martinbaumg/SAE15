import os
import pandas as pd

def merge_csv(filename1,filename2,mergedfilepath):
    df1=pd.read_csv(filename1)
    df2=pd.read_csv(filename2)
    df = pd.concat([df1,df2], ignore_index=True)
    df.to_csv(mergedfilepath, index=False)

def compute_missing_values(df):
    missing_data={}
    for item in df:
        percent=df[item].isna().sum()/len(df[item])* 100
        missing_data[item]={'number':df[item].isna().sum(),'percentage':'{:.2}%'.format(percent)}
    print(missing_data)

    return missing_data


def compute_outliers(df):
    outliers_data={}
    for item in ['RSSI']:
        max_value = df[item].max()
        min_value = df[item].min()

        outliers_count = len(df[df[item].map(lambda x: x == max_value)])+len(df[df[item].map(lambda x: x == min_value)])

        outliers_percent = (outliers_count / len(df[item])) * 100
        outliers_percent = '{0:.2f}'.format(outliers_percent)

        outliers_data[item]={'Number':outliers_count,'Percentage':outliers_percent}
    print(outliers_data)
    return outliers_data



if __name__ == '__main__':
    filename1 = os.path.join("../../data/processed/scan_wifi-rdc.csv")
    filename2 = os.path.join(os.getcwd(), "../../data/processed/scan_wifi-premier.csv")
    mergefilename = os.path.join(os.getcwd(), "../../data/processed/scan_wifi.csv")
    merge_csv(filename1,filename2,mergefilename)

    #valeurs abberantes et manquantes
    df=pd.read_csv(mergefilename)
    compute_missing_values(df)
    compute_outliers(df)


