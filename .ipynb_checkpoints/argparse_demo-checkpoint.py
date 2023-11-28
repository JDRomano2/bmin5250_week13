import argparse

# Create the argument parser object
parser = argparse.ArgumentParser(
    prog='argparse_demo.py',
    description='This script demonstrates basic features of Python\'s argparse library'
)

# Define the arguments the file can accept
parser.add_argument(
    '-f',
    '--filename',
    help="Name of the file that will be loaded [default: \"myfile1.txt\"].",
    default="myfile1.txt"
)
parser.add_argument('-v', '--verbose', action='store_true', help="Print the arguments to the screen for informational purposes")  # How did I know what to put in `action`? Read the documentation!!!

# Parse the arguments that the user entered at the command line
args = parser.parse_args()

if (args.verbose):
    print("INFO: User set the verbose flag")
    print(args)
    print()
    
if args.filename:
    with open(args.filename, 'r') as fp:
        file_contents = fp.readlines()
        print(file_contents)
        
else:
    print("No filename provided - please try again.")