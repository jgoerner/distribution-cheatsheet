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

# PDF lambda = 1
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100)),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100)),
                 alpha=.15,
                )

# PDF lambda = 2
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100), scale=2),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100),scale=2),
                 alpha=.15,
                )

# PDF lambda = 0.5
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100), scale=0.5),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100),scale=0.5),
                 alpha=.15,
                )

# LEGEND
plt.text(x=-1.25, y=.3, s="$ \lambda = 1$", rotation=51, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=-2.5, y=.13, s="$ \lambda = 2$", rotation=11, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=-0.75, y=.55, s="$ \lambda = 0.5$", rotation=75, alpha=.75, weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -7.25, y = 0.77, s = "Cauchy Distribution - $ \lambda $",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -7.25, y = 0.68,
         s = ("Depicted below are three Cauchy distributed random variables with varying $\lambda$. " +
             "It becomes \napparent, that $\lambda$ streches or tightens the distribution" +
             " (the smaller $\lambda$ the higher the peak)"),
         fontsize = 19, alpha = .85)
plt.text(x = -7.25,y = -0.1,
         s = '   © Hagen Mohr                                                                                                                                               github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');