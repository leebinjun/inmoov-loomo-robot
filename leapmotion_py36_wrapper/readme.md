## Generating a Python 3.6 Wrapper with SWIG 4.0

* Generating a Python 3.3.0 Wrapper with SWIG 2.0.9 – Leap Motion Support  
https://support.leapmotion.com/hc/en-us/articles/223784048


On Windows:   
Building LeapPython.pyd on Windows (64-bit Python 3.6 for this example) :

> Install Visual Studio, Python 3.6 for Windows x64, and swig-4.0.

> Create an empty C++ project. Copy Leap.h, LeapMath.h, Leap.i, and Leap.lib (x64) into this project folder.

> From that folder, run SWIG to generate LeapPython.cpp. For example: c:\leap_project>"C:\Program Files (x86)\swigwin-4.0.1\swig.exe" -c++ -python -o LeapPython.cpp -interface LeapPython Leap.i

> Open up the project properties, select the Release configuration, and go to the Configuration Properties -> General page. From there, set the 'Target Name' to LeapPython and set the 'Configuration Type' to 'Dynamic Library (.dll)'.

> Go to to the C/C++ -> General property page. Add the path containing Python.h, typically C:\Python36\include.

> Go to the Linker -> Input property page. Add Leap.lib and the full path to python36.lib, typically C:\Python36\libs\python36.lib. 

> Press F7 to build. (If you hit errors such as missing symbols, this tends to come from accidentally omitting one library or mixing x86 with x64. Double-check that you have the correct Leap.lib and python36.lib (from 64-bit Python) and are building a Win32 configuration.)

> Rename the output LeapPython.dll to LeapPython.pyd


