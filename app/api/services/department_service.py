from ..models import Department


class DepartmentService:
    """ Class to deal with department business logic """

    @staticmethod
    def create_department(department_code, department_name, region_id):
        department = Department(
            code=department_code,
            name=department_name,
            region_id=region_id
        )
        department.save()
        return department.id

    @staticmethod
    def find_department_by_code(department_code):
        try:
            return Department.objects.get(code=department_code)
        except Department.DoesNotExist:
            return None

    def find_or_create_department(self, department_code, department_name, region_id):
        department = self.find_department_by_code(department_code)
        if department is not None:
            return department.id
        return self.create_department(department_code, department_name, region_id)
