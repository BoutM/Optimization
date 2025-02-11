# Clinic Optimization: Number of Doctors

What follows is the given optimization problem: 

A clinic has implemented an online appointement booking system where patients sign up online for a 30-minute, or 1-hour appointmnet each day between 5am - 9am. Patients are then seen by a doctor between 9am - 6pm. The clinic anticipates that each day,the number of patients who request 1-hour appointments will be distributed as a negative Binomial (n = 0.64, p = 0.02), and the number of patients who request 30- minute appointments will be distributed as a Poisson (lam=45). Every idle minute costs the clinic $2 in support and operational costs. If the clinic can bill$55 for a 30-minute appointment, and $100 for a 1-hour appointment, how many physicians should the clinic employ in the practice to maximize profit and how much can the clinic expect to ear per day on average? Note that no overtime appointments are available, some will not be seen (they will go to another clinic). Make sure that longer appointments have priority over shorter appointments due to their more serious nature. 


In my approach, I utilize Monte Carlo simulations to locate the optimal solution.
