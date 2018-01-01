# %load ./src/normal/04_estimation.py
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

# SAMPLE DISTRIBUTION
plt.hist(sample, bins=50,normed=True, alpha=.25)

# TRUE CURVE
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),loc=mu_real, scale=sigma_real))

# ESTIMATED CURVE
plt.plot(np.linspace(2, 18, 1000), norm.pdf(np.linspace(2, 18, 1000),loc=mu_est, scale=sigma_est))

# LEGEND
plt.text(x=9.5, y=.1, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=7, y=.2, s="true distrubtion", rotation=55, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=5, y=.12, s="estimated distribution", rotation=55, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = 0, y = 0.3, s = "Normal Distribution - Parameter Estimation",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = 0, y = 0.265, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a normal distribution with $\mu = 10$\nand $\sigma = 2$ (red). Additionaly the estimated distrubution with $\mu \sim 9.96 $ and $\sigma \sim 1.94 $ is shown (yellow).',
         fontsize = 19, alpha = .85)
plt.text(x = 0,y = -0.025,
         s = '   ©Joshua Görner                                                                                                                                                   github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');