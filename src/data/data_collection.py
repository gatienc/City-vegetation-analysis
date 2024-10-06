"""
This module provides functions for data collection.

To use it, please fill your credentials in the .env file.
"""

import os
import sentinelhub


def load_sentinelhub_credentials():
    """
    Load SentinelHub credentials from the user input.

    SH_CLIENT_ID and SH_CLIENT_SECRET are loaded
    from the environment variables.

    Returns
    -------
    sentinelhub.SHConfig
        SentinelHub configuration object
    """
    config = sentinelhub.SHConfig()
    config.sh_client_id = os.environ.get("SH_CLIENT_ID")
    config.sh_client_secret = os.environ.get("SH_CLIENT_SECRET")
    config.sh_token_url = (
        "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"  # noqa E501
    )
    config.sh_base_url = "https://sh.dataspace.copernicus.eu"
    return config


def load_eval_script(evalscript_filename):
    """
    Load the evalscript from the specified evalscript javascript file.

    Returns
    -------
    str
        the evalscript
    """
    script_path = os.path.join(os.path.dirname(__file__), "evalscript", evalscript_filename)
    with open(script_path, "r", encoding="utf-8") as file:
        script_content = file.read()
        return script_content
