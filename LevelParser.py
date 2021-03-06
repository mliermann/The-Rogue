import AppEngine
from AppEngine import *

import ObjectClasses.StationaryObject as so
import ObjectClasses.MovableObject as mo

import random


class Parser():
    def __init__(self, level):
        self.level = level
        self.lines = []

        self.obstDict = {
            "#" : "Sprites/Ground/rocks.png",
            "@" : "Sprites/Ground/dead_vines.png",
            " " : ["Sprites/Ground/ground.png", "Sprites/Ground/ground2.png", "Sprites/Ground/ground3.png"],
            "$" : "Sprites/Ground/tree.png",
            "&" : "Sprites/Ground/treeGrove.png",
            "*" : "Sprites/Objects/sign.png"
        }

        self.hasParsed = False

    def parse(self):
        with open("GameConfig/levels.txt", "r") as f:
            self.lines = f.read().splitlines()

        self.lines = self.lines[self.lines.index("// %s" % self.level):]
        self.lines.pop(0)

        done = False
        for line in self.lines:
            if line == '':
                if done == False:
                    self.lines = self.lines[:self.lines.index(line)]
                    done = True


        self.hasParsed = True

    def checkForParse(self):
        if self.hasParsed == False:
            print("Warning: levels.txt has not been loaded. Call parser.parse() first before calling this one.")
            raise FileNotFoundError("levels.txt file not loaded.")

    def generate_ground(self, grndTileList):
        self.checkForParse()         
        for y in range(14):
            for x in range(15):
                random_grnd = random.randint(0, 2)
                grndTileList.append(sprite(self.obstDict[" "][random_grnd], x * 64, y * 64, "grnd x=%s, y=%s" % (x, y)))

    def generate_obstacles(self, obstTileList):
        self.checkForParse()
        for y in range(len(self.lines)):
            temp = list(self.lines[y])
            for x in range(len(temp)):
                if temp[x] != " ":
                    if temp[x] == "*":
                        obstTileList.append(so.StationaryObstacle(sprite(self.obstDict[temp[x]], x * 64 + 16, y * 64 + 16, "sign %s %s" % (x, y))))
                        print(x)
                        print(y)
                    else:
                        obstTileList.append(so.StationaryObstacle(sprite(self.obstDict[temp[x]], x * 64, y * 64, "obst x=%s, y=%s" % (x, y))))
    
    def generate_hazards(self, hazrdList):
        pass # of type DamagingObject

    def generate_levelComplete(self):
        self.checkForParse()


    
