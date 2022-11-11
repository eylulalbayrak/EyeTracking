import sys


class Segment:
    def __init__(self):
        self.segments = dict()

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
        step_size_width = self.calculate_step_size(width, columns)
        step_size_height = self.calculate_step_size(height, rows)

        upper_w, upper_h = 0, 0
        lower_w, lower_h = step_size_width, step_size_height

        letter = 0

        for _ in range(0, rows):
            for _ in range(0, columns):
                self.segments[chr(letter + 65)] = {
                    'coordinates': {
                        'upper_x': upper_w,
                        'upper_y': upper_h,
                        'lower_x': lower_w,
                        'lower_y': lower_h,
                    },
                    'asd': {
                        'total_fixations': 0,
                        'total_people': 0,
                        'total_duration': 0
                    },
                    'normal': {
                        'total_fixations': 0,
                        'total_people': 0,
                        'total_duration': 0
                    }
                }
                upper_w = lower_w
                lower_w += step_size_width
                letter += 1
            upper_w = 0
            lower_w = step_size_width
            upper_h = lower_h
            lower_h += step_size_height

        return self.segments

    def process_image(self):
        self.check_segmentation_size()
        rows, columns = self.get_segmentation_size()
        width, height = self.get_image_size()
        self.grid_segmentation(width, height, rows, columns)

    def addFixation(self, letter, file):
        total_fixations = self.segments[letter][file]['total_fixations'] + 1
        self.segments[letter][file]['total_fixations'] = total_fixations

    def addDuration(self, duration, letter, file):
        total_duration = self.segments[letter][file]['total_duration'] + duration
        self.segments[letter][file]['total_duration'] = total_duration

    def addPerson(self, letter, file):
        total_people = self.segments[letter][file]['total_people'] + 1
        self.segments[letter][file]['total_people'] = total_people


