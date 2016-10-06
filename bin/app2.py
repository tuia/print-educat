

import pyqrcode

for x in range(1, 64):
    print "We're on time %d" % (x)

    # gera qrcode para cada item #
    number = pyqrcode.create( "Item " + str(x) )
    number.svg( 'static/img/questions-codes/' + str(x) + '.svg', scale=8)