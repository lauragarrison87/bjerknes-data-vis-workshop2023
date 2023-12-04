import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap

# Dataset air.mon.mean.nc
# Download at ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc

airtemps = xr.open_dataset('air.mon.mean.nc')

# mean_by_year = airtemps.air.groupby(air.time.dt.year).mean(dim='time')
# just_50s = airtemps.air.sel(time=slice('1950-01-01','1959-12-31'))
# europe = airtemps.air.sel(lat=slice(75.,25.),lon=slice(-30.,50.))

# first year
air = airtemps.air.isel(time=0)

# Set up four subplots
f, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2, figsize=(8, 9))

air.plot.imshow(ax=ax1, cbar_kwargs={"label": "°C"}, cmap="jet")
ax1.set_title("cmap=jet (sorry)")
ax1.set_xlabel("")

air.plot.imshow(ax=ax2, cbar_kwargs={"label": "°C"}, cmap="twilight")
ax2.set_title("cmap=twilight")
ax2.set_xlabel("")
ax2.set_ylabel("")

air.plot.imshow(ax=ax3, cbar_kwargs={"label": "°C"}, cmap="hot")
ax3.set_title("cmap=hot")

air.plot.imshow(ax=ax4, cbar_kwargs={"label": "°C"}, cmap="gist_heat")
ax4.set_title("cmap=gist_heat")
ax4.set_ylabel("")

air.plot.imshow(ax=ax5, cbar_kwargs={"label": "°C"}, cmap="RdBu")
ax5.set_title("cmap=BuRd")

origin_cmap = mpl.colormaps['RdBu'].resampled(256)
newcolors = origin_cmap(np.linspace(0, 1, 256)) # TODO what does this do
highlight = (0/256, 0/256, 0/256, 1) # R G B A
newcolors[170:195, :] = highlight
my_cmap = ListedColormap(newcolors)

air.plot.imshow(ax=ax6, cbar_kwargs={"label": "°C"}, cmap=my_cmap)
ax6.set_title("cmap=self-defined")
ax6.set_ylabel("")

plt.tight_layout()
plt.show()
