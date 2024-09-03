from django.db import models

# Create your models here.
from .db import db_conn

users = db_conn['hospi']