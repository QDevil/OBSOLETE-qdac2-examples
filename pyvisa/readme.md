# Using PyVISA with QDAC-II

Test serial connection:

    $ QDAC_DEVICE=/dev/cu.usbserial-1420
    $ python usb_device.py

Test Ethernet connection:

    $ QDAC_IP=192.168.8.15
    $ python ethernet.py

# One-time setup

Linux/Mac:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install --upgrade pip
    $ pip install -r requirements.txt

Windows:

    PS> python3 -m venv venv
    PS> venv\Scripts\activate
    (venv) PS> pip install --upgrade pip
    (venv) PS> pip install -r requirements.txt
