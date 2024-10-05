import matplotlib.pyplot as plt
import numpy as np


def show_city_nvdi(masked_array: np.ndarray, city_name: str) -> None:
    """Show the NDVI image of the city.

    Note : The image should be a masked array with the NDVI values.

    Parameters
    ----------
    masked_array : np.ndarray
        The masked array of the NDVI values.
    city_name : str
        The name of the city.
    """

    plt.figure(figsize=(10, 8))
    plt.imshow(masked_array, cmap="YlGn", vmin=0, vmax=1)
    plt.title(f"Summer 2022 NDVI image of {city_name}")
    plt.axis("off")
    plt.colorbar(ax=plt.gca(), orientation="horizontal", shrink=0.5)
    plt.show()
