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

# PDF
plt.bar(left=np.arange(10), 
        height=(stats.geom.pmf(np.arange(10), p=.5)/np.max(stats.geom.pmf(np.arange(10), p=.5))), 
        width=.75,
        alpha=0.75
       )

# CDF
plt.plot(np.arange(10),
         stats.geom.cdf(np.arange(10), p=.5),
         color="#fc4f30",
        )

# LEGEND
plt.text(x=3.5, y=.3, s="pmf (normed)", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=2.5, y=.7, s="cdf", alpha=.75, weight="bold", color="#fc4f30")

# TICKS
plt.xticks(range(11))
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0.005, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -1.5, y = 1.25, s = "Geometric Distribution - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -1.5, y = 1.1, 
         s = 'Depicted below are the normed probability mass function (pmf) and the cumulative density\nfunction (cdf) of a Geometric distributed random variable $ y \sim Geom(p) $, given parameter $p =0.5 $.',
         fontsize = 19, alpha = .85)
plt.text(x = -1.5,y = -0.125,
         s = '   ©Joshua Görner                                                                                                                                                   github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');