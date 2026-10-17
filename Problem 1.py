def main():
    # Get loan information
    P0 = float(input("Enter the amount to finance: $"))
    r = float(input("Enter the annual interest rate (e.g., 0.02 for 2%): "))
    k = int(input("Enter the number of compounding periods per year: "))
    N = int(input("Enter the number of years: "))

    # Calculate the periodic interest rate and number of payments
    rate = r / k
    periods = N * k

    # Calculate the periodic payment
    if rate == 0:
        payment = P0 / periods
    else:
        payment = P0 * rate / (1 - (1 + rate) ** (-periods))

    # Print loan summary
    print("\nAMORTIZATION SCHEDULE")
    print("-" * 83)
    print(f"Loan Amount: ${P0:,.2f}")
    print(f"Annual Interest Rate: {r:.2%}")
    print(f"Payment per Period: ${payment:,.2f}")
    print(f"Loan Term: {N} years")
    print("-" * 83)

    # Print column headings
    print(f"{'Payment #':>10} {'Payment':>13} {'Interest':>13} "
          f"{'Principal':>13} {'Balance':>15}")
    print("-" * 83)

    balance = P0

    # Generate the amortization schedule
    for period in range(1, periods + 1):
        interest = balance * rate
        principal = payment - interest
        balance -= principal

        # Avoid a tiny negative balance caused by floating-point rounding
        if period == periods or abs(balance) < 0.005:
            balance = 0.0

        print(f"{period:>10} "
              f"${payment:>12,.2f} "
              f"${interest:>12,.2f} "
              f"${principal:>12,.2f} "
              f"${balance:>14,.2f}")

    print("-" * 83)


if __name__ == "__main__":
    main()