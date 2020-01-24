import os
import sys
import optparse

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary
import traci


def run():
    """ Method containing TraCI functionality and simulator loop """

    traci.person.add('person1', 'e16', 50.0)
    traci.person.appendWalkingStage('person1', ['e16', '-e20', '-e19', 'e1'], 50.0)

    step = 0
    while traci.simulation.getMinExpectedNumber() > 0:

        print(traci.person.getPosition3D('person1'))

        traci.simulationStep()

        pass

        step += 1

    traci.close()
    sys.stdout.flush()


def get_options():
    """ Use to parse commandline input when running this python script """

    opt_parser = optparse.OptionParser()
    opt_parser.add_option('--nogui', action='store_true', default=False,
                          help="Run the commandline version of SUMO")
    options, args = opt_parser.parse_args()
    return options


if __name__ == '__main__':

    options = get_options()
    if options.nogui:
        sumo_binary = checkBinary('sumo')
    else:
        sumo_binary = checkBinary('sumo-gui')

    traci.start([sumo_binary, '-c', '3x3.sumocfg', '--tripinfo-output',
                 'tripinfo.xml'])
    run()
