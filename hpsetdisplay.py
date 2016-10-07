#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a simple Python implementation of some C# code I discovered a few years ago at:
http://odetocode.com/humor/68.aspx
see also: http://miscellany.kovaya.com/2007/10/insert-coin.html for a version in Perl
Example usage:
$python hphack.py 192.168.0.100 "Insert Coin" """

import socket
import sys

def main(host, message, port=9100):
   send_string = unicode("\x1B%-12345X@PJL RDYMSG DISPLAY = \"" + message + "\"\r\n\x1B%-12345X\r\n", 'utf-8')
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
   try:
      s.connect((host, port))
   except socket.error as err:
      sys.stderr.write("Unable to connect to %s [%s].\r\n" % (host, strerror))
      return 1
   s.send(bytearray(send_string))
   s.close()

if __name__ == '__main__':
   if len(sys.argv) < 3:
      print ("Usage: %s <IP address> \"Message\"" % (sys.argv[0]))
      exit(1)
   main(sys.argv[1], sys.argv[2])
