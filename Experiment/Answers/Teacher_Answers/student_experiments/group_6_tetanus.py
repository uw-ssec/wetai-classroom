# Experiment for Group 6

###  Experiment Notes  ###
#Difficulty:  Easy
#Submitter: Ari Sinervo, Dylan Louie
#WetAI Account: 8822 (Ari, 1635444)
#Notebook: http://54.183.203.115:8822/notebooks/work/Experiment/Experiment_Introduction.ipynb
#Summary: Simple tetanus like pattern

 

####################
####################
# Stim Code
####################
####################  
stim_list = []
stim_hz = 25
stim_list.append(('stim',[0,1,2],150,200))
stim_list.append( ('next',None) )
stim_list = stim_list *  int( 5 * 60 * stim_hz )

