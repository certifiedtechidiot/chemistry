"""
========================================================================================
CLASS 11 PHYSICS HALF-YEARLY EXAM - END-TO-END CRASH PREPARATION CONTEXT
========================================================================================
Student: CertifiedTechIdiot
School: Navy Children School, Goa (NCS Goa)
Subject: Physics (042) - Class XI Half Yearly Examination
Date of Prep: September 27, 2026 (Exam Date: September 28, 2026)
Repository: https://github.com/certifiedtechidiot/chemistry

SYLLABUS (4 Units):
1. Unit 1: Units and Measurements (Units & Dimensions)
2. Unit 2: Motion in a Straight Line (1D Kinematics)
3. Unit 3: Motion in a Plane (Vectors, Projectiles, Circular Motion)
4. Unit 4: Laws of Motion (Newton's Laws, Friction, Banking, Impulse)
========================================================================================
"""

import math

METADATA = {
    "student": "CertifiedTechIdiot",
    "school": "Navy Children School, Goa",
    "exam": "Class 11 Physics Half-Yearly (042)",
    "date": "2026-09-27",
    "total_marks": 70,
    "passing_marks": 23,
    "target_score": "50+ to 60+ out of 70",
    "prep_window_hours": 15,
    "sleep_target": "3:00 AM to 7:30 AM (4.5 hours mandatory for memory consolidation)"
}

# ======================================================================================
# 1. TIMELINE & MILESTONES OF THE PREPARATION SESSION
# ======================================================================================

TIMELINE = [
    {
        "time": "11:48 AM",
        "event": "Initial Panic & Materials Ingestion",
        "details": (
            "Student had not prepared yet and exam was scheduled for next morning. "
            "Uploaded syllabus, Unit 1/2&3/4 teacher worksheets, and 2025-26 NCS Goa Half Yearly paper."
        )
    },
    {
        "time": "11:50 AM",
        "event": "Master Guide Generation & Additional PYQ Uploads",
        "details": (
            "Created comprehensive master guide artifact. Student uploaded 2 more full papers: "
            "Navy Children School Goa 2024-25 and 2023-24. Revealed a 60%+ verbatim recurrence pattern."
        )
    },
    {
        "time": "11:56 AM",
        "event": "Passing Feasibility Inquiry (35+ out of 70)",
        "details": (
            "Analyzed marking distribution: 3 derivations (15m) + 4 recurring questions (12m) + "
            "Case study graph reading (8m) + basic MCQs (8m) = 38-43 marks in just 2.5-3 hours."
        )
    },
    {
        "time": "11:58 AM",
        "event": "15-Hour Master Schedule Creation",
        "details": (
            "Student committed to studying until 3:00 AM (15 available hours). "
            "Target updated from survival (35+) to dominating (55-60+ marks) split into 5 structured blocks."
        )
    },
    {
        "time": "12:20 PM",
        "event": "Trajectory Equation Challenge ($y = 2x - 9x^2$)",
        "details": (
            "Compared $y = x\\tan\\theta - \\frac{g x^2}{2u^2\\cos^2\\theta}$ with $y = 2x - 9x^2$. "
            "Derived $\\tan\\theta = 2, \\cos^2\\theta = 1/5 \\implies u = \\sqrt{5g/18}$. "
            "With $g=10$, $u = 5/3\\text{ m/s}$; with $g=9.8$, $u = 7/(3\\sqrt{2})\\text{ m/s}$."
        )
    },
    {
        "time": "2:45 PM",
        "event": "Lecture Marathon Selection Strategy",
        "details": (
            "Compared Akshay Sir (PW, 4h, missing Laws of Motion) vs Next Toppers (5h 18m, all 4 units). "
            "Selected Next Toppers at 1.25x-1.5x speed with pen-and-paper active note taking."
        )
    },
    {
        "time": "3:01 PM",
        "event": "Calculus Differentiation Clarification",
        "details": (
            "Clarified $\\frac{d}{dt}(-4t) = -4$ using power rule $\\frac{d}{dt}(t^n) = n t^{n-1}$. "
            "For $x = 5t^2 - 4t + 5$, $v(t) = 10t - 4 \\implies v(2) = 16\\text{ m/s}$."
        )
    },
    {
        "time": "3:03 PM",
        "event": "Verification of Basic Differentiation in Papers",
        "details": (
            "Verified recurring appearance: 2025-26 Q4 ($x = -2t^2+4t$), 2024-25 Q12 ($x = at^2-bt^3$), "
            "2024-25 Q5 ($x = 3t^2+2t+6$), and Unit 4 Worksheet Q2 ($p = 3t^2+4t+5$)."
        )
    },
    {
        "time": "3:22 PM",
        "event": "Chapters 1, 2, 3 Passing Verification",
        "details": (
            "Proved Lessons 1, 2, 3 carry 50-55 marks out of 70. "
            "Recommended taking 15 minutes to learn 3 easy Lesson 4 items: Monkey on rope, lawn roller, recoil of gun."
        )
    },
    {
        "time": "3:26 PM",
        "event": "Speed Conversion Shortcut Rule",
        "details": (
            "$\\text{km/h} \\to \\text{m/s}$ multiply by $5/18$. $\\text{m/s} \\to \\text{km/h}$ multiply by $18/5$. "
            "Memorized standard exam numbers: 18->5, 36->10, 54->15, 72->20, 90->25, 720->200, 900->250."
        )
    },
    {
        "time": "3:29 PM",
        "event": "Average Marks Weightage Breakdown",
        "details": (
            "Lesson 1: 10-12m; Lesson 2: 18-20m; Lesson 3: 20-22m; Lesson 4: 16-18m."
        )
    },
    {
        "time": "3:42 PM",
        "event": "Galileo's Law of Odd Numbers",
        "details": (
            "For free fall from rest ($u=0$), distance in successive seconds is in ratio $1:3:5:7:9$. "
            "Direct application in 2023-24 Q24: distance in last second of a 6s round-trip is 25m."
        )
    },
    {
        "time": "4:11 PM",
        "event": "Comprehensive Lesson 2 Question Inventory",
        "details": (
            "Extracted all 1D kinematics questions from all papers into 6 distinct problem types."
        )
    },
    {
        "time": "5:06 PM",
        "event": "Types of Vectors Importance Filter",
        "details": (
            "Advised against memorizing 10 generic definitions. "
            "Focused solely on Position vs Displacement vectors (3 marks, asked in 2024 & 2023), "
            "Unit Vector, and Null Vector."
        )
    },
    {
        "time": "5:20 PM",
        "event": "Vector Algebra: $|A+B| = |A-B|$",
        "details": (
            "Square both sides: $A^2+B^2+2AB\\cos\\theta = A^2+B^2-2AB\\cos\\theta \\implies 4AB\\cos\\theta = 0 "
            "\\implies \\cos\\theta = 0 \\implies \\theta = 90^\\circ$."
        )
    },
    {
        "time": "5:24 PM - 5:36 PM",
        "event": "Vector Resolution & Rectangular Components",
        "details": (
            "Rectangular components are mutually perpendicular ($A_x = A\\cos\\theta, A_y = A\\sin\\theta$). "
            "Magnitude formula: $A = \\sqrt{A_x^2 + A_y^2}$. "
            "Found in ALL THREE years: 2025-26 Q5 (50N, 30N -> 40N); 2024-25 & 2023-24 Q28b (80km/h, 40km/h -> 40\\sqrt{3} km/h)."
        )
    },
    {
        "time": "5:45 PM",
        "event": "Only Studying Units + Lesson 2 Risk Evaluation",
        "details": (
            "Unit 1 + Unit 2 = ~30 to 33 marks. Passing with only those requires 75% accuracy (risky). "
            "Added 30-minute safety net: Projectile derivation (5m) + Centripetal accel (3m) = 40+ marks safely."
        )
    },
    {
        "time": "5:58 PM",
        "event": "Parallelogram Law of Vector Addition Derivation",
        "details": (
            "Full derivation: $R = \\sqrt{A^2 + B^2 + 2AB\\cos\\theta}$, $\\tan\\beta = \\frac{B\\sin\\theta}{A + B\\cos\\theta}$. "
            "Special cases: $\\theta = 0^\\circ (A+B), 180^\\circ (A-B), 90^\\circ (\\sqrt{A^2+B^2})$."
        )
    },
    {
        "time": "6:16 PM",
        "event": "Complementary Angles of Projectile ($\\\\theta$ and $90^\\circ - \\theta$)",
        "details": (
            "Proved $R_1 = R_2$ ($1:1$ ratio) and $H_1/H_2 = \\tan^2\\theta$. "
            "Direct match with 2025-26 Q31b, Worksheet Q11, 2024-25 Case Study 29."
        )
    },
    {
        "time": "6:24 PM",
        "event": "Bullet Max Height Numerical",
        "details": (
            "Bullet at $280\\text{ m/s}$ at $30^\\circ$: $H = \\frac{280^2 \\times (1/4)}{2 \\times 9.8} = 1000\\text{ m}$."
        )
    },
    {
        "time": "6:51 PM",
        "event": "Epiphany & 3-Step CBSE Marking Rule",
        "details": (
            "Student realized questions are direct formula substitutions, not Olympiad traps. "
            "Standardized 3-step format: (1) Given values (0.5m), (2) Boxed formula (1m), (3) Calculation + Units."
        )
    },
    {
        "time": "7:33 PM",
        "event": "Equation of Trajectory Derivation & Parabola Proof",
        "details": (
            "$x = (u\\cos\\theta)t \\implies t = x/(u\\cos\\theta)$. "
            "$y = (u\\sin\\theta)t - \\frac{1}{2}gt^2 \\implies y = x\\tan\\theta - \\frac{gx^2}{2u^2\\cos^2\\theta}$. "
            "Quadratic in $x$ proves path is a parabola. Shortcut form: $y = x\\tan\\theta(1 - x/R)$."
        )
    },
    {
        "time": "8:43 PM",
        "event": "Centripetal Acceleration Derivation",
        "details": (
            "Derivation by similar triangles: $|\\Delta v|/v = |\\Delta r|/r \\implies a_c = v^2/r = r\\omega^2$. "
            "Direction: Radially inward towards center. "
            "School problem: $r = 80\\text{ cm}, 14\\text{ rev in } 25\\text{ s} \\implies a_c = 9.9\\text{ m/s}^2$."
        )
    },
    {
        "time": "8:51 PM",
        "event": "Milestone & Night Strategy Finalization",
        "details": (
            "Lessons 2 and 3 completed! Night plan: "
            "Till 10:00 PM: Lesson 2 & 3 numericals. "
            "10:10 to 11:30 PM: Units & Dimensions + numericals. "
            "12:00 to 2:00 AM: Lesson 4 (Laws of motion). "
            "2:00 to 3:00 AM: Numericals & formula check. Sleep at 3:00 AM."
        )
    }
]

# ======================================================================================
# 2. THE 7 RECURRING GUARANTEED QUESTIONS (NCS GOA 3-YEAR PATTERN)
# ======================================================================================

RECURRING_QUESTIONS = {
    "1. Monkey Climbing Rope": {
        "parameters": "Mass m = 40 kg, Max breaking tension T_max = 600 N, g = 10 m/s^2",
        "cases": [
            {"condition": "Climbs up with a = 6 m/s^2", "formula": "T = m(g + a)", "calculation": "40(10 + 6) = 640 N", "verdict": "BREAKS (640 N > 600 N)"},
            {"condition": "Climbs down with a = 4 m/s^2", "formula": "T = m(g - a)", "calculation": "40(10 - 4) = 240 N", "verdict": "SAFE (240 N < 600 N)"},
            {"condition": "Climbs up with constant speed 5 m/s", "formula": "T = mg", "calculation": "40(10) = 400 N", "verdict": "SAFE (400 N < 600 N)"}
        ]
    },
    "2. Stone Whirled in Horizontal Circle": {
        "parameters": "Radius r = 80 cm = 0.8 m, 14 revolutions in 25 seconds",
        "step_1": "Frequency f = 14 / 25 = 0.56 Hz",
        "step_2": "Angular velocity omega = 2 * pi * f = 2 * (22/7) * (14/25) = 88/25 = 3.52 rad/s",
        "step_3": "Centripetal acceleration a_c = omega^2 * r = (3.52)^2 * 0.8 = 9.91 m/s^2",
        "direction": "Radially inward, towards the centre of the circular path"
    },
    "3. Bullet 3 km at 30 deg - Target 5 km": {
        "parameters": "R = 3000 m at theta = 30 deg",
        "calculation": "R = u^2 * sin(60 deg) / g = 3000 => u^2 / g = 3000 / (sqrt(3)/2) = 3464 m = 3.464 km",
        "max_range": "R_max = u^2 / g = 3.464 km (at theta = 45 deg)",
        "verdict": "NO, cannot hit 5 km target since 3.464 km < 5 km regardless of angle adjustment"
    },
    "4. Pendulum in Freely Falling Lift": {
        "formula": "T = 2 * pi * sqrt(l / g_eff)",
        "g_eff": "g_eff = g - g = 0",
        "answer": "T = 2 * pi * sqrt(l / 0) = INFINITE (Pendulum does not oscillate)"
    },
    "5. Angle with the VERTICAL Trap": {
        "trick": "If projected at 30 deg with the VERTICAL, angle with HORIZONTAL is theta = 90 - 30 = 60 deg!",
        "rule": "Always substitute theta = 60 deg into T, H, R projectile formulas"
    },
    "6. Angle where Range = 4 * Max Height": {
        "identity": "H / R = tan(theta) / 4",
        "application": "If R = 50 m and H = 10 m => 10 / 50 = tan(theta) / 4 => tan(theta) = 0.8 => theta = tan^-1(0.8) approx 38.7 deg"
    },
    "7. Hexagonal Path Cyclist": {
        "parameters": "Turn 60 deg after every 100 m",
        "analysis": "6 turns form a closed regular hexagon (displacement = 0 at 6th turn). At 7th turn, cyclist is at the end of the 7th side of 100 m.",
        "displacement": "100 m"
    }
}

# ======================================================================================
# 3. CORE DERIVATIONS MASTER REFERENCE
# ======================================================================================

DERIVATIONS = {
    "Projectile Motion": {
        "trajectory": {
            "x_eq": "x = (u * cos(theta)) * t => t = x / (u * cos(theta))",
            "y_eq": "y = (u * sin(theta)) * t - 0.5 * g * t^2",
            "final": "y = x * tan(theta) - (g * x^2) / (2 * u^2 * cos^2(theta))",
            "nature": "Quadratic in x (form y = Ax - Bx^2) => Path is a PARABOLA"
        },
        "time_of_flight": "T = (2 * u * sin(theta)) / g",
        "maximum_height": "H = (u^2 * sin^2(theta)) / (2 * g)",
        "horizontal_range": "R = (u^2 * sin(2 * theta)) / g (Max at theta = 45 deg, R_max = u^2 / g)",
        "complementary_angles": "R(90 - theta) = u^2 * sin(180 - 2*theta) / g = u^2 * sin(2*theta) / g = R(theta)"
    },
    "Centripetal Acceleration": {
        "statement": "Acceleration directed radially inwards towards centre in uniform circular motion",
        "proof": "Similar triangles: |Delta v| / v = |Delta r| / r => |Delta v| = (v/r) * |Delta r|; divide by Delta t => a_c = v^2 / r = r * omega^2",
        "direction": "Radially inward towards centre"
    },
    "Banking of Roads": {
        "purpose": "Provides necessary centripetal force using normal reaction component to avoid reliance on friction",
        "vertical_eq": "N * cos(theta) = mg + f * sin(theta) = mg + mu * N * sin(theta)",
        "horizontal_eq": "N * sin(theta) + f * cos(theta) = m * v^2 / r",
        "final_formula": "v_max = sqrt(r * g * (mu + tan(theta)) / (1 - mu * tan(theta)))",
        "optimum_speed": "v_0 = sqrt(r * g * tan(theta)) (when mu = 0)"
    },
    "Calculus Equations of Motion": {
        "v_eq": "a = dv/dt => int(dv, u, v) = a * int(dt, 0, t) => v = u + at",
        "s_eq": "v = ds/dt => ds = (u + at)dt => int(ds, 0, s) = int((u + at)dt, 0, t) => s = ut + 0.5 * a * t^2",
        "area_vt": "s = int(v dt) => Area under velocity-time graph represents displacement"
    },
    "Parallelogram Law": {
        "magnitude": "R = sqrt(A^2 + B^2 + 2 * A * B * cos(theta))",
        "direction": "tan(beta) = (B * sin(theta)) / (A + B * cos(theta))"
    },
    "Recoil of Gun": {
        "principle": "Law of Conservation of Linear Momentum",
        "formula": "P_initial = 0 => M * V_gun + m * v_bullet = 0 => V_gun = - (m / M) * v_bullet"
    }
}

# ======================================================================================
# 4. HELPER SOLVER FUNCTIONS
# ======================================================================================

def calculate_projectile(u: float, theta_deg: float, g: float = 9.8) -> dict:
    """Calculate Time of Flight, Max Height, and Range for a projectile."""
    rad = math.radians(theta_deg)
    t_flight = (2 * u * math.sin(rad)) / g
    h_max = (u**2 * (math.sin(rad))**2) / (2 * g)
    r_range = (u**2 * math.sin(2 * rad)) / g
    return {
        "time_of_flight_s": round(t_flight, 2),
        "max_height_m": round(h_max, 2),
        "range_m": round(r_range, 2)
    }

def calculate_centripetal(r_m: float, revs: int, time_s: float) -> dict:
    """Calculate frequency, angular velocity, and centripetal acceleration."""
    freq = revs / time_s
    omega = 2 * math.pi * freq
    a_c = (omega**2) * r_m
    return {
        "frequency_hz": round(freq, 3),
        "omega_rad_s": round(omega, 3),
        "a_c_m_s2": round(a_c, 2)
    }

def calculate_stopping_distance(u_kmh: float, a_retard: float) -> float:
    """Calculate stopping distance given speed in km/h and retardation in m/s^2."""
    u_ms = u_kmh * (5 / 18)
    s = (u_ms**2) / (2 * a_retard)
    return round(s, 2)

def calculate_rectangular_component(total: float, known_component: float) -> float:
    """Find missing perpendicular component using Pythagoras theorem."""
    return round(math.sqrt(total**2 - known_component**2), 2)

def calculate_lift_tension(m: float, a: float, mode: str, g: float = 9.8) -> float:
    """
    Calculate apparent weight / cable tension in a lift:
    mode: 'up_accel', 'down_accel', 'free_fall', 'uniform_velocity'
    """
    if mode == "up_accel":
        return round(m * (g + a), 2)
    elif mode == "down_accel":
        return round(m * (g - a), 2)
    elif mode == "free_fall":
        return 0.0
    elif mode == "uniform_velocity":
        return round(m * g, 2)
    else:
        raise ValueError("Unknown mode")

# ======================================================================================
# 5. VERIFICATION TESTS ON IMPORT OR RUN
# ======================================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("CLASS 11 PHYSICS HALF-YEARLY MASTER VERIFICATION SUITE")
    print("=" * 70)
    
    # Test 1: Projectile Problem from Paper (u = 28 m/s, theta = 30 deg)
    p = calculate_projectile(28, 30, g=9.8)
    print(f"Cricket Ball (28 m/s @ 30 deg): H = {p['max_height_m']}m, T = {p['time_of_flight_s']}s, R = {p['range_m']}m")
    assert abs(p['max_height_m'] - 10.0) < 0.2
    
    # Test 2: Stone in Circle (r = 0.8 m, 14 rev in 25 s)
    c = calculate_centripetal(0.8, 14, 25)
    print(f"Stone in Circle (0.8m, 14rev/25s): a_c = {c['a_c_m_s2']} m/s^2")
    assert abs(c['a_c_m_s2'] - 9.91) < 0.2
    
    # Test 3: Rectangular Components (Total 50 N, x = 30 N => y = 40 N)
    y_comp = calculate_rectangular_component(50, 30)
    print(f"Force Rectangular Component (50N, 30N): y = {y_comp} N")
    assert y_comp == 40.0
    
    # Test 4: Monkey on Rope (m = 40 kg, a = 6 m/s^2 up => T = 640 N)
    t_monkey_up = calculate_lift_tension(40, 6, "up_accel", g=10.0)
    print(f"Monkey Climbing Up (a=6, g=10): Tension = {t_monkey_up} N (Breaks 600N limit!)")
    assert t_monkey_up == 640.0

    print("=" * 70)
    print("ALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    print("=" * 70)
