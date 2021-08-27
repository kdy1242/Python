import my_module as mm

mm.지원이()
print(mm.date)

import travel.gangneung as ga
gp = ga.GangneungPackage()
print(gp)

from travel import gangneung
gp = gangneung.GangneungPackage()
print(gp)

from travel import ilsan
ilsan.이지()

from travel import *
ilsan.이지()
gp = gangneung.GangneungPackage()
print(gp)