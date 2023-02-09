#!/usr/bin/env python3
'''Assignment 4 Part 2 template'''
print(__doc__)

from typing import IO
import random as rand

class GenRandom:
    '''Class GenRandom'''
    def Setting(self,s,e):
        b = rand.randrange(s,e,1)
        return b

    def fl(self,v,c):
        h= round(rand.uniform(v,c),1)
        return h

def main():
    '''main method'''
    l =["CNT", "SHA", "X","Y","RAD","Rx","Ry","W","H","R","G","B","OP"]
    g = GenRandom()
    b = []
    b.append(l)
    for i in range(10):
        b.append([i,g.Setting(0,3),g.Setting(0,500),g.Setting(0,500),g.Setting(0,100),g.Setting(10,30),g.Setting(10,30),g.Setting(10,100),g.Setting(10,100),g.Setting(0,255),g.Setting(0,255),g.Setting(0,255),g.fl(0.0,1.0)])
    for item in b:
        print(str(item[0]).rjust(5), str(item[1]).rjust(5),str(item[2]).rjust(5),str(item[3]).rjust(5), str(item[4]).rjust(5),str(item[5]).rjust(5),str(item[6]).rjust(5),str(item[7]).rjust(5),str(item[8]).rjust(5),str(item[9]).rjust(5),str(item[10]).rjust(5),str(item[11]).rjust(5),str(item[12]).rjust(5))

main()

                                                                                                                                                                                                                                                                                                        
