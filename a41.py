#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)
import logging
from typing import IO

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class Rectangle:
    '''Rectangle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.x: int = cir[0]
        self.y: int = cir[1]
        self.width: int = cir[2]
        self.height: int = cir[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

class ProEpilogue:
    '''ProEpilogue class'''
    def writeHTMLcomment(self,f: IO[str], t: int, com: str):
        '''writeHTMLcomment method'''
        ts: str = "   " * t
        f.write(f'{ts}<!--{com}-->\n')
    
    def closeSVGcanvas(self,f: IO[str], t: int):
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        f.write(f'{ts}</svg>\n')
        f.write(f'</body>\n')
        f.write(f'</html>\n')
    
    def writeHTMLHeader(self,f: IO[str], winTitle: str):
        '''writeHeadHTML method'''
        self.writeHTMLline(f, 0, "<html>")
        self.writeHTMLline(f, 0, "<head>")
        self.writeHTMLline(f, 1, "<title>" + winTitle + "</title>")
        self.writeHTMLline(f, 0, "</head>")
        self.writeHTMLline(f, 0, "<body>")

    def openSVGcanvas(self,f: IO[str], t: int, canvas: tuple):
        '''openSVGcanvas method'''
        ts: str = "   " * t
        self.writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')

    def drawCircleLine(self,f: IO[str], t: int, c: Circle):
            '''drawCircle method'''
            ts: str = "   " * t
            line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
            f.write(f"{ts}{line}\n")

    def drawRectangleLine(self,f: IO[str], t: int, d: Rectangle):
            '''drawCircle method'''
            ts: str = "   " * t
            line: str = f'<rect x="{d.x}" y="{d.y}" width="{d.width}" height="{d.height}" fill="rgb({d.red}, {d.green}, {d.blue})" fill-opacity="{d.op}"></rect>'
            f.write(f"{ts}{line}\n")

    def writeHTMLline(self,f: IO[str], t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")

    def genArtCircle(self,f: IO[str], t: int):
        '''genART method'''
        self.drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
        self.drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
        self.drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
        self.drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
        self.drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
        self.drawCircleLine(f, t, Circle((50,250,50), (0,0,255,1.0)))
        self.drawCircleLine(f, t, Circle((150,250,50), (0,0,255,1.0)))
        self.drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
        self.drawCircleLine(f, t, Circle((350,250,50), (0,0,255,1.0)))
        self.drawCircleLine(f, t, Circle((450,250,50), (0,0,255,1.0)))

    def genArtRectangle(self,f: IO[str], t: int):
        s=ProEpilogue()
        '''genART method'''
        self.drawRectangleLine(f, t, Rectangle((50,50,50,50), (255,0,0,1.0)))
        self.drawRectangleLine(f, t, Rectangle((150,50,50,50), (255,0,0,1.0)))
        self.drawRectangleLine(f, t, Rectangle((250,50,50,50), (255,0,0,1.0)))
        self.drawRectangleLine(f, t, Rectangle((350,50,50,50), (255,0,0,1.0)))
        self.drawRectangleLine(f, t, Rectangle((450,50,50,50), (255,0,0,1.0)))
        self.drawRectangleLine(f, t, Rectangle((50,250,50,50), (0,0,225,1.0)))
        self.drawRectangleLine(f, t, Rectangle((150,250,50,50), (0,0,255,1.0)))
        self.drawRectangleLine(f, t, Rectangle((250,250,50,50), (0,0,255,1.0)))
        self.drawRectangleLine(f, t, Rectangle((350,250,50,50), (0,0,255,1.0)))
        self.drawRectangleLine(f, t, Rectangle((450,250,50,50), (0,0,255,1.0)))

    def writeHTMLfilecC(self):
        b=ProEpilogue()
        '''writeHTMLfile method'''
        fnam: str = "myPart1Art.html"
        winTitle = "My Art"
        f: IO[str] = open(fnam, "w")
        self.writeHTMLHeader(f, winTitle)
        self.openSVGcanvas(f, 1, (500,300))
        self.genArtCircle(f, 2)
        self.closeSVGcanvas(f, 1)
        f.close()

    def writeHTMLfilecR(self):
        b=ProEpilogue()
        '''writeHTMLfile method'''
        fnam: str = "a41.html"
        winTitle = "My Art"
        f: IO[str] = open(fnam, "a")
        self.writeHTMLHeader(f,winTitle)
        self.openSVGcanvas(f, 1, (500,300))
        self.genArtRectangle(f, 2)
        self.closeSVGcanvas(f, 1)
        f.close()

def main():
    '''main method'''
    v=ProEpilogue()
    v.writeHTMLfilecC()
    v.writeHTMLfilecR()
    
main()

                                                                                                                                                                                                                                                                                                        
