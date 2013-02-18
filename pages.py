pageno=0

def header(sec):
    global fil, pageno
    pageno += 1
    fname = 'page'+str(pageno)+'.html'
    if pageno == 1:
            fname = 'index.html'
    fil = open(fname,'w')
    fil.write('<!DOCTYPE html>\n')
    fil.write('<html>\n')
    fil.write('<head>\n')
    fil.write('<link rel="stylesheet" href="base.css" type="text/css"/>\n')
    fil.write('</head>\n')
    fil.write('<body>\n')
    fil.write('<center>\n')
    fil.write('<h1>'+sec+'</h1>\n')


def footer(ext=None):
    global fil, pageno
    prev = 'page'+str(pageno-1)+'.html'
    next = 'page'+str(pageno+1)+'.html'
    if pageno == 2:
        prev = 'index.html'
    fil.write('<br/>\n')
    fil.write('</center>')
    if pageno > 1:
        fil.write('<a href="'+prev+'">prev</a> ')
    fil.write('&nbsp; &nbsp; ')
    if not ext:
        fil.write('<a href="'+next+'">next</a> ')
    fil.write('</body>')
    fil.write('</html>')
    fil.close()

def image(iname,px):
    global fil
    fil.write('<img height="'+str(px)+'", src="images/'+iname+'.png">\n')

def video(vname,px):
    global fil
    fil.write('<video height="'+str(px)+'" controls>\n')
    fil.write('<source src="videos/'+vname+'.mp4" type="video/mp4">\n')
    fil.write('</video>')

def caption(txt):
    fil.write('<h2>'+txt+'</h2>')


header(' ')
fil.write('<br/>')
image('strauss',420)
footer()

header('Light Deflection')
image('query1',150)
caption('Newton (1704)')
footer()

header('Light Deflection')
image('dyson-etal',420)
footer()

header('Light Deflection')
image('lens0957',300)
image('lens1115',300)
caption('Double and Quadruple Quasars (discovered 1979/80)')
footer()

header('Geodesics')
image('flight1',320)
footer()

header('Geodesics')
image('flight2',320)
footer()

header('Geodesics')
image('darwin',450)
footer()

header('Geodesics')
video('gc',320)
caption('Raymond Ang&egrave;lil (2011)')
footer()

header('Geodesics')
video('wavefront1',320)
footer()

header('Geodesics')
video('wavefront2',320)
footer()

header('Geodesics')
video('wavefront3',320)
footer()

header("Fermat's Principle")
image('lens0957',300)
image('lens1115',300)
footer()

header("Fermat's Principle")
video('wavefront4',320)
footer()

header("Fermat's Principle")
image('irchel0',320)
footer()

header("Fermat's Principle")
image('irchel1',320)
footer()

header("Fermat's Principle")
image('irchel2',320)
footer()

header("Fermat's Principle")
image('lens0957',220)
image('arriv0957',220)
image('irchel1',220)
footer()

header("Fermat's Principle")
image('lens1115',220)
image('arriv1115',220)
image('irchel2',220)
footer()

header('Dark Matter')
image('sombrero',300)
image('malin',300)
caption('Sombrero galaxy (Messier 104)')
footer()

header('Dark Matter')
video('bfilg',320)
caption('Dominik Leier, Ignacio Ferreras (2011)')
footer()


header('The Expanding Universe')
image('nb',360)
footer()

header('The Expanding Universe')
video('pinot1',300)
footer()

header('The Expanding Universe')
video('pinot2',300)
footer()

header('The Expanding Universe')
fil.write('<table>')
fil.write('<tr><td>')
image('coles',220)
fil.write('</td> <td> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </td> <td>')
image('paraficz',220)
fil.write('</td></tr>\n')
fil.write('<tr><td><br/></td></tr>\n')
fil.write('<tr><td>')
fil.write('&nbsp;&nbsp;&nbsp;&nbsp; Jonathan Coles (2008)')
fil.write('</td> <td></td> <td>')
fil.write('&nbsp;&nbsp;&nbsp;&nbsp; Paraficz and Hjorth (2010)')
fil.write('</td></tr>\n')
fil.write('<tr><td>')
fil.write('&nbsp;&nbsp;&nbsp;&nbsp; using 11 lenses')
fil.write('</td> <td></td> <td>')
fil.write('&nbsp;&nbsp;&nbsp;&nbsp; using 18 lenses')
fil.write('</td></tr>\n')
fil.write('</table>')
footer()


header('A Lens Zoo?')
image('masterlens',400)
footer()

header('A Lens Zoo?')
image('aitoff',320)
footer()

header('A Lens Zoo?')
image('masterlens',400)
footer()

header('A Lens Zoo?')
image('zooniverse',420)
footer()

header('A Lens Zoo?')
video('lmt',320)
caption('Rafael K&uuml;ng and Jonathan Coles')
fil.write('<h4>Prototype: Dorde Masovic, Rafael K&uuml;ng, Marion Baumgartner</h4>\n')
fil.write('<code><a href="http://www.physik.uzh.ch/~rafik">')
fil.write('www.physik.uzh.ch/~rafik</a></code>\n')
footer(' ')

