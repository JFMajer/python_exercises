class HourOutOfBound(Exception): pass


provinces_tax_rate = {
    "Chico": 50,
    "Groucho": 70,
    "Harpo": 50,
    "Zeppo": 40
}


def calculate_tax(amount: float, province: str, time_of_purchase: int) -> float:
    if time_of_purchase < 0 or time_of_purchase > 24:
        raise HourOutOfBound("Please provide an integer between 0 and 24.")
    if amount <= 0:
        raise ValueError("Purchase price needs to be more than zero.")
    if province.strip() not in provinces_tax_rate.keys():
        raise ValueError(f"Province not found, please use one of {', '.join(provinces_tax_rate.keys())}")

    final_amount = amount + (amount * (provinces_tax_rate[province] / 100) * (time_of_purchase / 24))
    return round(final_amount, 3)