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
    lam = pm.Uniform("lambda", upper=20)
    normal = pm.Poisson("poisson", mu=lam, observed=sample)
    
# MODEL RUN
with model:
    step = pm.Metropolis()
    trace = pm.sample(50000, step=step)
    burned_trace = trace[45000:]

# LAMBDA - 95% CONF INTERVAL
lambdas = burned_trace["lambda"]
lambda_est_95 = np.mean(lambdas) - 2*np.std(lambdas), np.mean(lambdas) + 2*np.std(lambdas)
print("95% of sampled lambdas are between {:0.3f} and {:0.3f}".format(*lambda_est_95))

# SAMPLE DISTRIBUTION
cnt = Counter(sample)
_, values = zip(*sorted(cnt.items()))
plt.bar(range(len(values)), values/np.sum(values), alpha=0.25);

# TRUE CURVE
plt.plot(range(18), poisson.pmf(k=range(18), mu=lambda_real), color="#fc4f30")

# ESTIMATED CURVE
plt.plot(range(18), poisson.pmf(k=range(18), mu=np.mean(lambdas)), color="#e5ae38")

# LEGEND
plt.text(x=6, y=.06, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=3.5, y=.14, s="true distrubtion", rotation=60, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=1, y=.08, s="estimated distribution", rotation=60, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(17)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.0009, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = 0.19, s = "Poisson Distribution - Parameter Estimation",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = 0.17, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a Poisson distribution with $\lambda = 7$.\nAlso the estimated distrubution with $\lambda \sim {:.3f}$ is shown (yellow).'.format(np.mean(lambdas)),
         fontsize = 19, alpha = .85)
plt.text(x = -2.5,y = -0.02,
         s = '   ©Joshua Görner                                                                                                                                                   github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');