# ms17_010_Hunter by dangrimm
A simple script that converts netdiscover's output in nmap ip list input to check for ms17_010 remote vulnerability. It then
runs the smb-vuln-ms17-010.nse nmap script to determine if there are vulnerable hosts among the ones in the input ip list.
If you don't know about the remote code execution vulnerability, refer to https://support.microsoft.com/en-us/help/4013389/title.

For the script to work, you must have Alexandre Norman's nmap python module installed. (http://xael.org/pages/python-nmap-en.html)
To install it on Kali Linux, just run:

  root@kali: ~# pip install python-nmap

You must also have nmap's smb-vuln-ms17-010.nse script on your nmap/scripts folder.

Usage:

The input file can be, for example, a Netdiscover scan output. I personally use

root@kali: ~# netdiscover -P -N > ip_list.txt

Then, 

root@kali: ~# python ipHunter.py -i ip_list.txt

The script will then run a nmap scan with the following arguments:

-Pn -sC -p 445 -max-hostgroup 3 -open -script smb-vuln-ms17-010.nse <ip_list>

After the scan, it will return the IP addresses of the vulnerable hosts for exploitation and an output file.
