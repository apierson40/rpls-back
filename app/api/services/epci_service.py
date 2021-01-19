from ..models.department import Department
from ..models.epci import EPCI


class EPCIService:
    """ Class to deal with epci business logic """

    @staticmethod
    def create_epci(epci_code, epci_name, department_id):
        department = Department.objects.get(id=department_id)
        epci = EPCI(
            code=epci_code,
            name=epci_name,
        )
        epci.save()
        epci.departments.add(department)
        epci.save()
        return epci.id

    @staticmethod
    def find_epci_by_code(epci_code):
        try:
            return EPCI.objects.get(code=epci_code)
        except EPCI.DoesNotExist:
            return None

    def find_or_create_epci(self, epci_code, epci_name, department_id):
        epci = self.find_epci_by_code(department_id)
        if epci is not None:
            return epci.id
        return self.create_epci(epci_code, epci_name, department_id)
