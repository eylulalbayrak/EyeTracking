import sys


class Segment:
    def __init__(self):
        segments = {
            "asd": {},
            "normal": {}
        }

    def check_segmentation_size(self):
        if not (int(sys.argv[4].split("x")[0]) in range(2, 5)) or not (int(sys.argv[4].split("x")[1]) in range(2, 5)):
            sys.exit("Segmentation size should be between 2x2 and 4x4")

    def get_image_size(self):
        width = int(sys.argv[3].split("x")[0])
        height = int(sys.argv[3].split("x")[1])
        return width, height

    def get_segmentation_size(self):
        rows = int(sys.argv[4].split("x")[0])
        columns = int(sys.argv[4].split("x")[1])
        return rows, columns

    def calculate_step_size(self, length, section):
        return length / section

    def grid_segmentation(self, width, height, rows, columns):
        segments = {}

        step_size_width = self.calculate_step_size(width, columns)
        step_size_height = self.calculate_step_size(height, rows)

        w = step_size_width
        h = step_size_height

        letter = 0

        for _ in range(0, rows):
            for _ in range(0, columns):
                segments[chr(letter + 65)] = w, h
                w += step_size_width
                letter += 1
            w = step_size_width
            h += step_size_height

        return segments

    def process_image(self):
        self.check_segmentation_size()
        rows, columns = self.get_segmentation_size()
        width, height = self.get_image_size()
        # print(self.grid_segmentation(width, height, rows, columns))
