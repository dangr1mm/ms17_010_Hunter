import re
import sys
import getopt


def main(argv):
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'test.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
            print 'Input file is ', input_file
    ip_listing(input_file)


def ip_listing(ip_file):
    final_file = open("ip_final_list.txt", 'w')
    ok_flag = False
    with open(ip_file) as in_file:
        for line in in_file:
            ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            if ip:
                ip_var = ', '.join(ip) + "\n"
                final_file.write(ip_var)
                ok_flag = True
        final_file.close()
        if ok_flag:
            print """
----------------------------------
IP list generation succeeded!!! =D
----------------------------------

>> File name: ip_final_list.txt"""
        else:
            print """
-------------------------------
IP list generation failed!!! =/
-------------------------------

>>> No ip addresses were found on the given file input..."""


if __name__ == "__main__":
    main(sys.argv[1:])
