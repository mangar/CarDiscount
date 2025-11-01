from helpers.basemodel_helper import MyBaseModel


class InsuranceClass(MyBaseModel):
    id: int
    customer_id: str
    classification: str 
