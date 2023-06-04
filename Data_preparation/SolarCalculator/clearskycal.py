import numpy as np
import pandas as pd

class calsolar:

    def cal_zna(df, lat, lon):
        phi = lat
        doy_list = df.index.dayofyear
        hour_list = df.index.hour
        minute_list = df.index.minute
        zna_list = []
        for i in range(len(df.index)):
            time_vector = hour_list[i] + minute_list[i] / 60  # cal solar hour
            B = (360/365)*(doy_list[i] - 81)
            LSTM = 15*7
            EoT = 9.87*np.sin(2*B*np.pi/180)-7.53*np.cos(B*np.pi/180)-1.5*np.sin(B*np.pi/180)
            TC = 4*(lon-LSTM)+EoT
            LST = time_vector + TC/60
            HRA = 15*abs(LST-12)
            delta= -23.45*np.cos(2*np.pi*(doy_list[i]+10)/365)
            zna = np.sin(delta*np.pi/180)*np.sin(phi*np.pi/180) + np.cos(delta*np.pi/180)*np.cos(phi*np.pi/180)*np.cos(HRA*np.pi/180)
            zna_list.append(zna)
        return zna_list
    
    def cal_airmass(df, lat, lon):
        phi = lat
        doy_list = df.index.dayofyear
        hour_list = df.index.hour
        minute_list = df.index.minute
        am_list = []
        for i in range(len(df.index)):
            time_vector = hour_list[i] + minute_list[i] / 60  # cal solar hour
            B = (360/365)*(doy_list[i] - 81)
            LSTM = 15*7
            EoT = 9.87*np.sin(2*B*np.pi/180)-7.53*np.cos(B*np.pi/180)-1.5*np.sin(B*np.pi/180)
            TC = 4*(lon-LSTM)+EoT
            LST = time_vector + TC/60
            HRA = 15*abs(LST-12)
            delta= -23.45*np.cos(2*np.pi*(doy_list[i]+10)/365)
            x = np.sin(delta*np.pi/180)*np.sin(phi*np.pi/180) + np.cos(delta*np.pi/180)*np.cos(phi*np.pi/180)*np.cos(HRA*np.pi/180)
            x[x<0] = 0
            AM = 1 / (x + 0.50572 * (96.07995 - np.degrees(np.arccos(x))) ** -1.6364)
            am_list.append(AM)
        return am_list
    
    def cal_clearsky(df, lat, lon, alt):
        phi = lat
        doy_list = df.index.dayofyear
        hour_list = df.index.hour
        minute_list = df.index.minute
        iclr_list = []
        for i in range(len(df.index)):
            time_vector = hour_list[i] + minute_list[i] / 60  # cal solar hour
            B = (360/365)*(doy_list[i] - 81)
            LSTM = 15*7
            EoT = 9.87*np.sin(2*B*np.pi/180)-7.53*np.cos(B*np.pi/180)-1.5*np.sin(B*np.pi/180)
            TC = 4*(lon-LSTM)+EoT
            LST = time_vector + TC/60
            HRA = 15*abs(LST-12)
            delta= -23.45*np.cos(2*np.pi*(doy_list[i]+10)/365)
            x = np.sin(delta*np.pi/180)*np.sin(phi*np.pi/180) + np.cos(delta*np.pi/180)*np.cos(phi*np.pi/180)*np.cos(HRA*np.pi/180)
            x[x<0] = 0
            #TL = 5.124
            TL = 4.773765928887537
            f1 = np.e ** (-alt / 8000)
            f2 = np.e ** (-alt / 1250)
            a1 = (alt * 5.09e-5) + 0.868
            a2 = (alt * 3.92e-5) + 0.0387
            Isc = 1366.1
            AM = 1 / (x + 0.50572 * (96.07995 - np.degrees(np.arccos(x))) ** -1.6364)
            iclr_list.append(a1 * Isc * x * np.e ** (-a2 * AM * (f1 + f2 * (TL - 1))))
        return iclr_list 