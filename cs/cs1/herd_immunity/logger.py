# -*- encoding: utf-8 -*-
"""

"""

import sys

class Logger:

    def __init__(self, virus_name, population, vaccinated,
                 m_r, b_r_r):
        """
        
        """
        self.f = open('logs.txt', 'w')
        self.f.write(virus_name + '\n')
        self.f.write('Population: ' + str(population) + '\n')
        self.f.write('Persons vaccinated: ' + str(vaccinated) + '\n')
        self.f.write('Mortality Rate: ' + str(m_r) + '\n')
        self.f.write('Basic Reproduction Rate: ' + str(b_r_r) + '\n\n')

    
    def log(self, healthy, infected, dead):
        healthy = "Healthy: " + str(healthy)
        infected = "Infected: " + str(infected)
        dead = "Dead: " + str(dead)

        self.f.write('%-20s %20s %20s\n' % (healthy, infected, dead))

