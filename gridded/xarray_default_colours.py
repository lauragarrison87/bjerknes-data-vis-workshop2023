import xarray as xr
import matplotlib.pyplot as plt

# Dataset air.mon.mean.nc
# Download at ftp://ftp.cdc.noaa.gov/Datasets/ncep.reanalysis.derived/surface/air.mon.mean.nc

airtemps = xr.open_dataset('air.mon.mean.nc')

# mean_by_year = airtemps.air.groupby(air.time.dt.year).mean(dim='time')
# just_50s = airtemps.air.sel(time=slice('1950-01-01','1959-12-31'))
# europe = airtemps.air.sel(lat=slice(75.,25.),lon=slice(-30.,50.))

# first year
air = airtemps.air.isel(time=0)

# Set up four subplots
f, ((ax1, ax2), (ax3, ax4)) = plt.subanywplots(2, 2, figsize=(8, 6))

# The first plot (in kelvins) chooses "viridis" and uses the data's min/max
airk = air + 273.15
airk.plot.imshow(ax=ax1, cbar_kwargs={"label": "K"})
ax1.set_title("Kelvins: default")
ax1.set_xlabel("")

# The second plot (in celsius) now chooses "BuRd" and centers min/max around 0
# This happens automatically when the data range includes the 0 value
air.plot.imshow(ax=ax2, cbar_kwargs={"label": "°C"})
ax2.set_title("Celsius: default")
ax2.set_xlabel("")
ax2.set_ylabel("")

# The center doesn't have to be 0, BuRd will be chosen
airk = air + 273.15
airk.plot.imshow(ax=ax3, center=273.15, cbar_kwargs={"label": "K"})
ax3.set_title("Kelvins: center=273.15")

# Or it can be ignored, viridis is the default
air.plot.imshow(ax=ax4, center=False, cbar_kwargs={"label": "°C"})
ax4.set_title("Celsius: center=False")
ax4.set_ylabel("")

# Make it nice
plt.tight_layout()

plt.show()
