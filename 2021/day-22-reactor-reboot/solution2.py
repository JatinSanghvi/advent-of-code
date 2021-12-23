import re


class Rect:
    def __init__(self, value, xmin, xmax, ymin, ymax, zmin, zmax):
        self.value, self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax = \
            value, xmin, xmax, ymin, ymax, zmin, zmax

    def intersect(self, region):
        xmin = max(self.xmin, region.xmin)
        ymin = max(self.ymin, region.ymin)
        zmin = max(self.zmin, region.zmin)
        xmax = min(self.xmax, region.xmax)
        ymax = min(self.ymax, region.ymax)
        zmax = min(self.zmax, region.zmax)

        return None if xmin >= xmax or ymin >= ymax or zmin >= zmax else Rect(-region.value, xmin, xmax, ymin, ymax, zmin, zmax)

    def volume(self):
        return self.value * (self.xmax - self.xmin) * (self.ymax - self.ymin) * (self.zmax - self.zmin)


def solve(path):
    with open(path) as file:
        lines = file.readlines()

    rects = []
    pattern = re.compile("(.*?) x=(.*?)\.\.(.*?),y=(.*?)\.\.(.*?),z=(.*?)\.\.(.*?)")
    for line in lines:
        match = pattern.fullmatch(line.rstrip())
        rects.append(Rect(1 if match[1] == "on" else 0, int(match[2]), int(match[3]) + 1, int(match[4]), int(match[5]) + 1, int(match[6]), int(match[7]) + 1))

    regions = []
    for rect in rects:
        regions += [intersection for region in regions if (intersection := rect.intersect(region)) != None]
        if rect.value == 1: regions += [rect]

    volume = sum(region.volume() for region in regions)
    print(volume)


solve("input-test-2.txt")
solve("input-test-3.txt")
solve("input.txt")
