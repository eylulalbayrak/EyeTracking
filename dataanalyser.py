# Eye Tracking Data Analyzer
# by Eylul Begum Albayrak 2385110
# and Adam Mohamed I. K. 2350775

from population import PopulateDict
import sys
import matplotlib.pyplot as plt


def main():
    print("Expected Argument format: dataanalyser.py ",
          "[autism data file path] ",
          "[control data file path] ",
          "[image size]",
          "[grid size]")
    check_arg_length(sys.argv)
    p = PopulateDict()
    p.populate_dictionary('asd', sys.argv[1])
    p.populate_dictionary('normal', sys.argv[2])
    while (True):
        print_menu()
        try:
            choice = int(input())
        except:
            sys.exit("Invalid input!")

        if choice == 1:
            compare_for_element(p)
        elif choice == 2:
            compare_for_image(p)
        elif choice == 3:
            sys.exit()
        else:
            print("Invalid input!")


def print_menu():
    print("[1] Compare metric for a particular element of the image",
          "[2] Compare metric for whole image",
          "[3] Exit", sep='\n')


def compare_for_element(dictionary):
    metric = choose_metric()
    element = choose_element(dictionary)

    print_metric(dictionary, metric, element)


def compare_for_image(dictionary):
    metric = choose_metric()

    print_metric_for_image(dictionary, metric)


def choose_metric():
    print("[1] Total Number Of People",
          "[2] Total Time Viewed",
          "[3] Total Number of fixations", sep='\n')

    try:
        choice = int(input())
        if choice not in range(1, 4):
            sys.exit("Invalid Input!")
    except:
        sys.exit("Invalid Input!")

    attribute_names = {1: "total_people",
                       2: "total_duration",
                       3: "total_fixations"}

    return attribute_names[choice]


def choose_element(dictionary: PopulateDict):

    choice_num = 1
    elements = list(dictionary.s.segments.keys())
    print("You may enter the menu number or the case-insensitive letter of the segment")
    for element in elements:
        print(f"[{choice_num}] {element}")
        choice_num += 1

    choice = input()
    if choice.isdigit():
        choice = int(choice)-1
        return elements[choice]
    else:
        choice = choice.upper()
        if choice in elements:
            return choice
        else:
            sys.exit("Invalid Segment choice")


def print_metric_for_image(dictionary: PopulateDict, metric):
    groups = ["People with autism", "People without autism"]
    values = [dictionary.get_metric_for_image(metric, 'asd'),
              dictionary.get_metric_for_image(metric, 'normal')]

    plt.bar(groups, values)
    plt.xlabel("Groups")

    labels = {"total_fixation": "Total number of fixations",
              "total_people": "Total number of people",
              "total_duration": "Total time viewed"}
    plt.ylabel(labels[metric])
    plt.title(f"Comparison between people with and without autism for whole image")
    plt.show()


def print_metric(dictionary: PopulateDict, metric, element):

    groups = ["People with autism", "People without autism"]
    values = [dictionary.get_metric(element, metric, 'asd'),
              dictionary.get_metric(element, metric, 'normal')]

    plt.bar(groups, values)
    plt.xlabel("Groups")

    labels = {"total_fixation": "Total number of fixations",
              "total_people": "Total number of people",
              "total_duration": "Total time viewed"}
    plt.ylabel(labels[metric])
    plt.title(
        f"Comparison between people with and without autism for element {element}")
    plt.show()


def check_arg_length(args):
    if len(args) != 5:
        sys.exit("The number of arguments should be 4!")


if __name__ == '__main__':
    main()
