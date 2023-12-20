import machine
import time

# input:
adc1 = machine.ADC(26)
adc2 = machine.ADC(27)
# output:
led = machine.Pin("LED", machine.Pin.OUT)
# thresholds:
min_v1 = 1
min_v2 = 1.2
min_int_v1 = 3
min_int_v2 = 4
# local integration variables:
int_v1 = 0
int_v2 = 0
# timing and iterations:
time_us = []
n = 1000 # <= ~1000 before max memory
for i in range(n):
    t0  = time.time_ns()
    # read values:
    v1 = adc1.read_u16()
    v2 = adc2.read_u16()
    # check thresholds:
    if v1 < min_v1:
        int_v1 = 0
        ch1_event = False
    if v1 >= min_v1:
        int_v1 += v1
        if int_v1 > min_int_v1:
            ch1_event = True
            int_v1 = 0
    if v2 < min_v2:
        int_v2 = 0
        ch2_event = False
    if v2 >= min_v2:
        int_v2 += v2
        if int_v2 > min_int_v2:
            ch2_event = True
            int_v2 = 0
    # combined sort:
    if (ch1_event and ch2_event):
            led.toggle()
            ch1_event = False
            ch2_event = False
    time_us.append((1e-3 * (time.time_ns() - t0)))

if n <= 10:
    print('time_us', time_us)
print('t_max_us', max(time_us))
t_ave_us = sum(time_us) / n
print('t_ave_us', t_ave_us)
print('rate_Ksps', 1 / (1e-3 * t_ave_us))
