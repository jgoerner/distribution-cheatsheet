# IMPORTS
import pymc3 as pm
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.style as style
from IPython.core.display import HTML

# PLOTTING CONFIG
%matplotlib inline
style.use('fivethirtyeight')
plt.rcParams["figure.figsize"] = (14, 7)
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: center;
}
</style>
""")
plt.figure(dpi=100)

##### GENERATE DATA #####
A_TRUE = 75
B_TRUE = 100
np.random.seed(42)
sample = stats.beta.rvs(a=A_TRUE, b=B_TRUE, size=200)

##### SIMULATION #####
# MODEL BUILDING
with pm.Model() as model:
    a = pm.Uniform("a", upper=200)
    b = pm.Uniform("b", upper=200)
    beta = pm.Beta("beta", alpha=a, beta=b, observed=sample)
    
# MODEL RUN
with model:
    step = pm.Metropolis()
    trace = pm.sample(100000, step=step)
    burned_trace = trace[20000:]

# A - 95% CONF INTERVAL
a_s = burned_trace["a"]
a_est_95 = np.mean(a_s) - 2*np.std(a_s), np.mean(a_s) + 2*np.std(a_s)
print("95% of sampled mus are between {:0.3f} and {:0.3f}".format(*a_est_95))

# A - 95% CONF INTERVAL
b_s = burned_trace["b"]
b_est_95 = np.mean(b_s) - 2*np.std(b_s), np.mean(b_s) + 2*np.std(b_s)
print("95% of sampled mus are between {:0.3f} and {:0.3f}".format(*b_est_95))

#### PLOTTING #####
# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25)

# TRUE CURVE
plt.plot(np.linspace(0.3, 0.6, 100), stats.beta.pdf(np.linspace(0.3, 0.6, 100),a=A_TRUE, b=B_TRUE))

# ESTIMATED CURVE MCMC
plt.plot(np.linspace(0.3, 0.6, 100), stats.beta.pdf(np.linspace(0.3, 0.6, 100),a=a_s.mean(), b=b_s.mean()))

# LEGEND
plt.text(x=0.4125, y=2.5, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=0.475, y=8, s="true distrubtion", rotation=-55, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=0.34, y=9, s="estimated distribution", rotation=55, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.1, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = 0.275, y = 17, s = "Beta Distribution - Parameter Estimation (MCMC)",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = 0.275, y = 15, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a beta distribution with '+ r'$\alpha = 75$'+'\nand ' + r'$\beta = 100$ (red). Also the estimated distrubution with $\alpha \sim {:.3f} $ and $\beta \sim {:.3f} $ is shown.'.format(a_s.mean(), b_s.mean()),
         fontsize = 19, alpha = .85)
plt.text(x = 0.275,y = -1.5,
         s = '   ©Joshua Görner                                                                                                                                           github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');