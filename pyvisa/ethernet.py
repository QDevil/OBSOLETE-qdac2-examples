import pyvisa as visa
import os

qdac_addr = os.environ.get('QDAC_IP', '192.168.8.15')

print(f'Using IP address {qdac_addr}')

rm = visa.ResourceManager('@py')  # Use pyvisa-py
dac = rm.open_resource(f'TCPIP::{qdac_addr}::5025::SOCKET')
dac.write_termination = '\n'
dac.read_termination = '\n'

print(dac.query('syst:err:all?'))
print(dac.query('*idn?'))
