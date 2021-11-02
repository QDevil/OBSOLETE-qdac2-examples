import pyvisa as visa
import os

qdac_device = os.environ.get('QDAC_DEVICE', '/dev/cu.usbserial-1420')

print(f'Using device {qdac_device}')

rm = visa.ResourceManager('@py')  # Use pyvisa-py
dac = rm.open_resource(f'ASRL{qdac_device}::INSTR')
dac.write_termination = '\n'
dac.read_termination = '\n'
dac.baud_rate = 921600
dac.timeout = 100  # ms

print(dac.query('syst:err:all?'))
print(dac.query('*idn?'))
