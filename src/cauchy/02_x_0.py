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

# PDF MU = 0
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100)),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100)),
                 alpha=.15,
                )

# PDF MU = 2
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100), loc=2),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100),loc=2),
                 alpha=.15,
                )

# PDF MU = -2
plt.plot(np.linspace(-6, 6, 100),
         stats.cauchy.pdf(np.linspace(-6, 6, 100), loc=-2),
        )
plt.fill_between(np.linspace(-6, 6, 100),
                 stats.cauchy.pdf(np.linspace(-6, 6, 100),loc=-2),
                 alpha=.15,
                )

# LEGEND
plt.text(x=-1, y=.25, s="$ x_0 = 0$", rotation=70, alpha=.75, weight="bold", color="#008fd5")
plt.text(x=1, y=.25, s="$ x_0 = 2$", rotation=70, alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=-3.125, y=.25, s="$ x_0 = -2$", rotation=70, alpha=.75, weight="bold", color="#e5ae38")


# TICKS
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -7.25, y = 0.395, s = "Cauchy Distribution - $ x_0 $",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -7.25, y = 0.35,
         s = 'Depicted below are three Cauchy distributed random variables with varying $ x_0 $. As one can \neasily see the parameter $x_0$ shifts the distribution along the x-axis.',
         fontsize = 19, alpha = .85)
plt.text(x = -7.25,y = -0.05,
         s = '   © Hagen Mohr                                                                                                                                               github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');