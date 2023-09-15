#Question:

#A clinic has implemented an online appointement booking system where patients sign
#up online for a 30-minute, or 1-hour appointmnet each day between 5am - 9am. Patients
#are then seen by a doctor between 9am - 6pm. The clinic anticipates that each day,
#the number of patients who request 1-hour appointments will be distributed as a 
#negative Binomial (n = 0.64, p = 0.02), and the number of patients who request
#30- minute appointments will be distributed as a Poisson (lam=45). Every idle minute
#costs the clinic $2 in support and operational costs. If the clinic can bill$55 for a
#30-minute appointment, and $100 for a 1-hour appointment, how many physicians should
#the clinic employ in the practice to maximize profit and how much can the clinic 
#expect to ear per day on average? Note that no overtime appointments are available,
#some will not be seen (they will go to anotehr clinic). Make sure that longer
#appointments have priority over shorter appointments due to their more serious nature. 


import numpy as np
import math
import time
from matplotlib import pyplot as plt
     
start = time.time()

#Simulation Parameters
numofdocs = 12
Trials = 1_000_0 #number of trials to be executed

#Creation of emply lists as to append future values
a = []
b = []
c = []
d = []
e = []
g = []

#Appending the # of doctors
for i in range(numofdocs):
    a.append(i)

#lFirstly Looping through the number of doctorcs
for i in range(numofdocs):

    def simulation(i, Trials): #Creation of the simulation with # of doctors
    
        x = i*540 # Number of doctors x the minutes they are available
        profits = [0]*Trials
        costs = [0]*Trials
        
        for j in range(Trials):
            
            idle_cost = 0
            profit = 0

            #The Distribution Frequency of Clients
            ha = np.random.negative_binomial(0.64, 0.02)*60 #Hour Appointments          
            hha = np.random.poisson(45)*30 #Half-hour Appointments
    
            if ha >= x: #if else statements calculating the total costs
                profit += i*100*9
                idle_cost += 0
    
            else:
                profit += (ha/60)*100 
                y = x - ha
                if hha >= y:
                    profit += (y/30)*55
                else:
                    profit += (hha/30)*55
                    z = y - hha
                    idle_cost += z*2
            
            profits[j] = profit
            costs[j] = idle_cost
        
        Avg_GP = (sum(profits) - sum(costs))/Trials #Average Gross profit
         
        for i in range(Trials): 
            gp = profits[i] - costs[i]
            j =+ (gp-Avg_GP)*(gp-Avg_GP)
        
        Se = (math.sqrt(j/(Trials-1)))/math.sqrt(Trials) #Standard Error

        Avg_c = sum(costs)/Trials
        Avg_p = sum(profits)/Trials
        IdleTime = Avg_c/120
        
        b.append(Avg_GP) 
        c.append(Se)
        d.append(Avg_c)
        e.append(Avg_p)
        g.append(IdleTime)

    simulation(i, Trials)

#Creation of dictionaries to find optimal number of doctors and related stats
Dic = {b[i]: a[i] for i in range(numofdocs)}
Dic2 = {b[i] : c[i] for i in range(numofdocs)}
Dic3 = {b[i] : d[i] for i in range(numofdocs)}

end = time.time()

time = end-start

#Output 
print("")
print("Optimal number of doctors: %1.0f" % Dic[max(b)])
print("This will yeild an average daily gross profit of $%0.2f" % max(b))
print("")
print("The Standard Error is of $%0.4f " % Dic2[max(b)])
print("The lower confidence interval at 95%% is $%2.4f" %(max(b) -  1.96*(Dic2[max(b)])))
print("The upper confidence interval at 95%% is $%2.4f" %(max(b) + 1.96*(Dic2[max(b)])))
print("")
print("There is an average idle time of approximately %1.0f" %(Dic3[max(b)]/120), "hours")
print("Idle cost inccured is averaged at $%0.2f" %(Dic3[max(b)]))
print('')
print('Time Elapsed: %3.2f Seconds' %time)
print('Time Elapsed: %2.2f Minutes' %(time/60))
print('')
print('Total number of simulations performed: ', f'{numofdocs*Trials:,}')

#Graphical interpretation of results
fig, axs = plt.subplots(1, 2, figsize=(9, 3))
axs[0].set_xlabel("Number of Doctors")
axs[1].set_xlabel("Number of Doctors")
axs[0].set_ylabel("Amounts")
axs[1].set_ylabel("Idle Hours")
axs[0].plot(a, b, linestyle ='-', marker= 'o', label='Average Gross Profit')
axs[0].plot(a, d, linestyle ='-', marker= 'o', color='red', label='Average Cost')
axs[0].plot(a, e, linestyle ='-', marker= 'o', color='green', label='Average Profit')
axs[1].plot(a, g, linestyle ='-', marker= 'o', color='purple', label='Idle Time')
plt.show()
