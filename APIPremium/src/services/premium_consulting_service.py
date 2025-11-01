import random
import uuid
from faker import Faker

from models.classification_consulting import InsuranceClass


faker = Faker("pt_BR")


def get_classification_by_plate(plate: str) -> InsuranceClass | None:

    is_valid = random.choice([True, False])
    if is_valid:
        return InsuranceClass(
            id=random.randint(1, 1000),
            customer_id=str(uuid.uuid4()),
            classification=random.choice(["PREMIUM", "PRIVATE", "BASIC"])
        )

    return None



def find_discount_by_classification(classification: str) -> int:
    if classification.upper() == "PREMIUM":
        return 100
    elif classification.upper() == "PRIVATE":
        return 50
    else:
        return 0
