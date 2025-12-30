print("******Open Credit CGPA System******")
dept = input("Enter Department (CSE/EEE/ME/BBA/ENGLISH): ").strip().upper()

total_qp = 0.0
total_cr = 0.0

# ---------------- CSE ----------------

if dept == "CSE":
    print("\nDepartment: CSE")
    credit = 3.0

    #course 1
    take = input("Take Structured Programming? (y/n): ").strip().lower()

    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("mid (0-30): "))
        final = float(input("final (0-50): "))
        total = ct + mid + final

        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        qp = gp * credit
        total_qp += qp
        total_cr += credit
        print("Total: ", total, "GP: ", gp)

     # Course 2
    take = input("Take Discrete Mathematics? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final

        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00

        qp = gp * credit
        total_qp += qp
        total_cr += credit
        print("Total:", total, "GP:", gp)


    # Course 3
    take = input("Take Data Structures? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final

        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00

        qp = gp * credit
        total_qp += qp
        total_cr += credit
        print("Total:", total, "GP:", gp)

    # Course 4
    take = input("Take Digital Logic Design? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final

        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00

        qp = gp * credit
        total_qp += qp
        total_cr += credit
        print("Total:", total, "GP:", gp)

    # Course 5
    take = input("Take Database Systems? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final

        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00

        qp = gp * credit
        total_qp += qp
        total_cr += credit
        print("Total:", total, "GP:", gp)
# ---------------- EEE ----------------
elif dept == "EEE":
    print("\nDepartment: EEE")
    credit = 3.0

    take = input("Take Circuit Theory? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Electrical Machines? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Electronics I? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Power Systems I? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Control Systems? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

# ---------------- ME ----------------
elif dept == "ME":
    print("\nDepartment: ME")
    credit = 3.0

    take = input("Take Thermodynamics? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Fluid Mechanics? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Heat Transfer? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Strength of Materials? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Machine Design? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

# ---------------- BBA ----------------
elif dept == "BBA":
    print("\nDepartment: BBA")
    credit = 3.0

    take = input("Take Principles of Management? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Financial Accounting? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Marketing Management? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take HRM? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Business Statistics? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

# ---------------- ENGLISH ----------------
elif dept == "ENGLISH":
    print("\nDepartment: ENGLISH")
    credit = 3.0

    take = input("Take Poetry? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Drama? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Novel? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Linguistics? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

    take = input("Take Literary Theory? (y/n): ").strip().lower()
    if take == "y":
        ct = float(input("CT (0-20): "))
        mid = float(input("Mid (0-30): "))
        final = float(input("Final (0-50): "))
        total = ct + mid + final
        if total >= 80: gp = 4.00
        elif total >= 75: gp = 3.75
        elif total >= 70: gp = 3.50
        elif total >= 65: gp = 3.25
        elif total >= 60: gp = 3.00
        elif total >= 55: gp = 2.75
        elif total >= 50: gp = 2.50
        elif total >= 45: gp = 2.25
        elif total >= 40: gp = 2.00
        else: gp = 0.00
        total_qp += gp * credit
        total_cr += credit

else:
    print("Invalid department!")

# Final Result
if total_cr > 0:
    cgpa = total_qp / total_cr
    print("\n--- OPEN CREDIT RESULT ---")
    print("Total Credits Taken:", total_cr)
    print("Estimated CGPA:", round(cgpa, 2))
else:
    print("\nNo credit counted, CGPA cannot be calculated.")