import argparse

def report_vowels_count(input):
    count = []
    for vowel in "aeiouy":
      count.append( (vowel,input.count(vowel)) )
    return count

def count_vowels(input):
    count = 0
    for char in input:
      count += "aeiouy".count(char)
    return count


def main():
    parser = argparse.ArgumentParser(prog='vowels',description='Count the numbers of vowels in INPUT')
    parser.add_argument('input', metavar='INPUT')
    parser.add_argument('-r', '--report', help="report a sum of each vowel found", action='store_true')      # option that takes a value
    
    args = parser.parse_args()
    if(args.report):
        report = report_vowels_count(args.input)
        for k,v in report:
            if(v == 0):
                continue
            print(f"The vowel {k} appears {v} times in `{args.input}`")
        exit(0)
    vowels_count = count_vowels(args.input)
    print(vowels_count)

if(__name__ == "__main__"):
    main()