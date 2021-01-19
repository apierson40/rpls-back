from ..models import Address


class AddressService:
    """ Class to deal with address business logic """

    @staticmethod
    def create_address(
            address_num,
            address_repetition_indice,
            address_type,
            address_name,
            address_locality,
            address_postal_code,
            city_id):
        address = Address.objects.create(
            num=address_num,
            repetition_indice=address_repetition_indice,
            type=address_type,
            name=address_name,
            locality=address_locality,
            postal_code=address_postal_code,
            city_id=city_id
        )
        address.save()
        return address.id

    @staticmethod
    def find_address_by_attributes(
            address_num,
            address_repetition_indice,
            address_type,
            address_name,
            address_locality,
            address_postal_code,
            city_id
    ):
        try:
            return Address.objects.get(
                num=address_num,
                repetition_indice=address_repetition_indice,
                type=address_type,
                name=address_name,
                locality=address_locality,
                postal_code=address_postal_code,
                city_id=city_id
            )
        except Address.DoesNotExist:
            return None

    def find_or_create_address(
            self,
            address_num,
            address_repetition_indice,
            address_type,
            address_name,
            address_locality,
            address_postal_code,
            city_id):
        address = self.find_address_by_attributes(
            address_num,
            address_repetition_indice,
            address_type,
            address_name,
            address_locality,
            address_postal_code,
            city_id
        )
        if address is not None:
            return address.id
        return self.create_address(
            address_num,
            address_repetition_indice,
            address_type,
            address_name,
            address_locality,
            address_postal_code,
            city_id
        )
