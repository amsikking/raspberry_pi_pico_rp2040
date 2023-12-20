import machine
import time

adc4 = machine.ADC(4)

t0_ns = []
t1_ns = []
n = 1000 # <= ~1000 before max memory
for i in range(n):
    t0_ns.append(time.time_ns())
    reading = adc4.read_u16()
    t1_ns.append(time.time_ns())

time_us = [1e-3 * (t1_i - t0_i) for t1_i, t0_i in zip(t1_ns, t0_ns)]

if n <= 10:
    print('time_us', time_us)
print('t_max_us', max(time_us))
t_ave_us = sum(time_us) / n
print('t_ave_us', t_ave_us)
print('rate_Ksps', 1 / (1e-3 * t_ave_us))
