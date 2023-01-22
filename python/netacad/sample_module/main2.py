from sys import path

path.append('../sample_package/extra_pack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import funI
from extra.good.beta import funB as bet

print(sig.funS())
print(alp.funA())
print(funI())
print(bet())

