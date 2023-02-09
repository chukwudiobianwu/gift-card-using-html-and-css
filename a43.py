#!/usr/bin/env python3
'''Assignment 4 Part 1 template'''
print(__doc__)
from typing import IO
import random as rand

class PyArt:
    '''Class PyArt'''
    def __init__(self,cx: str, xv: str, cir: int, col: tuple, ciro: tuple, om: tuple, ro: tuple, sp: tuple):
        self.fnm: str = cx
        self.wbnn: str = xv
        self.snm: str =cir
        self.x:str =col[0]
        self.swidth: str =col[1]
        self.y: str =col[2]
        self.sheight: str =col[3]
        self.ss: str =ciro[0]
        self.es: str =ciro[1]
        self.sr: str =om[0]
        self.er: str =om[1]
        self.bh: str =ro[0]
        self.eh: str =ro[1]
        self.bw: str =ro[2]
        self.ew: str =ro[3]
        self.fr: str = sp[0]
        self.cr: str = sp[1]
        self.fg: str = sp[2]
        self.cg: str = sp[3]
        self.fb: str = sp[4]
        self.cb: str = sp[5]
        self.fo: str = sp[6]
        self.co: str = sp[7]

class GenRandom:
    '''Class GenRandom'''
    def Setting(self,s: int,e: int) -> int:
        if(s==e):
            b=s
            return b
        else:
            b = rand.randrange(s,e,1)
            return b

    def fl(self,v,c) -> int:
        h= round(rand.uniform(v,c),1)
        return h

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

class Ellipse:
    '''Ellipse class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rx: int = cir[2]
        self.ry: int = cir[3]
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
    
    def drawEllipseLine(self,f: IO[str], t: int, d: Ellipse):
        '''drawCircle method'''
        ts: str = "   " * t
        line: str = f'<ellipse cx="{d.cx}" cy="{d.cy}" rx="{d.rx}" ry="{d.ry}" fill="rgb({d.red}, {d.green}, {d.blue})" fill-opacity="{d.op}"></ellipse>'
        f.write(f"{ts}{line}\n")

    def writeHTMLline(self,f: IO[str], t: int, line: str):
        '''writeLineHTML method'''
        ts = "   " * t
        f.write(f"{ts}{line}\n")

    def genArtCircle(self,f: IO[str], t: int ,bh: int,bk: int,bl: int,r: int,g: int,b: int,o: int):
        '''genART method'''
        self.drawCircleLine(f, t, Circle((bh,bk,bl), (r,g,b,o)))

    def genArtRectangle(self,f: IO[str], t: int,q: int,w: int,e: int,r: int,b: int,y: int,u: int,i: int):
        '''genART method'''
        self.drawRectangleLine(f, t, Rectangle((q,w,e,r), (b,y,u,i)))
    
    def genArtEllipse(self,f: IO[str], t: int,q: int,w: int,e: int,m: int,b: int,y: int,u: int,i: int):
        '''genART method'''
        self.drawEllipseLine(f, t, Ellipse((q,w,e,m), (b,y,u,i)))

class GenRandomShape:
    '''GenRandomShape'''
    def but(self,br: int,sf: int,cx:PyArt) -> object: 
        k:GenRandom =GenRandom()
        b=rand.randrange(br,sf+1)
        v=ProEpilogue()
        fnam: str = cx.fnm
        f: IO[str] = open(fnam, "a")
        if(b==0): 
           return v.genArtCircle(f, 2 ,k.Setting(cx.x,cx.y), k.Setting(cx.x,cx.y), k.Setting(cx.sr,cx.er),k.Setting(cx.fr,cx.cr),k.Setting(cx.fg,cx.cg),
            k.Setting(cx.fb,cx.cb),k.fl(cx.fo,cx.co))
        if(b==1):
           return v.genArtRectangle(f, 2 ,k.Setting(cx.x,cx.y), k.Setting(cx.x,cx.y), k.Setting(cx.bh,cx.eh),k.Setting(cx.bw,cx.ew),k.Setting(cx.fr,cx.cr),k.Setting(cx.fg,cx.cg),
            k.Setting(cx.fb,cx.cb),k.fl(cx.fo,cx.co))
        if(b==2):
           return v.genArtEllipse(f, 2 ,k.Setting(cx.x,cx.y), k.Setting(cx.x,cx.y), k.Setting(cx.sr,cx.er),k.Setting(cx.sr,cx.er),k.Setting(cx.fr,cx.cr),k.Setting(cx.fg,cx.cg),
            k.Setting(cx.fb,cx.cb),k.fl(cx.fo,cx.co))

class ArtConfig:
    '''Class ArtConfig'''
    def space(self,cx: PyArt):
        b:ProEpilogue =ProEpilogue()
        h:GenRandomShape =GenRandomShape()
        '''writeHTMLfile method'''
        fnam: str = cx.fnm
        winTitle = cx.wbnn
        f: IO[str] = open(fnam, "w")
        z: IO[str] = open(fnam, "a")
        b.writeHTMLHeader(f, winTitle)
        b.openSVGcanvas(f, 1, (cx.swidth,cx.sheight))
        for i in range(cx.snm):
            h.but(cx.ss,cx.es,cx)
        b.closeSVGcanvas(z, 1)
        f.close()
        
def main() -> None:
    '''main method'''
    v:PyArt =PyArt("SVGART1.html","Python SVG Art1", 500 , (0,500,500,200) , (0,2), (25,50), (0,150,0,150), (0,120,0,120,0,105,0.8,1.0))
    be:ArtConfig = ArtConfig()
    be.space(v)

main()

                                                                                                                                                                                                                                                                                                        
