from .region_service import RegionService
from .department_service import DepartmentService
from .epci_service import EPCIService
from .city_service import CityService
from .address_service import AddressService
from .building_service import BuildingService
from .parcel_service import ParcelService
from .housing_service import HousingService
from .reference_geographical_database_service import ReferenceGeographicalDatabaseService

import pandas as pd
import numpy as np
from django.conf import settings


class DataIntegrationService:

    @staticmethod
    def integrate_geocoded_csv_data():

        # adding services
        region_service = RegionService()
        department_service = DepartmentService()
        epci_service = EPCIService()
        city_service = CityService()
        address_service = AddressService()
        building_service = BuildingService()
        parcel_service = ParcelService()
        housing_service = HousingService()
        reference_database_service = ReferenceGeographicalDatabaseService()

        # import and read geocoded csv
        csv_path = '/'.join([settings.STATIC_ROOT, 'results/rpls_cannes_geocoded.csv'])
        df = pd.read_csv(csv_path)

        # replace nan value by None
        df = df.replace({np.nan: None})

        # find centroid of commune
        centroid = reference_database_service.get_commune_centroid()

        # iter through csv and integrate datas
        for index, row in df.iterrows():
            print('Row index -> {}'.format(index))

            # deal with region data
            region_id = region_service.find_or_create_region(row["REG"], row["LIBREG"])

            # deal with department data
            department_id = department_service.find_or_create_department(row["DEP"], row["LIBDEP"], region_id)

            # deal with epci data
            epci_id = epci_service.find_or_create_epci(row["EPCI"], row["LIBEPCI"], department_id)

            # deal with city data
            city_id = city_service.find_or_create_city(
                ''.join(['0', str(row["DEPCOM"])]),
                row["LIBCOM"],
                department_id,
                epci_id
            )

            # deal with address data
            address_id = address_service.find_or_create_address(
                row["NUMVOIE"],
                row["INDREP"],
                row["TYPVOIE"],
                row["NOMVOIE"],
                row["LIEUDIT"],
                ''.join(['0', str(row["CODEPOSTAL"])]),
                city_id
            )

            # deal with building data
            building_id = None
            if not (row["ENTREE"] is None and row["BAT"] is None and row["BAT"] is None and row["COMPLGEO"] is None):
                building_id = building_service.find_or_create_building(
                    row["ENTREE"],
                    row["BAT"],
                    row["IMMEU"],
                    row["COMPLGEO"],
                    address_id
                )

            # deal with housing data
            housing_id = housing_service.create_housing(
                row["NUMAPPT"],
                row["NUMBOITE"],
                row["ESC"],
                row["COULOIR"],
                row["ETAGE"],
                row["COMPLIDENT"],
                row["QPV"],
                row["TYPECONST"],
                row["NBPIECE"],
                row["SURFHAB"],
                row["CONSTRUCT"],
                row["LOCAT"],
                row["PATRIMOINE"],
                row["ORIGINE"],
                row["FINANAUTRE"],
                row["CONV"],
                row["NUMCONV"],
                row["SRU_EXPIR"],
                row["DATCONV"],
                row["NEWLOGT"],
                row["DPEDATE"],
                row["DPEENERGIE"],
                row["DPESERRE"],
                row["SRU_ALINEA"],
                row["CODSEGPATRIM"],
                row["LIBSEGPATRIM"],
                row["CUS"],
                row["DROIT"],
                row["X"],
                row["Y"],
                address_id,
                building_id
            )

            housing_lon, housing_lat = housing_service.find_housing_lon_lat_by_id(housing_id)
            if housing_lon is not None and housing_lat is not None:

                # seach parcel where housing belong
                parcel_id, parcel_geom = reference_database_service.get_parcelle_from_housing_lon_lat(housing_lon, housing_lat)

                # if housing belong to a parcel, adding parcel infos to database
                if parcel_id is not None:
                    parcel_id_db = parcel_service.find_parcel_by_id(parcel_id)
                    if parcel_id_db is None:
                        parcel_service.create_parcel(parcel_id, parcel_geom)
                    else:
                        parcel_service.increment_housing_count_from_parcel_id(parcel_id)
                    housing_service.adding_parcel_id(housing_id, parcel_id)
