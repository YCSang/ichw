"""planets.py: Simulation of planets movement.

__author__ = 'Sang'
__pkuid__ = '1600017765'
__email__ = 'johnbirdsang@pku.edu.cn'
"""

import turtle
from math import cos, sin, sqrt


class Planet(turtle.Turtle):
    """a subclass of turtle.Turtle,
    to identify orbit and movement of a planet.
    """

    def __init__(self, a, e, phi, color):
        """parameters and initial options of an orbit.
        a, b, c stand for the parameter of the ellipse.
        phi stands for the rotation of the axis of the ellispse.
        xi, yi stand for position before rotation.
        x, y stand for position after rotation.
        """
        super().__init__()
        self.time = 0
        self.a = a
        self.b = a*sqrt(1 - e**2)
        self.c = a*e
        self.phi = phi
        self.xi = self.a + self.c
        self.yi = 0
        self.x = self.xi * cos(self.phi) - self.yi * sin(self.phi)
        self.y = self.xi * sin(self.phi) + self.yi * cos(self.phi)
        self.w = 1000 * a**-1.5
        self.color(color)
        self.shape('circle')
        self.up()
        self.setheading(90)
        self.goto(self.x, self.y)
        self.pd()

    def run(self):
        """planet moves with time going.
        """
        self.time += 0.1
        self.xi = self.a * cos(self.w * self.time) + self.c
        self.yi = self.b * sin(self.w * self.time)
        self.x = self.xi * cos(self.phi) - self.yi * sin(self.phi)
        self.y = self.xi * sin(self.phi) + self.yi * cos(self.phi)
        self.goto(self.x, self.y)


def main():
    """main loop
    """
    Sun = turtle.Turtle(shape='circle')
    Sun.color('yellow')
    PA = Planet(50, 0.2, 0, 'blue')
    PB = Planet(100, 0.17, 1, 'lime')
    PC = Planet(120, 0.1, 0.2, 'red')
    PD = Planet(160, 0.05, 2, 'black')
    PE = Planet(210, 0.13, 1.3, 'orange')
    PF = Planet(240, 0.08, 0.1, 'cyan')
    while True:
        PA.run()
        PB.run()
        PC.run()
        PD.run()
        PE.run()
        PF.run()


if __name__ == '__main__':
    main()
