print("=== FIXED CREDIT CGPA SYSTEM ===")
dept = input("Enter Department (CSE/EEE/ME/BBA/ENGLISH): ").strip().upper()

total_qp = 0.0
total_cr = 0.0
credit = 3.0

# ---------------- CSE ----------------
if dept == "CSE":
    print("\nDepartment: CSE")

    # 1) Structured Programming
    print("\nStructured Programming")
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

    # 2) Discrete Mathematics
    print("\nDiscrete Mathematics")
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

    # 3) Data Structures
    print("\nData Structures")
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

    # 4) Digital Logic Design
    print("\nDigital Logic Design")
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

    # 5) Computer Organization
    print("\nComputer Organization")
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

    # 6) Database Systems
    print("\nDatabase Systems")
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

# ---------------- EEE ----------------
elif dept == "EEE":
    print("\nDepartment: EEE")

    # 1) Circuit Theory
    print("\nCircuit Theory")
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

    # 2) Electrical Machines
    print("\nElectrical Machines")
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

    # 3) Electronics I
    print("\nElectronics I")
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

    # 4) Signals & Systems
    print("\nSignals & Systems")
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

    # 5) Power Systems I
    print("\nPower Systems I")
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

    # 6) Control Systems
    print("\nControl Systems")
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

    # 1) Engineering Mechanics
    print("\nEngineering Mechanics")
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

    # 2) Strength of Materials
    print("\nStrength of Materials")
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

    # 3) Thermodynamics
    print("\nThermodynamics")
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

    # 4) Fluid Mechanics
    print("\nFluid Mechanics")
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

    # 5) Heat Transfer
    print("\nHeat Transfer")
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

    # 6) Machine Design
    print("\nMachine Design")
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

    # 1) Principles of Management
    print("\nPrinciples of Management")
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

    # 2) Financial Accounting
    print("\nFinancial Accounting")
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

    # 3) Business Economics
    print("\nBusiness Economics")
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

    # 4) Marketing Management
    print("\nMarketing Management")
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

    # 5) Human Resource Management
    print("\nHuman Resource Management")
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

    # 6) Business Statistics
    print("\nBusiness Statistics")
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

    # 1) History of English Literature
    print("\nHistory of English Literature")
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

    # 2) Poetry
    print("\nPoetry")
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

    # 3) Drama
    print("\nDrama")
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

    # 4) Novel
    print("\nNovel")
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

    # 5) Linguistics
    print("\nLinguistics")
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

    # 6) Literary Theory
    print("\nLiterary Theory")
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
    print("Invalid department! Please enter: CSE/EEE/ME/BBA/ENGLISH")

# ---------- FINAL RESULT ----------
if total_cr > 0:
    cgpa = total_qp / total_cr
    print("\n--- FIXED CREDIT RESULT ---")
    print("Total Credits:", total_cr)
    print("Total Quality Points:", total_qp)
    print("Estimated CGPA:", round(cgpa, 2))
else:
    print("\nCGPA cannot be calculated.")
