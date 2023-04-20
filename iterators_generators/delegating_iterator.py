"""You have custom class containing a list, tuple or other iterable and
want custom iteration on your new container"""


class SectionPointClouds:

    def __init__(self, section_id):
        self._section_id = section_id
        self._point_clouds = []

    def add_point_cloud(self, point_cloud):
        self._point_clouds.append(point_cloud)

    def __iter__(self):
        # the iter function only calls the __iter__ method inside the list
        # _point_clouds that implements the __next__ method
        return iter(self._point_clouds)

if __name__ == "__main__":
    section_point_clouds = SectionPointClouds(1)
    # I know point clouds are not like this simple example but lets focus
    # on the point here, :)
    section_point_clouds.add_point_cloud(0.23)
    section_point_clouds.add_point_cloud(0.55)
    section_point_clouds.add_point_cloud(0.33)
    # __iter__ method on SectionPointClouds is called when we try to iterate over
    # an object like here
    for point in section_point_clouds:
        print(point)
        # outputs 0.23 0.55 0.33


