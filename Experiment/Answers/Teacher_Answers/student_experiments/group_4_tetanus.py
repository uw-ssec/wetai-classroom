# Experiment for Group 4

###  Experiment Notes  ###
#Difficulty:  Easy
#Submitter: Tanvi Singh
#WetAI Account: 8823 (1993726)
#Notebook: http://54.183.203.115:8823/notebooks/work/Experiment/Experiment_Introduction.ipynb
#Summary: Simple tetanus like pattern

    
####################
####################
# Stim Code
####################
####################    
stim_list = []
stim_hz = 15
stim_list.append(('stim',[0,1,2],150,200))   # voltage: milli-V, time: micro-seconds
#stim_list.append(('delay',66))          # time: milli-seconds
#stim_list.append(('stim',[1],150,200))
stim_list.append( ('next',None) )
#stim_list = stim_list *  int( 5 * 60 * stim_hz )




