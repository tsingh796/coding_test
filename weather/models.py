from django.db import models

from coding_test.commons.constants import MISSING_VALUE
from coding_test.commons.models import BaseModel


"""
    Weather model stores data collected every day from stations.
"""


class Weather(BaseModel):
    station_id = models.CharField(
        max_length=20)
    date = models.DateField()
    max_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    min_temp = models.FloatField(
        default=MISSING_VALUE,
    )
    precipitation = models.FloatField(
        default=MISSING_VALUE,
    )

    class Meta:
        unique_together = [
            "station_id",
            "date",
        ]


class StatsModel(BaseModel):
    station_id = models.CharField(
        max_length=50)
    year = models.PositiveSmallIntegerField()
    avg_max_temp = models.FloatField(
        null=True,
    )
    avg_min_temp = models.FloatField(
        null=True,
    )
    total_precipitation = models.FloatField(
        null=True,
    )

    class Meta:
        unique_together = [
            "station_id",
            "year",
        ]
