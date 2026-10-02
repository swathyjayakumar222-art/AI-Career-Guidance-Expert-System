from inference_engine import (
    forward_chain,
    perform_forward_chaining
)


# ==========================================
# SAMPLE STUDENT PROFILE
# ==========================================

user_facts = {

    "education": "undergraduate",

    "programming": "advanced",

    "mathematics": "high",

    "problem_solving": "high",

    "technology": "high",

    "data_interest": "high",

    "creativity": "medium",

    "security_interest": "low",

    "work_style": "technical",

    "teamwork": "both",

    "activity": "software",

    "career_priority": "technology"
}


# ==========================================
# RUN FORWARD CHAINING
# ==========================================

derived_facts = perform_forward_chaining(
    user_facts
)


print("\n==============================")
print("   DERIVED FACTS")
print("==============================\n")


for fact in sorted(derived_facts):

    print("✓", fact)


# ==========================================
# RUN CAREER RECOMMENDATIONS
# ==========================================

recommendations = forward_chain(
    user_facts
)


print("\n==============================")
print("   CAREER RECOMMENDATIONS")
print("==============================\n")


for recommendation in recommendations:

    print(
        recommendation["career"],
        "→",
        recommendation["match"],
        "%"
    )

    print(
        recommendation["reason"]
    )

    print()