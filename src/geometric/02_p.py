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

# PDF P = .2
plt.scatter(np.arange(11),
            (stats.geom.pmf(np.arange(11), p=.2)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(11),
         (stats.geom.pmf(np.arange(11), p=.2)),
         alpha=0.75,
        )

# PDF P = .5
plt.scatter(np.arange(11),
            (stats.geom.pmf(np.arange(11), p=.5)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(11),
         (stats.geom.pmf(np.arange(11), p=.5)),
         alpha=0.75,
        )

# PDF P = .9
plt.scatter(np.arange(11),
            (stats.geom.pmf(np.arange(11), p=.9)),
            alpha=0.75,
            s=100
       )
plt.plot(np.arange(11),
         (stats.geom.pmf(np.arange(11), p=.9)),
         alpha=0.75,
        )

# LEGEND
plt.text(x=4.25, y=.15, s="$p = 0.2$", alpha=.75, weight="bold", color="#008fd5")
plt.text(x=2.5, y=.25, s="$p = 0.5$", alpha=.75, weight="bold", color="#fc4f30")
plt.text(x=1.5, y=.7, s="$p = 0.9$", alpha=.75, weight="bold", color="#e5ae38")

# TICKS
plt.xticks(range(11))
plt.tick_params(axis = 'both', which = 'major', labelsize = 18)
plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

# TITLE, SUBTITLE & FOOTER
plt.text(x = -1, y = 1.125, s = "Geometric Distribution - $p$",
               fontsize = 26, weight = 'bold', alpha = .75)
plt.text(x = -1, y = 1, 
         s = 'Depicted below are three Geometric distributed random variables with varying $p $. As one can\nsee the parameter $p$ flattens the distribution (the larger p the sharper the distribution).',
         fontsize = 19, alpha = .85)
plt.text(x = -1,y = -0.175,
         s = '   ©Joshua Görner                                                                                                                                             github.com/jgoerner   ',
         fontsize = 14, color = '#f0f0f0', backgroundcolor = 'grey');