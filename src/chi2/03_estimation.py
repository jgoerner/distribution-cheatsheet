# IMPORTS
import numpy as np
import scipy.stats as stats
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

##### COMPUTATION #####
# DECLARING THE "TRUE" PARAMETERS UNDERLYING THE SAMPLE
k_real = 2

# DRAW A SAMPLE OF N=1000
np.random.seed(42)
sample = stats.chi2.rvs(df=k_real, size=1000)

# ESTIMATE K
k_est = np.mean(sample)
print("Estimated k: {}".format(k_est))

##### PLOTTING #####
# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25)

# TRUE CURVE
plt.plot(np.linspace(0, 18, 1000), stats.chi2.pdf(np.linspace(0, 18, 1000),df=k_real))

# ESTIMATED CURVE
plt.plot(np.linspace(0, 18, 1000), stats.chi2.pdf(np.linspace(0, 18, 1000),df=k_est))

# LEGEND
plt.text(x=.75, y=.1, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=3, y=.15, s="true distrubtion", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=1, y=.4, s="estimated distribution", alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(0, 19)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.003, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2, y = 0.675, s = "Chi-Squared Distribution - Parameter Estimation",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2, y = 0.6, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a Chi-Squared distribution with \n$k=2$ (red). Also the estimated distrubution with $k \sim {:.3f} $ is shown (yellow).'.format(np.mean(sample)),
         fontsize = 19, alpha = .85)
plt.text(x = -2,y = -0.075,
         s = '   ©Joshua Görner                                                                                                                                               github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');