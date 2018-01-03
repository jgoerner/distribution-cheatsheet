# IMPORTS
import pymc3 as pm
import numpy as np
from scipy.stats import binom
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

##### DATA GENERATION #####
# DRAW A SAMPLE
np.random.seed(42)
sample = stats.binom.rvs(p=0.3, n=200, size=1000)

##### SIMULATION #####
# MODEL BUILDING
with pm.Model() as model:
    p = pm.Beta("p", 1, 1)
    n = pm.DiscreteUniform("n", lower=sample.max(), upper=10*sample.max())
    binomial = pm.Binomial("binomial", p=p, n=n, observed=sample)
    
# MODEL RUN
with model:
    step = pm.Metropolis()
    trace = pm.sample(100000, step=step)
    burned_trace = trace[50000:]

# P - 95% CONF INTERVAL
ps = burned_trace["p"]
ps_est_95 = ps.mean() - 2*ps.std(), ps.mean() + 2*ps.std()
print("95% of sampled ps are between {:0.3f} and {:0.3f}".format(*ps_est_95))

# N - 95% CONF INTERVAL
ns = burned_trace["n"]
ns_est_95 = ns.mean() - 2*ns.std(), ns.mean() + 2*ns.std()
print("95% of sampled Ns are between {:0.3f} and {:0.3f}".format(*ns_est_95))

##### PLOTTING #####
# SAMPLE
plt.hist(sample, 
         bins=30, 
         normed=True,
         alpha=.25,
        )

# TRUE CURVE
plt.plot(np.arange(40, 90), 
         stats.binom.pmf(np.arange(40, 90), 
                         p=0.3, 
                         n=200,
                        ),
        )

# ESTIMATED CURVE
plt.plot(np.arange(40, 90), 
         stats.binom.pmf(np.arange(40, 90), 
                         p=burned_trace["p"].mean(), 
                         n=burned_trace["n"].mean(),
                        ),
        )

# LEGEND
plt.text(x=58, y=.03, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=48, y=.055, s="true distrubtion", rotation=50, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=68, y=.055, s="estimated distribution", rotation=-50, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(40, 91)[::4])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.0009, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = 34, y = 0.135, s = "Binomial Distribution - Parameter Estimation (MCMC)",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = 34, y = 0.12, 
         s = 'Depicted below is the distribution of a sample drawn from a Binomial distribution with $N = 100$\nand $p = 0.3$. Additionally the estimated distrubution with $N \sim {:.3f}$ and $p \sim {:.2f}$ is shown.'.format(np.mean(ns), np.mean(ps)),
         fontsize = 19, alpha = .85)
plt.text(x = 34, y = -0.02,
         s = '   ©Joshua Görner                                                                                                                                                   github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');