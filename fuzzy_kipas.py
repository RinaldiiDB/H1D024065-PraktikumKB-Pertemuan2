import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

suhu = ctrl.Antecedent(np.arange(0, 41, 1), 'suhu')
kelembapan = ctrl.Antecedent(np.arange(0, 101, 1), 'kelembapan')
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kipas')

suhu['dingin'] = fuzz.trimf(suhu.universe, [0, 0, 20])
suhu['normal'] = fuzz.trimf(suhu.universe, [15, 25, 35])
suhu['panas'] = fuzz.trimf(suhu.universe, [30, 40, 40])

kelembapan['kering'] = fuzz.trimf(kelembapan.universe, [0, 0, 50])
kelembapan['sedang'] = fuzz.trimf(kelembapan.universe, [30, 50, 70])
kelembapan['lembap'] = fuzz.trimf(kelembapan.universe, [60, 100, 100])

kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 0, 50])
kipas['sedang'] = fuzz.trimf(kipas.universe, [30, 50, 70])
kipas['cepat'] = fuzz.trimf(kipas.universe, [60, 100, 100])

rule1 = ctrl.Rule(suhu['dingin'] & kelembapan['kering'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['normal'] & kelembapan['sedang'], kipas['sedang'])
rule3 = ctrl.Rule(suhu['panas'] & kelembapan['lembap'], kipas['cepat'])
rule4 = ctrl.Rule(suhu['panas'], kipas['cepat'])
rule5 = ctrl.Rule(kelembapan['lembap'], kipas['cepat'])

kipas_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5])
kipas_simulasi = ctrl.ControlSystemSimulation(kipas_ctrl)

while True:
    try:
        suhu_input = float(input("Masukkan suhu (0-40 °C): "))
        if 0 <= suhu_input <= 40:
            break
        else:
            print("Suhu harus antara 0 - 40!")
    except:
        print("Input tidak valid!")

while True:
    try:
        kelembapan_input = float(input("Masukkan kelembapan (0-100 %): "))
        if 0 <= kelembapan_input <= 100:
            break
        else:
            print("Kelembapan harus antara 0 - 100!")
    except:
        print("Input tidak valid!")

kipas_simulasi.input['suhu'] = suhu_input
kipas_simulasi.input['kelembapan'] = kelembapan_input

kipas_simulasi.compute()

print("\n=== HASIL ===")
print("Suhu:", suhu_input)
print("Kelembapan:", kelembapan_input)
print("Kecepatan kipas:", kipas_simulasi.output['kipas'])

kipas.view(sim=kipas_simulasi)