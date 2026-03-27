import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

biaya = ctrl.Antecedent(np.arange(0,1001), 'biaya')
permintaan = ctrl.Antecedent(np.arange(0,60), 'permintaan')
produksi = ctrl.Consequent(np.arange(0,100), 'produksi')
# Biaya produksi
biaya['Rendah'] = fuzz.zmf(biaya.universe, 0, 500)
biaya['Standar'] = fuzz.pimf(biaya.universe, 0, 500, 500, 1000)
biaya['Tinggi'] = fuzz.smf(biaya.universe, 500, 1000)

permintaan['Turun'] = fuzz.trapmf(permintaan.universe, [0,0,10,30])
permintaan['Biasa'] = fuzz.trimf(permintaan.universe, [10,30,50])
permintaan['Naik'] = fuzz.trapmf(permintaan.universe, [30,50,60,60])

produksi['Berkurang'] = fuzz.trapmf(produksi.universe, [0,0,10,50])
produksi['Normal'] = fuzz.trimf(produksi.universe, [30,50,70])
produksi['Bertambah'] = fuzz.trapmf(produksi.universe, [50,90,100,100])

aturan1 = ctrl.Rule(biaya['Rendah'] & permintaan['Naik'],
produksi['Bertambah'])
aturan2 = ctrl.Rule(biaya['Standar'], produksi['Normal'])
aturan3 = ctrl.Rule(biaya['Tinggi'] & permintaan['Turun'],
produksi['Berkurang'])

engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)

system.input['biaya'] = 500
system.input['permintaan'] = 30
system.compute()
print(system.output['produksi'])
produksi.view(sim=system)
input()