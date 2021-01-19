from django.contrib.gis.geos import Point
from ..models import Housing


class HousingService:
    """ Class to deal with business housing logic """

    @staticmethod
    def create_housing(
            housing_num_apartment,
            housing_num_box,
            housing_staircase,
            housing_hall,
            housing_floor,
            housing_compl,
            housing_qpv,
            housing_type_const,
            housing_nb_piece,
            housing_surface,
            housing_construct,
            housing_locate,
            housing_patrimoine,
            housing_origine,
            housing_finanture,
            housing_conv,
            housing_num_conv,
            housing_sru_expir,
            housing_date_conv,
            housing_new_logt,
            housing_dpe_date,
            housing_dpe_energie,
            housing_dpe_serre,
            housing_sru_alinea,
            housing_code_seg_patrim,
            housing_seg_patrim,
            housing_cus,
            housing_droit,
            housing_x,
            housing_y,
            address_id,
            building_id
    ):
        geom = None
        if housing_x is not None and housing_y is not None:
            geom = Point(x=housing_x, y=housing_y, srid=2154)

        housing = Housing.objects.create(
            num_apartment=housing_num_apartment,
            num_box=housing_num_box,
            staircase=housing_staircase,
            hall=housing_hall,
            floor=housing_floor,
            compl=housing_compl,
            qpv=housing_qpv,
            type_const=housing_type_const,
            nb_piece=housing_nb_piece,
            surface=housing_surface,
            construct=housing_construct,
            locate=housing_locate,
            patrimoine=housing_patrimoine,
            origine=housing_origine,
            finanture=housing_finanture,
            conv=housing_conv,
            num_conv=housing_num_conv,
            sru_expir=housing_sru_expir,
            date_conv=housing_date_conv,
            new_logt=housing_new_logt,
            dpe_date=housing_dpe_date,
            dpe_energie=housing_dpe_energie,
            dpe_serre=housing_dpe_serre,
            sru_alinea=housing_sru_alinea,
            code_seg_patrim=housing_code_seg_patrim,
            lib_seg_patrim=housing_seg_patrim,
            cus=housing_cus,
            droit=housing_droit,
            lon=housing_x,
            lat=housing_y,
            geom=geom,
            address_id=address_id,
            building_id=building_id,
        )
        housing.save()
        return housing.id

    @staticmethod
    def find_housing_by_id(housing_id):
        try:
            return Housing.objects.get(id=housing_id)
        except Housing.DoesNotExist:
            return None

    @staticmethod
    def find_housing_lon_lat_by_id(housing_id):
        try:
            housing = Housing.objects.get(id=housing_id)
            return housing.lon, housing.lat
        except Housing.DoesNotExist:
            return None

    @staticmethod
    def adding_parcel_id(housing_id, parcel_id):
        housing = Housing.objects.get(id=housing_id)
        housing.parcel_id = parcel_id
        housing.save()

    @staticmethod
    def find_housing_by_attributes(
            housing_num_apartment,
            housing_num_box,
            housing_staircase,
            housing_hall,
            housing_floor,
            housing_compl,
            housing_qpv,
            housing_type_const,
            housing_nb_piece,
            housing_surface,
            housing_construct,
            housing_locate,
            housing_patrimoine,
            housing_origine,
            housing_finanture,
            housing_conv,
            housing_num_conv,
            housing_sru_expir,
            housing_date_conv,
            housing_new_logt,
            housing_dpe_date,
            housing_dpe_energie,
            housing_dpe_serre,
            housing_sru_alinea,
            housing_code_seg_patrim,
            housing_seg_patrim,
            housing_cus,
            housing_droit,
            housing_x,
            housing_y,
            address_id,
            building_id
    ):
        try:
            return Housing.objects.get(
                num_apartment=housing_num_apartment,
                num_box=housing_num_box,
                staircase=housing_staircase,
                hall=housing_hall,
                floor=housing_floor,
                compl=housing_compl,
                qpv=housing_qpv,
                type_const=housing_type_const,
                nb_piece=housing_nb_piece,
                surface=housing_surface,
                construct=housing_construct,
                locate=housing_locate,
                patrimoine=housing_patrimoine,
                origine=housing_origine,
                finanture=housing_finanture,
                conv=housing_conv,
                num_conv=housing_num_conv,
                sru_expir=housing_sru_expir,
                date_conv=housing_date_conv,
                new_logt=housing_new_logt,
                dpe_date=housing_dpe_date,
                dpe_energie=housing_dpe_energie,
                dpe_serre=housing_dpe_serre,
                sru_alinea=housing_sru_alinea,
                code_seg_patrim=housing_code_seg_patrim,
                lib_seg_patrim=housing_seg_patrim,
                cus=housing_cus,
                droit=housing_droit,
                lon=housing_x,
                lat=housing_y,
                address_id=address_id,
                building_id=building_id,
            )
        except Housing.DoesNotExist:
            return None

    def find_or_create_housing(
            self,
            housing_num_apartment,
            housing_num_box,
            housing_staircase,
            housing_hall,
            housing_floor,
            housing_compl,
            housing_qpv,
            housing_type_const,
            housing_nb_piece,
            housing_surface,
            housing_construct,
            housing_locate,
            housing_patrimoine,
            housing_origine,
            housing_finanture,
            housing_conv,
            housing_num_conv,
            housing_sru_expir,
            housing_date_conv,
            housing_new_logt,
            housing_dpe_date,
            housing_dpe_energie,
            housing_dpe_serre,
            housing_sru_alinea,
            housing_code_seg_patrim,
            housing_seg_patrim,
            housing_cus,
            housing_droit,
            housing_x,
            housing_y,
            address_id,
            building_id
    ):
        housing = self.find_housing_by_attributes(
            housing_num_apartment,
            housing_num_box,
            housing_staircase,
            housing_hall,
            housing_floor,
            housing_compl,
            housing_qpv,
            housing_type_const,
            housing_nb_piece,
            housing_surface,
            housing_construct,
            housing_locate,
            housing_patrimoine,
            housing_origine,
            housing_finanture,
            housing_conv,
            housing_num_conv,
            housing_sru_expir,
            housing_date_conv,
            housing_new_logt,
            housing_dpe_date,
            housing_dpe_energie,
            housing_dpe_serre,
            housing_sru_alinea,
            housing_code_seg_patrim,
            housing_seg_patrim,
            housing_cus,
            housing_droit,
            housing_x,
            housing_y,
            address_id,
            building_id
        )
        if housing is not None:
            return housing.id
        return self.create_housing(
            housing_num_apartment,
            housing_num_box,
            housing_staircase,
            housing_hall,
            housing_floor,
            housing_compl,
            housing_qpv,
            housing_type_const,
            housing_nb_piece,
            housing_surface,
            housing_construct,
            housing_locate,
            housing_patrimoine,
            housing_origine,
            housing_finanture,
            housing_conv,
            housing_num_conv,
            housing_sru_expir,
            housing_date_conv,
            housing_new_logt,
            housing_dpe_date,
            housing_dpe_energie,
            housing_dpe_serre,
            housing_sru_alinea,
            housing_code_seg_patrim,
            housing_seg_patrim,
            housing_cus,
            housing_droit,
            housing_x,
            housing_y,
            address_id,
            building_id
        )
