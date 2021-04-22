"""
Module:             DataGathering
SubModule:          Doepke's DCTR Client
Author:             Amey Mahadik <amey.mahadik@ferdinand-steinbeis-institut.de>
"""

from .FakeModbus.client.sync import ModbusTcpClient as MTC

class DCTR:
    """
    Inputs: 
            uri :                   The ip address or local/remote domain on which the Doepke DCTR is running
            _reg_count:             Number of registers in the device
            _callback_alarm1:       The callback function to be triggered on triggering of alarm 1
            _callback_alarm1_args:  Arguments for alarm1 callback
            _callback_alarm2:       The callback function to be triggered on triggering of alarm 2
            _callback_alarm2_args:  Arguments for alarm2 callback  
    """

    def __init__(self, uri : str, _reg_count : int = 11 , unit : int =1,
     _callback_alarm1 = None, _callback_alarm1_args = (None,),
     _callback_alarm2 = None, _callback_alarm2_args = (None,)):
        self.client = MTC(uri= uri)
        self.reg_count = _reg_count
        self.unit = unit
        if(_callback_alarm1 == None):
            self._alarm1 = self.internal_alarm1
        else:
            self._alarm1 = _callback_alarm1
        self._alarm1_args = list(_callback_alarm1_args)

        if(_callback_alarm2 == None):
            self._alarm2 = self.internal_alarm2
        else:
            self._alarm2 = _callback_alarm2
        self._alarm2_args = list(_callback_alarm2_args)

    

    # Internal Alarm Notification
    def internal_alarm1(self, args):
        print('Alarm 1 Triggered')


    # Internal Alarm Notification
    def internal_alarm2(self, args):
        print('Alarm 2 Triggered')
        

    # Read all registers from the device
    def read_registers( self, base_register = 0x00 ):
        vals = self.client.read_holding_registers(base_register, self.reg_count, unit = self.unit)
        if(vals[-2] == 1):
            self._alarm1( *self._alarm1_args )
        
        if(vals[-1] == 1):
            self._alarm2( *self._alarm2_args )
        
        return(vals)


def externalAlarm1(name:str):
    print(name)


d = DCTR('avb', _callback_alarm1=externalAlarm1, _callback_alarm1_args=('Heisenberg',))

for i in range(50):
    print(d.read_registers())