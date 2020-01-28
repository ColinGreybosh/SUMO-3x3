# SUMO-3x3
Microscopic Traffic Simulation with Demand POIs using SUMO and TraCI

###### Running the simulator
```
usage: run_simulator.py [-h] [--nogui] config_file

Run a given .sumocfg file with TraCI intervention

positional arguments:
  config_file  provide the file path to the .sumocfg file

optional arguments:
  -h, --help   show this help message and exit
  --nogui      run the commandline version of SUMO

>>> python run_simulator.py cooperH.sumocfg
```