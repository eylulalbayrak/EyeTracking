import sys
from segmentation import Segment


class PopulateDict:
    def __init__(self):
        self.s = Segment()
        self.s.process_image()

    def args_length(self):
        if len(sys.argv) != 5:
            sys.exit("The number of arguments should be 4!")

    def read_autism(self):
        textfile = open('./TextFiles/' + sys.argv[1], 'r')
        return textfile.readlines()

    def read_normal(self):
        textfile = open('./TextFiles/' + sys.argv[2], 'r')
        return textfile.readlines()

    def populate_dictionary(self, filename):
        if filename == 'asd':
            lines = self.read_autism()
        elif filename == 'normal':
            lines = self.read_normal()
        else:
            sys.exit("No text file named" + filename)

        lines = lines[1:len(lines)]  # to skip the first line

        for line in lines:
            element = line.split(",")
            for key in self.s.segments.keys():
                if self.s.segments[key]['coordinates']['upper_x'] <= int(element[1]) <= \
                        self.s.segments[key]['coordinates']['lower_x'] and \
                        self.s.segments[key]['coordinates']['upper_y'] <= int(element[2]) <= \
                        self.s.segments[key]['coordinates']['lower_y']:
                    if int(element[0]) == 0:
                        self.s.addPerson(key, filename)
                    self.s.addFixation(key, filename)
                    self.s.addDuration(int(element[3]), key, filename)
                    break
        # print(self.s.segments)