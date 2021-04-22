from Doepke.DCTR.DCTR import DCTR

device = DCTR('192.168.0.12', _reg_count=10)

for i in range(50):
    print(device.read_registers())