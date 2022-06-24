# Exemple d extrait script __init__.py
# import de la bibliothèque de programmation Python et prends en charge des tableaux
# Une image au finale est un tableau Numpy standard contenant des pixels de points de données

import logging
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import json
import time
from requests import get, post
import os
from collections import OrderedDict
import numpy as np
