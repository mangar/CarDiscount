import re
import uuid, random
import logging as log

from fastapi import APIRouter, HTTPException

from services.premium_consulting_service import get_classification_by_plate, find_discount_by_classification
from helpers.basemodel_helper import MyBaseModel

router = APIRouter()

# 
# 
class ClassificationConsultingRequest(MyBaseModel):
    license_plate: str
    customer_id: str | None = None
    payment_method: str | None = None
    payment_ammount: float | None = None

# 
# 
class ClassificationConsultingResponse(MyBaseModel):
    is_valid: bool
    license_plate: str
    percentage_discount: int | None = None
    token: str | None = None


# 
# 
@router.post("/")
def classificatioon_consulting(entry: ClassificationConsultingRequest) -> ClassificationConsultingResponse:
    log.debug(f"[init] classificatioon_consulting({entry.__repr__()})")

    if not is_valid_plate(entry.license_plate):
        raise HTTPException(status_code=400, detail="Placa invalida")


    classification = get_classification_by_plate(entry.license_plate)
    log.debug(f"Classification: {classification.__repr__()}")


    if classification is None or classification.classification.upper() == "BASIC":
        return ClassificationConsultingResponse(is_valid=False, license_plate=entry.license_plate)
    else:
        return ClassificationConsultingResponse(
            is_valid=True,
            license_plate=entry.license_plate,
            percentage_discount=find_discount_by_classification(classification.classification),
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

