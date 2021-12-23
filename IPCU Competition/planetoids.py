#!/usr/bin/env python3
# ^^^ Important - tells kattis this is python3 vs python2
  
import sys
import json
import math


def act_to_binary(a):
	value = ''
	for action in a:
		if a[action]:
			value += '1'
		else:
			value += '0'
	return value

def direction(cord1, cord2):
	x1, y1 = cord1
	x2, y2 = cord2
	return [abs(float(x1) - float(x2)), abs(float(y1) - float(y2))]

#file = open('data.txt', 'w')

actions = {
	"thrust" : False,
	"clockwise" : False,
	"counter_clockwise" : True,
	"shoot" : True,
	"hyperspace" : False,
	"change" : True
	}

while True:
	raw_data = sys.stdin.readline()
	# Exit if stdin is closed.
	if not raw_data:
		break

	data = json.loads(raw_data)
	# Exit if we hit Game Over.
	if "gameOver" in data and data["gameOver"]:
		break

	#file.write('Distance to Artifac: ' + str(dist))
	# @TODO: Process input frame
	# Emit command.
	shipR = float(data["shipR"])
	direct = direction(data["shipPos"], data["artfPos"])
	angle_to_goal = math.degrees(math.atan2(direct[0], direct[1])) + 90

	#if data["artfPos"][0] < 0: # artifact is in left zone

	# if ship is pointed towards goal
	if shipR <= angle_to_goal + 3 and shipR >= angle_to_goal -3:
		actions["thrust"] = True
	else:
		actions["thrust"] = False

	# ship needs to turn counter clockwise to point towards  goal	
	if shipR < angle_to_goal:
		actions["clockwise"] = False
		actions["counter_clockwise"] = True
	# ship needs to turn clockwise to points towards goal
	elif shipR > angle_to_goal:
		actions["clockwise"] = True
		actions["counter_clockwise"] = False
	

	#file.write("Score: " + str(data["currentScore"]) + '\n')
	#file.write("artifact cord: " + str(data["artfPos"]) + '\n')
	#file.write("angle to goal: " +str(angle_to_goal) + '\n')
	#file.write("ShipR: " +str(data["shipR"])+ '\n')
	#file.write("Clockwise: " + str(actions["clockwise"]) + '\n')
	#file.write("Counter: " + str(actions["counter_clockwise"]) + '\n')
	
	
	# 1 thrust
	# 1 clockwise
	# 1 counterclockwise
	# 1 shoot
	# 1 hyperspace
	# 1 change state
	binary_moves = act_to_binary(actions)
	sys.stdout.write(binary_moves + "\n")
	sys.stdout.flush()
#file.close()
