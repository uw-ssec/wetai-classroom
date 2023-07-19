# Experiment for Group 5

###  Experiment Notes  ###
#Difficulty: Easy
#Submitter: Bradley Tait, 
#WetAI Account: 8824 (1677536)
#Notebook: http://54.183.203.115:8824/notebooks/work/Experiment/Experiment_Introduction.ipynb
#Summary: Simple tetanus like pattern



    

####################
####################
# Stim Code
####################
####################  
stim_list = []
stim_hz = 5
stim_list.append(('stim',[0,1],150,200))
for i in range(4):
    stim_list.append(('delay',33))
    stim_list.append(('stim',[1],150,400))
stim_list.append( ('next',None) )
stim_list = stim_list *  int( 5 * 60 * stim_hz )



