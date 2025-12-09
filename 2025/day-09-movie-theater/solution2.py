def solve(path: str) -> None:
    with open(path, encoding="utf-8") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    points = [tuple(map(int, line.split(","))) for line in lines]

    max_area = 0
    for i1 in range(len(points)):
        x1, y1 = points[i1]
        for i2 in range(i1 + 1, len(points)):
            x2, y2 = points[i2]
            rect_xmin, rect_xmax = min(x1, x2), max(x1, x2)
            rect_ymin, rect_ymax = min(y1, y2), max(y1, y2)

            # Check if a segment intersects the rectangle.
            oseg_x, oseg_y = points[-1]
            for seg_x, seg_y in points:
                if seg_x == oseg_x:
                    if rect_xmin < seg_x < rect_xmax:
                        seg_ymin, seg_ymax = min(seg_y, oseg_y), max(seg_y, oseg_y)
                        if seg_ymax > rect_ymin and seg_ymin < rect_ymax:
                            break
                else:  # seg_y == oseg_y
                    if rect_ymin < seg_y < rect_ymax:
                        seg_xmin, seg_xmax = min(seg_x, oseg_x), max(seg_x, oseg_x)
                        if seg_xmax > rect_xmin and seg_xmin < rect_xmax:
                            break

                oseg_x, oseg_y = seg_x, seg_y
            else:
                max_area = max(max_area, (rect_xmax - rect_xmin + 1) * (rect_ymax - rect_ymin + 1))

    print(max_area)


solve("input-test.txt")  # 24
solve("input.txt")  # 1542119040
