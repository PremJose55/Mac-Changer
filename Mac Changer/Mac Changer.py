import subprocess
import optparse
import re


parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help= "Enter the Interface.")
parser.add_option("-m","--mac",dest="mac",help= "Enter the Mac Address.")
(values, argument) = parser.parse_args()

interface = values.interface
mac = values.mac

if not interface:
    parser.error("Enter the Interface. Press -h for help.")
elif not mac:
    parser.error("Enter the Mac Address. Press -h for help")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])

output = subprocess.check_output(["ifconfig",interface])


final_output = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))


if final_output:
    print("")

    if final_output.group(0) == mac :

        print("(+) Mac Address changed to", final_output.group(0))

    else:
        print("Mac Address is not changed.")

else:
    print("Could not find Mac Address.")





