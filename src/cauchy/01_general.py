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
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100))/np.max(stats.cauchy.pdf(np.linspace(-6, 6, 100))),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100))/np.max(stats.cauchy.pdf(np.linspace(-6, 6, 100))),
                 alpha=.15,
                )
# CDF
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.cdf(np.linspace(-6, 6, 100)),
        )

# LEGEND
plt.text(x=2, y=.25, s="pdf", rotation=-50, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=-.4, y=.5, s="cdf", rotation=55, alpha=.75, weight="bold", color="#fc4f30")

# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -7.25, y = 1.25, s = "Cauchy - Overview",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -7.25, y = 1.1,
         s = ("Depicted below are the normed probability density function (pdf) and the cumulative density \nfunction (cdf) of a cauchy distributed random variable $ x \sim Cauchy(\lambda , x_0)$"
              " given $\lambda = 1,  x_0 = 0$"),
         fontsize = 19, alpha = .85)
plt.text(x = -7.25,y = -0.2,
         s = '   © Hagen Mohr                                                                                                                                               github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');