from segmentation import Segment
import sys

class PopulateDict:
    def __init__(self):
        self.s = Segment()
        self.s.process_image()

    def read_file(self, path):
        textfile = open(path, 'r')
        return textfile.readlines()

    def populate_dictionary(self, dict_to_populate, path):
        if dict_to_populate in ['asd','normal']:
            lines = self.read_file(path)
        else:
            sys.exit("Unexpected error occured while reading files")

        lines = lines[1:]  # to skip the first line

        for line in lines:
            element = line.split(",")
            visited_segments = []
            for key in self.s.segments.keys():
                if self.s.segments[key]['coordinates']['upper_x'] <= int(element[1]) <= \
                        self.s.segments[key]['coordinates']['lower_x'] and \
                        self.s.segments[key]['coordinates']['upper_y'] <= int(element[2]) <= \
                        self.s.segments[key]['coordinates']['lower_y']:
                    if key not in visited_segments:
                        visited_segments.append(key)
                        self.s.addPerson(key, dict_to_populate)
                    if int(element[0]) == 0:
                        visited_segments = []
                    self.s.addFixation(key, dict_to_populate)
                    self.s.addDuration(int(element[3]), key, dict_to_populate)
                    break
        # print(self.s.segments)

    def get_metric(self,element , metric, group):
        return self.s.segments[element][group][metric]

    def get_metric_for_image(self, metric, group):
        sum = 0
        for element in self.s.segments.keys():
            sum+=self.s.segments[element][group][metric]
        return sum