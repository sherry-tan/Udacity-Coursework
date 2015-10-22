#!/usr/bin/env python
# -*- coding: utf-8 -*-
# So, the problem is that the gigantic file is actually not a valid XML, because
# it has several root elements, and XML declarations.
# It is, a matter of fact, a collection of a lot of concatenated XML documents.
# So, one solution would be to split the file into separate documents,
# so that you can process the resulting files as valid XML documents.

import xml.etree.ElementTree as ET
PATENTS = 'patent.data'

def get_root(fname):
    tree = ET.parse(fname)
    return tree.getroot()


def split_file(filename):
    # we want you to split the input file into separate files
    # each containing a single patent.
    # As a hint - each patent declaration starts with the same line that was causing the error
    # The new files should be saved with filename in the following format:
    # "{}-{}".format(filename, n) where n is a counter, starting from 0.
    
    n = 0
    
    #short solution 2nd try
    with open(filename, "r") as f:
        for line in f:
            if line.startswith("<?xml"):
                name = "%s-%d"%(filename, n)
                out = open(name,'w')
                out.write(line)
                n += 1
            out.write(line)
       

       
 
#last_pos = fp.tell()
#line = fp.readline()
#while line != '':
 # if line == 'SPECIAL':
  #  fp.seek(last_pos)
   # other_function(fp)
    #break
  #ast_pos = fp.tell()
  #line = fp.readline()       

  # with open(filename, "r") as f:
   #     lines = f.readlines()
   
    
    #for j, line in enumerate(lines):
     #   if line.startswith("<?xml"):
      #     index.append(j)
    #index.append(len(lines)-1)
    
    #for i in range(len(index)-1):
     #   name = "%s-%d"%(filename, i)
      #  out = open(name,'w')
       # for a in range(index[i], index[i+1]):
        #    out.write(lines[a])
       
    pass


def test():
    split_file(PATENTS)
    for n in range(4):
        try:
            fname = "{}-{}".format(PATENTS, n)
            f = open(fname, "r")
            if not f.readline().startswith("<?xml"):
                print "You have not split the file {} in the correct boundary!".format(fname)
            f.close()
        except:
            print "Could not find file {}. Check if the filename is correct!".format(fname)


test()