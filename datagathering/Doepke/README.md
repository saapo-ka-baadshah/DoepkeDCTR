# The reader module for the components developed by **Doepke** #
---
## DCTR ##
This is a **Differential Current Transformer** and uses **Modbus/TCP** protocol.
In this module the package used is **FakeModbus** which simulates the data response from the actual device.
For Production, please change the following line from `Doepke/DCTR/DCTR.py` 
```python
from FakeModbus.client.sync import ModbusTcpClient as MTC
```
to (`FakeModbus` to `pymodbus`)
```python
from pymodbus.client.sync import ModbusTcpClient as MTC
```

- ### Class `DCTR` ###
  ```python
  from Doepke.DCTR.DCTR import DCTR

  device = DCTR(uri = "address_to_ur_device", 
                _reg_count = 11,
                _callback_alarm1 = pointYourCallbackForAlarm1,
                _callback_alarm1_args = Alarm1CallbackArgs,
                _callback_alarm2 = pointYourCallbackForAlarm2,
                _callback_alarm2_args = Alarm2CallbackArgs)
  ```

  Use **`DCTR.read_registers(base_register)`** to read the data from all the registers as mentioned on the count.
  *base_register : bytes &nbsp;&nbsp;&nbsp; specify base register. (default = 0x00)*
  ```python3
  data = device.read_registers(0x00)
  ```



