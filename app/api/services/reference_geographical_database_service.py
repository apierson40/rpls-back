import psycopg2


class ReferenceGeographicalDatabaseService:

    @staticmethod
    def connect_to_external_pg_database():
        """
        host: 35.240.91.249
        port: 5432
        database: geodude
        user: pierson
        password: ae6chongu2YuaV
        """
        return psycopg2.connect(
            host="35.240.91.249",
            port="5432",
            database="geodude",
            user="pierson",
            password="ae6chongu2YuaV",
            options="-c search_path=public,geo"
        )

    def get_parcelle_from_housing_lon_lat(self, lon, lat):
        connexion = self.connect_to_external_pg_database()
        cursor = connexion.cursor()

        cursor.execute('''SELECT id, ST_AsText(ST_Transform(geom, 2154)) FROM geo_parcelle2 WHERE ST_Contains(ST_Transform(geom, 2154), ST_PointFromText('POINT(%s %s)', 2154));''', (lon, lat))
        result = [x for x in cursor.fetchall()]
        parcel_id = None
        parcel_geom = None
        if len(result) > 0:
            parcel_id, parcel_geom = result[0]

        cursor.close()
        connexion.close()
        return parcel_id, parcel_geom

    def get_commune_centroid(self):
        connexion = self.connect_to_external_pg_database()
        cursor = connexion.cursor()

        cursor.execute('''SELECT ST_AsText(ST_Transform(ST_Centroid(geom), 2154)) FROM geo_place2 WHERE id=2199;''')
        result = [x[0] for x in cursor.fetchall()][0]

        cursor.close()
        connexion.close()
        return result
