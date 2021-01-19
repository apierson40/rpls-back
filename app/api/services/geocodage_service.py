from django.conf import settings
import requests
import pandas as pd
import numpy as np


class GeocodageService:

    @staticmethod
    def geocode_csv_data():

        # read csv
        csv_path = '/'.join([settings.STATIC_ROOT, 'rpls_cannes.csv'])
        df = pd.read_csv(csv_path, sep=';')
        df = df.replace({np.nan: None})

        # request params
        url = 'http://api-adresse.data.gouv.fr/search/'

        x = []
        y = []
        for index, row in df.iterrows():
            print('Traitement -> {} row'.format(index))

            # create q param
            voie = ''
            if row["NUMVOIE"] is not None:
                voie += row["NUMVOIE"]

            if row["INDREP"] is not None:
                voie += ' '
                voie += row["INDREP"]

            if row["TYPVOIE"] is not None:
                voie += ' '
                voie += row["TYPVOIE"]

            if row["NOMVOIE"] is not None:
                voie += ' '
                voie += row["NOMVOIE"]

            code_postal = ''.join(['0', str(row["CODEPOSTAL"])])

            # create all parameters
            params = {
                'q': voie,
                'postcode': code_postal,
                'limit': '1'
            }

            # send request
            res = requests.get(url=url, params=params)
            json = res.json()

            # save data
            if len(json['features']) > 0:
                x.append(json['features'][0]['properties']['x'])
                y.append(json['features'][0]['properties']['y'])
            else:
                x.append(None)
                y.append(None)

        # adding data to dataframe
        df['X'] = x
        df['Y'] = y

        # save as csv
        df.to_csv('/'.join([settings.STATIC_ROOT, 'rpls_cannes_geocoded_pierson.csv']))
        print('Geocoded csv created at {}'.format('/'.join([settings.STATIC_ROOT, 'rpls_cannes_geocoded_pierson.csv'])))
