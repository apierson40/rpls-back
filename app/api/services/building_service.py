from ..models import Building


class BuildingService:
    """ Class to deal with building business logic """

    @staticmethod
    def create_building(
            building_entry,
            building_batiment,
            building_immeuble,
            building_compl,
            address_id):
        building = Building.objects.create(
            entry=building_entry,
            batiment=building_batiment,
            immeuble=building_immeuble,
            compl=building_compl,
            address_id=address_id
        )
        building.save()
        return building.id

    @staticmethod
    def find_building_by_attributes(
            building_entry,
            building_batiment,
            building_immeuble,
            building_compl,
            address_id
    ):
        try:
            return Building.objects.get(
                entry=building_entry,
                batiment=building_batiment,
                immeuble=building_immeuble,
                compl=building_compl,
                address_id=address_id
            )
        except Building.DoesNotExist:
            return None

    def find_or_create_building(
            self,
            building_entry,
            building_batiment,
            building_immeuble,
            building_compl,
            address_id
    ):
        building = self.find_building_by_attributes(
            building_entry,
            building_batiment,
            building_immeuble,
            building_compl,
            address_id
        )
        if building is not None:
            return building.id
        return self.create_building(
            building_entry,
            building_batiment,
            building_immeuble,
            building_compl,
            address_id
        )
