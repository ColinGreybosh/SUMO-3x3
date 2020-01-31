# SUMO-3x3
Microscopic Traffic Simulation with Demand POIs using SUMO and TraCI

## Scenarios
* 3x3
* cooperH
* noCars

### 3x3
A 3 block by 3 block road network with manual routing and bus stop locations.

### cooperH
Similar to 3x3, but featuring ACTIVITYGEN demand routes.

### noCars
Similar to 3x3, but with multimodal transportation.
Pedestrians make use of the bus line circling the blocks.

## Running the simulator with TraCI intervention
```
usage: run_simulator.py [-h] [--nogui] config_file

Run a given .sumocfg file with TraCI intervention

positional arguments:
  config_file  provide the file path to the .sumocfg file

optional arguments:
  -h, --help   show this help message and exit
  --nogui      run the commandline version of SUMO
```
#### Example Usage (with GUI)
```shell script
> python run_simulator.py ./cooperH/cooperH.sumocfg
```
#### Example Usage (without GUI)
```shell script
> python run_simulator.py --nogui ./cooperH/cooperH.sumocfg
```