from ..models import Parcel


class ParcelService:
    """ Class to deal with parcel business logic """

    @staticmethod
    def create_parcel(parcel_id, parcel_geom):
        parcel = Parcel.objects.create(
            id=parcel_id,
            geom=parcel_geom,
            housing_count=1
        )
        parcel.save()
        return parcel.id

    @staticmethod
    def find_parcel_by_id(parcel_id):
        try:
            return Parcel.objects.get(id=parcel_id)
        except Parcel.DoesNotExist:
            return None

    def find_or_create_parcel(self, parcel_id, parcel_geom):
        parcel = self.find_parcel_by_id(parcel_id)
        if parcel is not None:
            return parcel.id
        return self.create_parcel(parcel_id, parcel_geom)

    def increment_housing_count_from_parcel_id(self, parcel_id):
        parcel = self.find_parcel_by_id(parcel_id)
        parcel.housing_count = parcel.housing_count + 1
        parcel.save()
