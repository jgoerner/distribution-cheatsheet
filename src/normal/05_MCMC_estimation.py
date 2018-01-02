# IMPORTS
import pymc3 as pm
import numpy as np
from scipy.stats import norm
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

##### SIMULATION #####
# MODEL BUILDING
with pm.Model() as model:
    mu = pm.Uniform("mu", upper=20)
    std = pm.Uniform("std", upper=5)
    normal = pm.Normal("normal", mu=mu, sd=std, observed=sample)
    
# MODEL RUN
with model:
    step = pm.Metropolis()
    trace = pm.sample(50000, step=step)
    burned_trace = trace[45000:]
    
# MU - 95% CONF INTERVAL
mus = burned_trace["mu"]
mu_est_95 = np.mean(mus) - 2*np.std(mus), np.mean(mus) + 2*np.std(mus)
print("95% of sampled mus are between {:0.3f} and {:0.3f}".format(*mu_est_95))

# STD - 95% CONF INTERVAL
stds = burned_trace["std"]
std_est_95 = np.mean(stds) - 2*np.std(stds), np.mean(stds) + 2*np.std(stds)
print("95% of sampled sigmas are between {:0.3f} and {:0.3f}".format(*std_est_95))

#### PLOTTING #####
# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25)

# TRUE CURVE
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),loc=mu_real, scale=sigma_real))

# ESTIMATED CURVE MCMC
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),loc=np.mean(mus), scale=np.mean(stds)))

# LEGEND
plt.text(x=9.5, y=.1, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=7, y=.2, s="true distrubtion", rotation=55, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=5, y=.12, s="estimated distribution", rotation=55, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = 0, y = 0.3, s = "Normal Distribution - Parameter Estimation (MCMC)",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = 0, y = 0.265, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a normal distribution with $\mu = 10$\nand $\sigma = 2$ (red). Also the estimated distrubution with $\mu \sim {:.3f} $ and $\sigma \sim {:.3f} $ is shown (yellow).'.format(np.mean(mus), np.mean(stds)),
         fontsize = 19, alpha = .85)
plt.text(x = 0,y = -0.025,
         s = '   ©Joshua Görner                                                                                                                                                   github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');