```python
from django.db import models
from datetime import datetime


class CustomDateTimeField(models.CharField):
    """
    Custom Field for storing datetime in "YYYY-MM-DD hh:mm:ss" format as a string.
    """

    def __init__(self, *args, **kwargs):
        # 기본 max_length 설정 (YYYY-MM-DD hh:mm:ss = 19)
        kwargs["max_length"] = 19
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        """
        Convert the string value from the database to a Python `datetime.datetime`.
        """
        if value is None:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid datetime format in database: {value}")

    def to_python(self, value):
        """
        Convert the value to Python's `datetime.datetime`.
        """
        if isinstance(value, datetime):
            return value
        if value is None:
            return None
        try:
            return datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError(f"Invalid datetime format: {value}")

    def get_prep_value(self, value):
        """
        Prepare the value for saving into the database as a string in "YYYY-MM-DD hh:mm:ss" format.
        """
        if value is None:
            return None
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        raise ValueError(f"Invalid datetime object: {value}")
```



```python
from django.db import models
from datetime import datetime
from .fields import CustomDateTimeField


class CommonModel(models.Model):
    """Common Model Definition"""

    created_at = CustomDateTimeField(auto_now_add=True)
    updated_at = CustomDateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

