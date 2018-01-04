# IMPORTS
from collections import Counter
import numpy as np
from scipy.stats import geom
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
p_real = 0.3

# DRAW A SAMPLE OF N=100
np.random.seed(42)
sample = geom.rvs(p=p_real, size=100)

# ESTIMATE P
p_est = 1.0/np.mean(sample)
print("Estimated p: {}".format(p_est))

##### PLOTTING #####
# SAMPLE DISTRIBUTION
cnt = Counter(sample)
cnt[0] = 0 # added to fit pmf
_, values = zip(*sorted(cnt.items()))
plt.bar(range(len(values)), values/np.sum(values), alpha=0.25);

# TRUE CURVE
plt.plot(range(18), geom.pmf(k=range(18), p=p_real), color="#fc4f30")

# ESTIMATED CURVE
plt.plot(range(18), geom.pmf(k=range(18), p=p_est), color="#e5ae38")

# LEGEND
plt.text(x=2, y=.06, s="sample", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=6.5, y=.075, s="true distrubtion", rotation=-15, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=2, y=.275, s="estimated distribution", rotation=-60, alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(17)[::2])
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.002, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -2.5, y = 0.425, s = "Geometric Distribution - Parameter Estimation",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -2.5, y = 0.375, 
         s = 'Depicted below is the distribution of a sample (blue) drawn from a Geometric distribution with\n$p = 0.3$ (red). Also the estimated distrubution with $p \sim {:.3f}$ is shown (yellow).'.format(np.mean(sample)),
         fontsize = 19, alpha = .85)
plt.text(x = -2.5,y = -0.04,
         s = '   ©Joshua Görner                                                                                                                                                github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');