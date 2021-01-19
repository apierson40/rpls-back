from ..models import City


class CityService:
    """ Class to deal with city business logic """

    @staticmethod
    def create_city(city_code, city_name, department_id, epci_id):
        city = City.objects.create(
            code=city_code,
            name=city_name,
            department_id=department_id,
            epci_id=epci_id
        )
        city.save()
        return city.id

    @staticmethod
    def find_city_by_code(city_code):
        try:
            return City.objects.get(code=city_code)
        except City.DoesNotExist:
            return None

    def find_or_create_city(self, city_code, city_name, department_id, epci_id):
        city = self.find_city_by_code(city_code)
        if city is not None:
            return city.id
        return self.create_city(city_code, city_name, department_id, epci_id)
