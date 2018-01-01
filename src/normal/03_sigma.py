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

# PDF SIGMA = 1
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100), scale=1),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100), scale=1),
                 alpha=.15,
                )

# PDF SIGMA = 2
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100), scale=2),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100), scale=2),
                 alpha=.15,
                )

# PDF SIGMA = 0.5
plt.plot(np.linspace(-4, 4, 100), 
         stats.norm.pdf(np.linspace(-4, 4, 100), scale=0.5),
        )
plt.fill_between(np.linspace(-4, 4, 100),
                 stats.norm.pdf(np.linspace(-4, 4, 100), scale=0.5),
                 alpha=.15,
                )

# LEGEND
plt.text(x=-1.25, y=.3, s="$ \sigma = 1$", rotation=51, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=-2.5, y=.13, s="$ \sigma = 2$", rotation=11, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=-0.75, y=.55, s="$ \sigma = 0.5$", rotation=75, alpha=.75, weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -5, y = 0.98, s = "Normal Distribution - $ \sigma $",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -5, y = 0.87, 
         s = 'Depicted below are three normally distributed random variables with varying $\sigma $. As one can easily\nsee the parameter $\sigma$ "sharpens" the distribution (the smaller $ \sigma $ the sharper the function).',
         fontsize = 19, alpha = .85)
plt.text(x = -5,y = -0.15,
         s = '   ©Joshua Görner                                                                                                                                                 github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');