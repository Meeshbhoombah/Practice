# -*- encoding: utf-8 -*-
"""
simulation.py

"""

import sys
from random import randrange
from random import uniform
from random import seed
from logger import Logger

class Simulation:

    def __init__(self, user_args):
        """ Initalizes the Simulation class

        Args:
            population_number (int): the total population of the herd
            vaccinated_percentage (float): the percentage of the total population that 
                is immune to the virus
            virus_name (string): the name of the virus of which the simulation is being 
                ran
            mortality_rate (float): the mortality rate of the virus, decides if a 
                person dies at the end of a step
            basic_repro_rate (float): the basic reproduction rate of the virus, decides 
                the likelihood of a virus spreading from an infected person to 
                another healthy, un-vaccinated person
            infected (int, optional): the number of the total population that has been 
                infected at the start of the simulation, default value is 1

        Raises:
            ValueError: if the required command line arguments are not met            
        """
        seed(42)

        if len(user_args) < 6:
            print('Include: [population] [persons vaccinated] [name of virus] '
                  '[mortality rate] [basic reproduction rate] '
                  '[persons infected (optional)]')

            sys.exit(1)

        # TODO - Handle incorrect values
        self.population          = int(user_args[0])
        self.vaccinated          = int(float(user_args[1]) * self.population)
        self.dead                = 0
        self.population_li       = []        

        self.virus_name          = str(user_args[2])
        self.mortality_rate      = float(user_args[3])
        self.basic_repro_rate    = float(user_args[4])
        
        if user_args[5] is None:
            self.infected = 1        
        else:
            self.infected = int(user_args[5])

        self.logger = Logger(self.virus_name, self.population, self.vaccinated,
                             self.mortality_rate, self.basic_repro_rate)
   
        healthy = self.population - (self.infected + self.dead)
        self.logger.log(healthy, self.infected, self.dead)

        self.current = 0
    
    def __iter__(self):
        """ Creates population based on intalized values of self.population,
                self.vaccinated 
    
        Returns:
            self.population_li (list): populated with an index equivelent to that of the 
                population decided by the user with values for the following:
                    - 0 = health
                    - 1 = vaccinated
                    - 2 = sick
                    - 3 = dead
        """
        # create the general population
        for i in range(self.population):
            self.population_li.append(0)
        
        # set vaccinated
        for i in range(self.vaccinated):
            vaccinated_index = randrange(0, len(self.population_li))
            self.population_li[vaccinated_index] = 1
        
        # set infected
        for i in range(self.infected):
            person_index = randrange(0, len(self.population_li))
            person_value = self.population_li[person_index]        

            if person_value != 0: 
                self.population_li[person_index] = 2
            else:
                i -= 1
                pass

        return self


    def __next__(self):
        """ for each iteration of the simulation set the amount of sick, dead, and 
                 vaccinated based on the mortality and basic reproduction rate 
                 and previous # of dead, sick, and vaccinated

        Returns:
            self.population_li (list): populated with the following values corresponding
                to the following states:
                    - 0 = health
                    - 1 = vaccinated
                    - 2 = sick
                    - 3 = dead
        """
        for i in range(self.infected):
        # for the amount of sick people choose 100 non-sick persons at random and infect
        # them based on the basic reproduction rate
            
            for interaction in range(100):
            # each sick person should interact with 100 persons from the population

                person_index = randrange(0, len(self.population_li))
                person_value = self.population_li[person_index]           
                
                if person_value == 0:
                # if the person is healthy and unvaccinated
                    roll = uniform(0.0, 1.0)                
    
                    if roll < self.basic_repro_rate:
                        self.population_li[person_index] = 2
                        self.infected += 1
                    else:
                        pass

        for i in [i for i, x in enumerate(self.population_li) if x == 2]:
        # kill a sick person based on the mortality rate
            roll = uniform(0.0, 1.0)
           
            if roll < self.mortality_rate:
                del self.population_li[i]
                self.dead += 1

        self.logger.log(len(self.population_li), self.infected, self.dead)

        self.current += 1
    
        return self


if __name__ == '__main__':
    # assign the user's input to a list called user_args        
    user_args = sys.argv[1:]
    
    for i in Simulation(user_args):
         print("Round ended")
    

