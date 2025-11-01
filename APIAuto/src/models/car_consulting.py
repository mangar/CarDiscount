from helpers.basemodel_helper import MyBaseModel
from datetime import datetime


class InsurancePolicy(MyBaseModel):
    id: int
    customer_id: str
    policy_number: str
    policy_expiration_date: datetime
    license_plate: str
    vehicle_model: str
    vehicle_make: str
