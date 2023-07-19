# Experiment for Group 6

###  Experiment Notes  ###
#Difficulty: Hard
#Submitter: Nicholas Rondoni
#WetAI Account: 8843 (1493370)
#Notebook: http://54.183.203.115:8843/notebooks/work/Experiment/Compiled_Work.ipynb
#Summary: Random walk of stim strengths

 
# import packages
from math import sqrt
from scipy.stats import norm
import numpy as np



####################
####################
# Student's helper code
####################
####################  
def brownian(x0, n, dt, delta, out=None):
    """
    Generate an instance of Brownian motion (i.e. the Wiener process):

        X(t) = X(0) + N(0, delta**2 * t; 0, t)

    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1) and
    [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.
    
    Written as an iteration scheme,

        X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)


    If `x0` is an array (or array-like), each value in `x0` is treated as
    an initial condition, and the value returned is a numpy array with one
    more dimension than `x0`.

    Arguments
    ---------
    x0 : float or numpy array (or something that can be converted to a numpy array
         using numpy.asarray(x0)).
        The initial condition(s) (i.e. position(s)) of the Brownian motion.
    n : int
        The number of steps to take.
    dt : float
        The time step.
    delta : float
        delta determines the "speed" of the Brownian motion.  The random variable
        of the position at time t, X(t), has a normal distribution whose mean is
        the position at time t=0 and whose variance is delta**2*t.
    out : numpy array or None
        If `out` is not None, it specifies the array in which to put the
        result.  If `out` is None, a new numpy array is created and returned.

    Returns
    -------
    A numpy array of floats with shape `x0.shape + (n,)`.
    
    Note that the initial value `x0` is not included in the returned array.
    """

    x0 = np.asarray(x0)

    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))

    # If `out` was not given, create an output array.
    if out is None:
        out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples. 
    np.cumsum(r, axis=-1, out=out)

    # Add the initial condition.
    out += np.expand_dims(x0, axis=-1)

    return out



def stim_creator():
    
    T = 400 #4.74       # Total time.
    N = 19 #3000        # Number of steps.
    dt = T/N           # Time step size
    delta = 3.5 #1.18 #np.sqrt(dt)    # The Wiener process parameter.
    m = 1       # Number of realizations to generate.
    x = np.empty((m,N+1))   # Create an empty array to store the realizations.
    x[:, 0] = 150        # Initial values of x.
    
    global stim_pattern
    brownian(x[:,0], N, dt, delta, out=x[:,1:])

    stim_pattern = []
    for i in range(x.shape[1]):
        if x[0][i] > 250:
            x[0][i] = 245
        if x[0][i] < 50:
            x[0][i] = 45 
        stim_pattern.append(('stim', [0], x[0][i], 20)) # what to do, neuron id, mV, for how many microseconds, at the end determine hz (how many times protocol is repeated within a second).
    
    #stim_pattern.append(('delay', 50))
    stim_pattern.append(('next', None))
    
    return stim_pattern






####################
####################
# Stim Code
####################
####################  
stim_hz = 20
stim_list = []
for i in range( 5 * 60 * stim_hz  ):
    stim_list.extend( stim_creator() )


