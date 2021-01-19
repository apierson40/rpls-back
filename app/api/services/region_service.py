from ..models import Region


class RegionService:
    """ Class to deal with region business logic """

    @staticmethod
    def create_region(region_code, region_name):
        region = Region.objects.create(
            code=region_code,
            name=region_name
        )
        region.save()
        return region.id

    @staticmethod
    def find_region_by_code(region_code):
        try:
            return Region.objects.get(code=region_code)
        except Region.DoesNotExist:
            return None

    def find_or_create_region(self, region_code, region_name):
        region = self.find_region_by_code(region_code)
        if region is not None:
            return region.id
        return self.create_region(region_code, region_name)
