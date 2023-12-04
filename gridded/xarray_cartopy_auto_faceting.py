import cartopy.crs as ccrs
import matplotlib as mpl
import matplotlib.pyplot as plt
import xarray as xr

ds = xr.open_dataset('air.mon.mean.nc')
air = ds.air

# fig,axis = plt.subplots(
#     1, 1, 
#     subplot_kw = {"projection" : ccrs.Mollweide()}
# )

facetgrid = air.sel(
        time=["1950-09-01", "1975-09-01", "2000-09-01", "2018-09-01"],
    ).plot(
    col="time",
    col_wrap=2,
    transform=ccrs.PlateCarree(),  # remember to provide this!
    subplot_kws={"projection": ccrs.Mollweide()},
    cbar_kwargs={"orientation": "vertical", "shrink": 0.8, "aspect": 40},
    robust=True,
    cmap="RdBu_r",
    vmin=-40, vmax=40
)

# lets add a coastline to each axis
# great reason to use FacetGrid.map
def draw_coast_on_current():
    plt.gca().coastlines()

# apply function to each facet
facetgrid.map(draw_coast_on_current)

plt.show()
