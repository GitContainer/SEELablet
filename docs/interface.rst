The Communications Library : interface
======================================

``interface`` is a class contained within the ``SEEL`` package, and contains the functions
used to access the instrument's various control and measurement tools.

During initialization, the class auto detects the USB ports on which a SEELablet device is 
connected, and connects to the first one. 

It also accepts keywords arguments if the user
wishes to connect to a specific port. e.g. ``I = interface.connect(port = '\dev\ttyUSB0')``


Main Communication Class : SEEL.interface
-----------------------------------------

.. automodule:: SEEL.interface
	:members:
	:exclude-members: write_flash,write_bulk_flash

