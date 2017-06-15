import re
import sys
import getopt
import nmap


def main(argv):
    print """
=============================================
WELCOME TO MS17-010 VULNERABILITY HOST HUNTER
============================================="""
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    except getopt.GetoptError:
        print 'ipHunter.py -i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ipHunter.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
    ip_listing(input_file)


def ip_listing(ip_file):
    host_list = ""
    final_file = open("ip_final_list.txt", 'w')
    ok_flag = False
    with open(ip_file) as in_file:
        for line in in_file:
            ip = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            if ip:
                ip_var = ', '.join(ip) + " "
                final_file.write(ip_var)
                host_list += ip_var
                ok_flag = True
        final_file.close()
        if ok_flag:
            do_nmap(host_list)
            print """
----------------------------------
Generated a list of IPs on the network for further scanning (.txt format): ip_final_list.txt
----------------------------------

----------------------------------
And a list of vulnerable hosts (.txt format): vuln_list.txt
----------------------------------

"""
        else:
            print """
-------------------------------
IP list generation failed!!! =/
-------------------------------

>>> No ip addresses were found on the given file input...

"""


def do_nmap(host_list):
    vuln_list = open("vuln_list.txt", "w")
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 445 -max-hostgroup 3 -open -script smb-vuln-ms17-010.nse')
    print """
**************************
POSSIBLE VULNERABLE HOSTS:
**************************
"""
    for host in nm.all_hosts():
        print str(host) + " // " + "VULNERABLE"
        vuln_list.write(str(host))
    vuln_list.close()

if __name__ == "__main__":
    main(sys.argv[1:])
