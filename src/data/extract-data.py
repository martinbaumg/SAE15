#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse

def ExtractFolderName (path):
    return os.path.dirname(path)

def ExtractFileName (path):
    return os.path.basename(path)

def ExtractPlace (folderName) :
    return folderName.split('-')[1]

def ExtractDate (folderName) :
    date=folderName.split('-')[-1]
    return date

def ExtractIdExp (fileName) :
    IdExp = fileName.split('-')[-1]
    return IdExp

def ExtractSsid (content) :
    ssid=content.split("'")[0][:-1]
    return ssid

def ExtractMacAddr (content) :
    MacAddr = content.split("'")[1]
    return MacAddr
    
def ExtractRssi (content) :
    Rssi = content.split("'")[2]
    return Rssi

def ExtractInfo(path):
    folderName = ExtractFolderName(path) # Extract folder name
    fileName = ExtractFileName(path) # Extract filename
    result=""
    descRd = open(path, "r")
    contents = descRd.readlines()
    for content in contents:
        ssid=ExtractSsid(content)
        Addr=ExtractMacAddr(content)
        rssi=ExtractRssi(content)
        date=ExtractDate(folderName)
        IdExp=ExtractDate(fileName)
        place=ExtractPlace(folderName)
        result+=','.join([place,date,IdExp,ssid,Addr,rssi])
    descRd.close()
    return(result)



if __name__ == '__main__':
    # declare variables
    isFileCreated = False
    descWr = None
    result = ""
    folderName = ""
    fileName = ""

    # define arguments
    parser = argparse.ArgumentParser(description='Extract information from Wi-Fi logs')
    parser.add_argument("-input", help="path of the input file", required=True)
    args = parser.parse_args()
    if os.path.isfile(args.input):
        result = ExtractInfo(args.input)
        descWr = open("../../data/processed/wifi.csv","w")
        descWr.write("Location,Date,SSID,Addr,RSSI\n")
        descWr.write(result)
        descWr.close()
    elif os.path.isdir(args.input):
        listFiles = os.listdir(args.input)
        for fichier in listFiles:
            if isFileCreated == False:
                descWr = open("../../data/processed/wifi.csv","w")
                descWr.write("Building,Date,SSID,Addr,RSSI\n")
                descWr.close()
                isFileCreated = True

            result= ExtractInfo(os.path.join(args.input,fichier))
            descWr = open("../../data/processed/wifi.csv","a")
            descWr.write(result)
            descWr.close()
            result=""
    else :
        print("Erreur : le fichier ou le dossier n'existe pas")
        
