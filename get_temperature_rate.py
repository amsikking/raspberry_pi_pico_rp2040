import machine
import time

sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / (65535)

temp_degC = []
time_us = []
n = 1000 # <= ~1000 before max memory
for i in range(n):
    t0  = time.time_ns()
    reading = sensor_temp.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode,
    # connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    temp = 27 - (reading - 0.706) / 0.001721
    temp_degC.append(temp)
    time_us.append((1e-3 * (time.time_ns() - t0)))

if n <= 10:
    print('temp_degC', temp_degC)
    print('time_us', time_us)
print('t_max_us', max(time_us))
t_ave_us = sum(time_us) / n
print('t_ave_us', t_ave_us)
print('rate_Ksps', 1 / (1e-3 * t_ave_us))
