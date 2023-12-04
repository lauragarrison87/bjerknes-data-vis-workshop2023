import cartopy.crs as ccrs
import matplotlib as mpl
import matplotlib.pyplot as plt
import xarray as xr

ds = xr.open_dataset('air.mon.mean.nc')
air = ds.air

print(air)


fig,axis = plt.subplots(
    1, 1, 
    subplot_kw = {"projection" : ccrs.Mollweide()}
)

air.sel(time="1975-12-01").plot(
    ax=axis,
    transform=ccrs.PlateCarree(),  # this is important! (is rectangular grid one that xarray ex are using)
    # usual xarray stuff
    cbar_kwargs={"orientation": "horizontal", "shrink": 0.7}, #from matplotlib args - arrows indicate outliers in map
    robust=True, # handling of outliers
    # vmin=-74,
    # vmax=74,
    # cmap="RdBu_r"
)
axis.coastlines()  # cartopy function


plt.show()

