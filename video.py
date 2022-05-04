

import geopandas as gpd
import matplotlib.pyplot as plt
from cartopy.io.img_tiles import GoogleTiles
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import numpy as np
import datetime
from multiprocessing import Pool

outdir = 'results'

gdf = gpd.read_file('ProgMapShape.shp')
gdf = gdf[['geometry', 'timeinint']]
gdf = gdf.sort_values(by=['timeinint'])


# In[2]:


class ShadedReliefESRI(GoogleTiles):
    # shaded relief
    def _image_url(self, tile):
        x, y, z = tile
        url = (
            'https://server.arcgisonline.com/ArcGIS/rest/services/'                'World_Street_Map/MapServer/tile/{z}/{y}/{x}.jpg').format(
            z=z, y=y, x=x)
        return url


def main_code(ii):
    fig1 = plt.figure(1, figsize=(15, 13))
    ax = plt.axes(projection=ShadedReliefESRI().crs)
    extent = [-121.572, -120.376, 40.5832, 39.861]

    ax.set_extent(extent)
    ax.add_image(ShadedReliefESRI(), 9)  # the value '14' is the scale, larger the domain smaller the scale should be

    time = gdf.iloc[ii].timeinint

    for gg in np.arange(0, ii + 2, 1):
        geom = gdf.iloc[gg].geometry

        for pp in geom:
            xs, ys = pp.exterior.xy
            ax.fill(xs, ys, alpha=0.8, fc='b', transform=ccrs.PlateCarree())

    dt = datetime.datetime.fromtimestamp(time)
    print(dt)

    ax.set_xticks(np.linspace(extent[0], extent[1], 7), crs=ccrs.PlateCarree())  # set longitude indicators
    ax.set_yticks(np.linspace(extent[2], extent[3], 7)[1:], crs=ccrs.PlateCarree())  # set latitude indicators
    lon_formatter = LongitudeFormatter(number_format='0.2f', degree_symbol=u'\N{DEGREE SIGN}',
                                       dateline_direction_label=True)  # format lons
    lat_formatter = LatitudeFormatter(number_format='0.2f', degree_symbol=u'\N{DEGREE SIGN}')  # format lats
    ax.xaxis.set_major_formatter(lon_formatter)  # set lons
    ax.yaxis.set_major_formatter(lat_formatter)  # set lats
    ax.xaxis.set_tick_params(labelsize=14, rotation=30)
    ax.yaxis.set_tick_params(labelsize=14)
    txt = ax.text(0.5, 1.05, dt, horizontalalignment='center', verticalalignment='center', transform=ax.transAxes,
                  fontsize=16)

    plt.savefig(outdir + '/{:02d}.png'.format(ii))
    txt.remove()
    plt.close()
    print(ii)


def main():
    p = Pool(processes=2)
    p.map(main_code, [ii for ii in np.arange(0, gdf.shape[0] + 2, 2)])

    p.close()


if __name__ == '__main__':
    main()
