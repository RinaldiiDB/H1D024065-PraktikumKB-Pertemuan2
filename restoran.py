import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

makanan = ctrl.Antecedent(np.arange(0,11), 'makanan')
pelayanan = ctrl.Antecedent(np.arange(0,11), 'pelayanan')
nilai = ctrl.Consequent(np.arange(0,11), 'nilai')

makanan['TidakEnak'] = fuzz.trimf(makanan.universe, [0, 2, 4])
makanan['Sedang'] = fuzz.trimf(makanan.universe, [3, 5, 7])
makanan['Enak'] = fuzz.trimf(makanan.universe, [6, 8, 10])

pelayanan['Ketus'] = fuzz.trimf(pelayanan.universe, [0, 2, 4])
pelayanan['Biasa'] = fuzz.trimf(pelayanan.universe, [3, 5, 7])
pelayanan['Ramah'] = fuzz.trimf(pelayanan.universe, [6, 8, 10])

nilai['Buruk'] = fuzz.trimf(nilai.universe, [0, 2, 4])
nilai['Cukup'] = fuzz.trimf(nilai.universe, [3, 5, 7])
nilai['Baik'] = fuzz.trimf(nilai.universe, [6, 8, 10])

aturan1 = ctrl.Rule(makanan['TidakEnak'] & pelayanan['Ketus'],
nilai['Buruk'])
aturan2 = ctrl.Rule(makanan['Sedang'] | pelayanan['Biasa'],
nilai['Cukup'])
aturan3 = ctrl.Rule(makanan['Enak'] | pelayanan['Ramah'], nilai['Baik'])
engine = ctrl.ControlSystem([aturan1, aturan2, aturan3])
system = ctrl.ControlSystemSimulation(engine)
system.input['makanan'] = 5.5
system.input['pelayanan'] = 7
system.compute()

print(system.output['nilai'])
