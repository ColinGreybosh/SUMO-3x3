import os
import sys
import argparse

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci


def run():
    """ Method containing TraCI functionality and simulator loop """

    # traci.person.add('person1', 'e16', 50.0)
    # traci.person.appendWalkingStage('person1', ['e16', '-e20', '-e19', 'e1'], 50.0)

    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:

        # print("p1 at:", traci.person.getPosition3D('person1'))

        traci.simulationStep()

        pass  # TraCI commands go here

        step += 1

    traci.close()
    sys.stdout.flush()


if __name__ == '__main__':

    # Receive commandline input for the config file and SUMO GUI/CLI
    parser = argparse.ArgumentParser(description='Run a given .sumocfg file with TraCI intervention')
    parser.add_argument('config_file', action='store', type=str, help='provide the file path to the .sumocfg file')
    parser.add_argument('--nogui', action='store_true', default=False, help="run the commandline version of SUMO")
    args = parser.parse_args()

    if args.nogui:
        sumo_binary = checkBinary('sumo')
    else:
        sumo_binary = checkBinary('sumo-gui')
    traci.start([sumo_binary, '-c', args.config_file,
                 '--tripinfo-output', 'tripinfo.xml'])
    run()
