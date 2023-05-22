import textwrap
from dialer.domain import Switch


def add_operator_pricings(switch: Switch, name: str, raw_pricing: str):
    lines = raw_pricing.strip().splitlines()
    for line in lines:
        prefix, price_str = line.split()
        price = float(price_str)
        switch.add_pricing(name, prefix, price)


def main():
    switch = Switch()
    add_operator_pricings(
        switch,
        "Operator A",
        textwrap.dedent(
            """
            1	 0.9
            268	 5.1
            46	 0.17
            4620	 0.0
            468	 0.15
            4631	 0.15
            4673	 0.9
            46732	 1.1
            """
        ),
    )
    add_operator_pricings(
        switch,
        "Operator B",
        textwrap.dedent(
            """
            1	 0.92
            44	 0.5
            46	 0.2
            467	 1.0
            48	 1.2
            """
        ),
    )

    phone_numbers = [
        "68123456789",
        "46231423333",
        "46731423333",
        "46732423333",
        "48231423333",
    ]

    for phone_number in phone_numbers:
        result = switch.route(phone_number)
        if not result:
            print(f"No operator supports number {phone_number}")
            continue
        operator, price = result
        print(f"Routing to {phone_number} using operator {operator} at ${price}/min")
