import json
import os

import pandas as pd
from flask import Flask, request, send_from_directory, abort

app = Flask(__name__)
UPLOAD_DIRECTORY = "."

conversions = ['h5', 'pk1', 'feather', 'parquet']