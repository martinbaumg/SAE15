import os
import pandas as pd
def ComputeMean(df):
    df_rssi = df['RSSI']
    mean = df_rssi.mean()
    print("valeur moyenne :", mean)
    return mean


def ComputeMedian(df):
    df_rssi = df['RSSI']
    median = df_rssi.median()
    print("valeur medianne :", median)
    return median


if __name__=='__main__':
    filename1 = os.path.join("../../data/processed/scan_wifi-rdc.csv")
    df1=pd.read_csv(filename1)
    mean1=ComputeMean(df1)
    median1=ComputeMedian(df1)
    filename2 = os.path.join(os.getcwd(), "../../data/processed/scan_wifi-premier.csv")
    df2 = pd.read_csv(filename2)
    mean2 = ComputeMean(df2)
    median2 = ComputeMedian(df2)




