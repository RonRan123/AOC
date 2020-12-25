#!/usr/bin/python3

import argparse
import subprocess

SESSION = "53616c7465645f5fd136cc37220cd6e40990af36fb50b55c9a1eae66fad321a419ac3333324e0ea839092b9732e5e518"
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day', type=int)
parser.add_argument('--year', type=int, default=2020)
args = parser.parse_args()
cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(args.year, args.day, SESSION)

output = subprocess.check_output(cmd, shell=True)

print(output.decode('utf-8'), end='')