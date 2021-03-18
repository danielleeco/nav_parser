#!/usr/bin/env python
# coding: utf-8

import pandas as pd


def preprocessing():
    the_file = []
    with open('gps_all', 'r', encoding='Windows-1251') as file:
        for line in file:
            the_file.append(line)

    for i in range(len(the_file)):
        if the_file[i][0] != '$':
            the_file[i] = ''
        the_file[i] = the_file[i].strip()

    the_file = [i.split(',') for i in the_file if len(i) > 5]
    the_file = [x for x in the_file if x]

    db = {
        '$GPGGA': {
            'items': [],
            'keys': ['UTC', 'latitude', 'direction_NS', 'longitude',
                     'direction_EW', 'GPS_quality', 'num_of_SV', 'HDOP', 'MSL',
                     'M_high', 'geoid_sep', 'M_geoid_sep', 'age', 'refstation']
        },

        '$GPGSA': {
            'items': [],
            'keys': ['mode_1', 'mode_2', 'prn_number', 'PDOP', 'HDOP',
                     'VDOP', 'ID_1', 'ID_2', 'ID_3', 'ID_4', 'ID_5',
                     'ID_6', 'ID_7', 'ID_8', 'PDOP', 'HDOP', 'VDOP']
        },

        '$GPGSV': {
            'items': [],
            'keys': ['num_of_msgs', 'num', 'total_num', 'SV_PRN',
                     'elevation', 'azimuth', 'SNR', 'second_SV_2', 'second_3',
                     'second_SV_4', 'third_SV_1', 'third_SV_2', 'third_SV_3',
                     'third_SV_4', 'fourth_SV_1', 'fourth_SV_2',
                     'fourth_SV_3', 'fourth_SV_4', 'checksum']
        },

        '$GPRMC': {
            'items': [],
            'keys': ['UTC', 'data_status', 'latitude', 'NS',
                     'longitude', 'EW', 'speed', 'track_',
                     'UT_date', 'magn', 'EW_', 'checksum']
        }

    }

    for line in the_file:
        types = line[0]
        db[types]['items'].append(line[1:])

    db_pd = dict()
    for key in db:
        db_pd[key] = pd.DataFrame(db[key]['items'],
                                  columns=db[key]['keys'], dtype=float)

    for key in db_pd:
        print(db_pd[key])
    return (db_pd)
