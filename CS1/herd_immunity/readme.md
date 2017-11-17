# Herd Immunity Simulation
After reading the prompt for this project I decided to not create a person
class and instead have a list of all person values, with each person 
being given a different value for their state:
- Healthy, unvaccinated = 0
- Healthy, vaccinated = 1
- Sick = 2
- Dead = 3

As a result, I gained the ability to enumerate and loop over lists in python
much more quickly, and the generation of my list did not take as long as 
creating `x` number of person objects.


