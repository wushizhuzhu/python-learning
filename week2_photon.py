#Excercise 1
# name = "hydrogen"
# n = 2
# energy = -3.4

# print(f"element = {name}")
# print(f"n = {n}, E = {energy} eV")
# print(f"2 * n = {2 * n}")
# print(f"E / n = {energy / n}")
# print(f"{name} level n={n}: {energy:.2f} eV")
def photon_energy_eV(wavelength_nm):
    '''用 E = hc/λ 计算光子能量，输入波长单位 nm，返回能量单位 eV。'''
    h = 6.62607015e-34
    c = 2.99792458e8
    energy = h * c / (wavelength_nm * 1e-9) / 1.602176634e-19
    return energy
message = " Please input the wavelength_nm you want (unit: nm)\n "
message += "And if you want to end, please input 'q'\n "
message += "Now please input: "
while True :
    wavelength = input(message)
    if wavelength == "q" :
        print("Calculation is over!")
        break
    else :
        wavelength_nm = float(wavelength)
        Energy = photon_energy_eV(wavelength_nm)
        print(f" The energy corresponding to wavelength is {Energy:.3f} eV ")
# 固定算三个波长（题目要求的版本）
print("\n=== 三个典型波长 ===")
for wl in (500, 121.6, 0.1):
    print(f"{wl:8.1f} nm → {photon_energy_eV(wl):10.3f} eV")

    


