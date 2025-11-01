import re
import uuid, random
import logging as log

from fastapi import APIRouter, HTTPException

from services.car_consulting_service import find_insurance_policy_by_plate, find_discount_by_customer_id_and_payment_method
from helpers.basemodel_helper import MyBaseModel

router = APIRouter()

# 
# 
class CarConsultingRequest(MyBaseModel):
    license_plate: str
    payment_method: str

# 
# 
class CarConsultingResponse(MyBaseModel):
    is_valid: bool
    license_plate: str
    percentage_discount: int | None = None
    vehicle_model: str | None = None
    vehicle_make: str | None = None
    token: str | None = None


# 
# 
@router.post("/")
def car_consulting(entry: CarConsultingRequest) -> CarConsultingResponse:
    log.debug(f"[init] car_consulting({entry.license_plate})")

    if not is_valid_plate(entry.license_plate):
        raise HTTPException(status_code=400, detail="Placa invalida")


    insurance = find_insurance_policy_by_plate(entry.license_plate)
    log.debug(f"Insurance: {insurance.__repr__()}")


    if insurance is None:
        return CarConsultingResponse(is_valid=False, license_plate=entry.license_plate)
    else:
        return CarConsultingResponse(
            is_valid=True,
            license_plate=insurance.license_plate,
            percentage_discount=find_discount_by_customer_id_and_payment_method(insurance.customer_id, entry.payment_method),
            vehicle_model=insurance.vehicle_model,
            vehicle_make=insurance.vehicle_make,
            token=str(uuid.uuid4())
        )





# 
# 
PLATE_REGEX = re.compile(r'^[A-Z]{3}\d{4}$|^[A-Z]{3}\d[A-Z]\d{2}$')

def is_valid_plate(plate: str) -> bool:

    log.debug(f"_is_valid_plate({plate})")

    if plate is None:
        return False

    _plate = plate.replace(" ", "").replace("-", "")
    _plate = _plate.upper()

    log.debug(f"{_plate} ... {len(_plate)} ... {len(_plate) != 7}")

    if len(_plate) != 7:
        return False

    return bool(PLATE_REGEX.match(_plate))

