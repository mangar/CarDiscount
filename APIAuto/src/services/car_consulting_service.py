import random
import uuid
from faker import Faker

from models.car_consulting import InsurancePolicy


faker = Faker("pt_BR")


def find_insurance_policy_by_plate(plate: str) -> InsurancePolicy | None:

    is_valid = random.choice([True, False])
    if is_valid:
        return InsurancePolicy(
            id=random.randint(1, 1000),
            customer_id=str(uuid.uuid4()),
            policy_number=faker.bothify(text='????-########'),
            policy_expiration_date=faker.date_between(start_date='today', end_date='+1y'),
            license_plate=plate,
            vehicle_model=faker.word().capitalize(),
            vehicle_make=faker.company(),
        )

    return None



def find_discount_by_customer_id_and_payment_method(customer_id: str, payment_method) -> int:
    if payment_method.lower() == "tagz":
        return 15
    elif payment_method.lower() == "tagp":
        return 30
    else:
        return 0
