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
#Numpy : algèbre linéaire. Sera l interface de programmation des images. Le traitement peut être fait par des opérations matricielles mais aussi par des boucles (même si cela reste moins efficace)
import numpy as np
