import logging
import enum

logger = logging.getLogger(__name__)

class TrendType(enum.Enum):
    unknown = 0
    increasing = 1
    decreasing = 2

    def __str__(self):
        return self.name

class TrendError(Exception):
    pass

class InvalidTrendTypeError(TrendError):
    def __init__(self, trend_type):
        self.trend_type = trend_type
        super().__init__(f'Invalid trend type: {trend_type}')

    def __str__(self):
        return self.message
