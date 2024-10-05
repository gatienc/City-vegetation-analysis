import geopandas as gpd
import numpy as np
import rasterio


def get_masked_image(image_path: str, polygon: gpd.GeoDataFrame):
    """
    Get a masked image based on a given image path and polygon.
    Parameters
    ----------
    image_path : str
        The path to the image file.
    polygon : shapely.geometry.Polygon
        The polygon used for masking.

    Returns
    -------
    numpy.ma.masked_array
        The masked image array.
    """
    with rasterio.open(image_path) as dataset:
        dataset_array = dataset.read(1)
        mask = rasterio.features.geometry_mask(
            [polygon], out_shape=dataset_array.shape, transform=dataset.transform, invert=False
        )
        masked_array = np.ma.masked_array(dataset_array, mask)
        masked_array = np.ma.masked_array(dataset_array, mask)
    return masked_array
