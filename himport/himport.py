import importlib
import os
from requests import get
from himport import utils

def himport(url: str, import_name: str):
    """Imports a link over http

    Args:
        url (str): The url of the python file
        import_name (str): The name you want to use when calling that file
    """
    text = get(url=url).text
    os.mkdir("./hcache")
    utils.TemporaryDirectory("hcache", import_name)
    with open(f"hcache/{import_name}.py", "w+") as cache_file: 
        cache_file.write(text)

    module = importlib.import_module(f"hcache.{import_name}")
    
    return module