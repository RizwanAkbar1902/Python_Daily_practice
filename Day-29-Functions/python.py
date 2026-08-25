"""
Project: Bill Generator
Day: 29
Author: Rizwan Akbar

Description:
A simple Python bill generator that calculates discounts, taxes,
and the final bill amount using reusable functions.

Concepts Practiced:
- Functions
- Parameters and Arguments
- Return Values
- Default Parameters
- Function Composition
- String Formatting
- User Input
"""


def calculate_discount(price, discount_percent):
    """Calculate and return the discount amount."""
    return (price * discount_percent) / 100


def calculate_tax(amount, tax_rate=5):
    """Calculate and return tax using a default rate of 5%."""
    return (amount * tax_rate) / 100


def calculate_bill(price, discount_percent, tax_rate=5):
    """Calculate discount, discounted price, tax, and final total."""

    discount = calculate_discount(price, discount_percent)
    discounted_price = price - discount
    tax = calculate_tax(discounted_price, tax_rate)
    final_total = discounted_price + tax

    return discount, discounted_price, tax, final_total


def display_bill(
    item_name,
    price,
    discount_percent,
    discount,
    discounted_price,
    tax_rate,
    tax,
    final_total
):
    """Display the final bill in a clean receipt format."""

    print("\n" + "=" * 40)
    print("           🧾 INVOICE RECEIPT")
    print("=" * 40)

    print(f"Item Name       : {item_name}")
    print(f"Original Price  : Rs. {price:.2f}")
    print(f"Discount ({discount_percent:.1f}%) : -Rs. {discount:.2f}")
    print(f"Price After Off : Rs. {discounted_price:.2f}")
    print(f"Tax ({tax_rate:.1f}%)        : +Rs. {tax:.2f}")

    print("-" * 40)
    print(f"Final Total     : Rs. {final_total:.2f}")

    print("=" * 40)
    print("        🙏 Thank you for your purchase!")
    print("=" * 40)


def main():
    """Collect user input and generate the final bill."""

    print("\n" + "=" * 40)
    print("        💰 BILL GENERATOR")
    print("=" * 40)

    item_name = input("Enter item name: ").strip().title()

    try:
        price = float(input("Enter item price: "))
        discount_percent = float(
            input("Enter discount percentage: ")
        )

        if price <= 0:
            print("⚠️ Price must be greater than zero.")
            return

        if not 0 <= discount_percent <= 100:
            print("⚠️ Discount must be between 0 and 100%.")
            return

    except ValueError:
        print("⚠️ Invalid input! Please enter numeric values.")
        return

    discount, discounted_price, tax, final_total = calculate_bill(
        price,
        discount_percent
    )

    display_bill(
        item_name,
        price,
        discount_percent,
        discount,
        discounted_price,
        5,
        tax,
        final_total
    )


if __name__ == "__main__":
    main()