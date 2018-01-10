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
x_0_true = 10
lambd_true = 1.5
np.random.seed(42)
sample = stats.cauchy.rvs(loc=x_0_true, scale=lambd_true, size=200)

##### SIMULATION #####
# MODEL BUILDING
with pm.Model() as model:
    x_0 = pm.Uniform("x_0", upper=50) # technically x_0 could take on negative values - not tested here
    lambd = pm.Uniform("lambda", upper=20) # lambda is always > 0
    cauchy = pm.Cauchy("cauchy", alpha=x_0, beta=lambd, observed=sample)

# MODEL RUN
with model:
    trace = pm.sample(draws=100000)
    burned_trace = trace[20000:]

# x_0 - 95% CONF INTERVAL
x_0s = burned_trace["x_0"]
x_0_est_95 = np.mean(x_0s) - 2*np.std(x_0s), np.mean(x_0s) + 2*np.std(x_0s)
print("95% of sampled x_0s are between {:0.3f} and {:0.3f}".format(*x_0_est_95))

# Lambda - 95% CONF INTERVAL
lambds = burned_trace["lambda"]
lambd_est_95 = np.mean(lambds) - 2*np.std(lambds), np.mean(lambds) + 2*np.std(lambds)
print("95% of sampled lambdas are between {:0.3f} and {:0.3f}".format(*lambd_est_95))

#### PLOTTING #####
# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25, range=[-10, 30])

# TRUE CURVE
plt.plot(np.linspace(-10, 30, 50), stats.cauchy.pdf(np.linspace(-10, 30, 50),loc=x_0_true, scale=lambd_true))

# ESTIMATED CURVE MCMC
plt.plot(np.linspace(-10, 30, 50), stats.cauchy.pdf(np.linspace(-10, 30, 50),loc=np.mean(x_0s), scale=np.mean(lambds)))

# LEGEND
plt.text(x=8.5, y=.05, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=13, y=.1, s="true distrubtion", rotation=0, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=-1.5, y=.1, s="estimated distribution", rotation=0, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.001, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -15, y = 0.255, s = "Cauchy - Parameter Estimation (MCMC)",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -15, y = 0.225,
         s = 'Depicted below is the distribution of a sample (blue) drawn from a cauchy distribution with ' + r'$x_0 = 10$' + '\nand ' + r'$\lambda = 1.5$ (red). ' + r'Also the estimated distrubution with $x_0 \sim {:.3f} $ and $\lambda \sim {:.3f} $ is shown (yellow).'.format(np.mean(x_0s), np.mean(lambds)),
         fontsize = 19, alpha = .85)
plt.text(x = -15,y = -0.025,
         s = '   © Hagen Mohr                                                                                                                                                     github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');