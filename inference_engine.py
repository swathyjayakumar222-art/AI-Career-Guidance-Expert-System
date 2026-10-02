from knowledge_base import (
    INFERENCE_RULES,
    CAREER_RULES,
    CAREER_ROADMAPS
)


# ==========================================
# CHECK WHETHER A CONDITION IS TRUE
# ==========================================

def condition_matches(
    condition,
    user_facts,
    derived_facts
):

    # Normal user-answer condition
    if "fact" in condition:

        fact_name = condition["fact"]

        accepted_values = condition["values"]

        user_value = user_facts.get(fact_name)

        return user_value in accepted_values


    # Derived fact condition
    if "derived" in condition:

        derived_fact = condition["derived"]

        return derived_fact in derived_facts


    return False


# ==========================================
# FORWARD CHAINING
# ==========================================

def perform_forward_chaining(user_facts):

    derived_facts = set()

    changed = True

    while changed:

        changed = False

        for rule in INFERENCE_RULES:

            conditions = rule["conditions"]

            rule_is_true = all(
                condition_matches(
                    condition,
                    user_facts,
                    derived_facts
                )
                for condition in conditions
            )

            if rule_is_true:

                new_fact = rule["conclusion"]

                if new_fact not in derived_facts:

                    derived_facts.add(new_fact)

                    changed = True


    return derived_facts


# ==========================================
# CREATE HUMAN-READABLE REASONING TRACE
# ==========================================

def generate_reasoning_trace(
    user_facts,
    derived_facts
):

    trace = []


    # ==========================================
    # EDUCATION
    # ==========================================

    education = user_facts.get("education")

    education_names = {

        "school_9_10":
            "School student (Class 9–10)",

        "school_11_12":
            "Higher-secondary student (Class 11–12)",

        "undergraduate":
            "Undergraduate student",

        "postgraduate":
            "Postgraduate student"
    }


    if education in education_names:

        trace.append(
            "Education level identified as: "
            + education_names[education]
        )


    # ==========================================
    # DERIVED FACT EXPLANATIONS
    # ==========================================

    derived_explanations = {

        "strong_technical_profile":
            "Programming and problem-solving answers indicate a strong technical profile.",

        "strong_analytical_profile":
            "Mathematics and problem-solving answers indicate a strong analytical profile.",

        "data_oriented":
            "Mathematics and data-interest answers indicate a data-oriented profile.",

        "security_oriented":
            "Cybersecurity and technology interests indicate a security-oriented profile.",

        "creative_profile":
            "Creativity and preferred work style indicate a creative profile.",

        "collaborative_leader":
            "Teamwork and leadership preferences indicate a collaborative leadership profile.",

        "software_oriented":
            "Your preferred activity and technology interest indicate a software-oriented profile.",

        "ai_oriented":
            "Your preferred activity and programming ability indicate an AI-oriented profile.",

        "research_oriented":
            "Your career priority and problem-solving preference indicate a research-oriented profile.",

        "technology_focused":
            "Your technology interest and career priority indicate a technology-focused profile.",

        "strong_software_candidate":
            "The technical and software rules together indicate a strong software candidate.",

        "strong_data_candidate":
            "The analytical and data rules together indicate a strong data candidate.",

        "strong_ai_candidate":
            "The technical and AI rules together indicate a strong AI candidate.",

        "strong_security_candidate":
            "The technical and security rules together indicate a strong cybersecurity candidate."
    }


    # Keep the reasoning in a logical order
    reasoning_order = [

        "strong_technical_profile",

        "strong_analytical_profile",

        "data_oriented",

        "security_oriented",

        "creative_profile",

        "collaborative_leader",

        "software_oriented",

        "ai_oriented",

        "research_oriented",

        "technology_focused",

        "strong_software_candidate",

        "strong_data_candidate",

        "strong_ai_candidate",

        "strong_security_candidate"
    ]


    for fact in reasoning_order:

        if fact in derived_facts:

            if fact in derived_explanations:

                trace.append(
                    derived_explanations[fact]
                )


    return trace


# ==========================================
# GENERATE CAREER REASONS
# ==========================================

def generate_reasons(
    user_facts,
    derived_facts,
    conditions
):

    reasons = []


    for condition in conditions:

        # ======================================
        # USER ANSWER CONDITION
        # ======================================

        if "fact" in condition:

            fact_name = condition["fact"]

            accepted_values = condition["values"]

            user_value = user_facts.get(fact_name)


            if user_value in accepted_values:

                reason_map = {

                    "education":
                        "Your education level was considered in the analysis.",

                    "programming":
                        "You have programming experience.",

                    "mathematics":
                        "You are comfortable with mathematics.",

                    "problem_solving":
                        "You show an interest in problem solving.",

                    "technology":
                        "You have a strong interest in technology.",

                    "data_interest":
                        "You are interested in working with data.",

                    "creativity":
                        "You show creative interests.",

                    "security_interest":
                        "You are interested in cybersecurity.",

                    "work_style":
                        "Your preferred work style fits this career.",

                    "teamwork":
                        "Your teamwork preference fits this career.",

                    "activity":
                        "Your preferred activities match this career.",

                    "career_priority":
                        "Your career priorities align with this path."
                }


                if fact_name in reason_map:

                    reasons.append(
                        reason_map[fact_name]
                    )


        # ======================================
        # DERIVED CONDITION
        # ======================================

        elif "derived" in condition:

            derived_fact = condition["derived"]


            derived_reason_map = {

                "strong_technical_profile":
                    "Your answers indicate a strong technical profile.",

                "strong_analytical_profile":
                    "Your answers indicate strong analytical ability.",

                "data_oriented":
                    "Your profile shows a strong orientation toward data.",

                "security_oriented":
                    "Your profile shows a strong security orientation.",

                "creative_profile":
                    "Your answers indicate a creative profile.",

                "collaborative_leader":
                    "Your teamwork and leadership preferences indicate a collaborative leadership profile.",

                "software_oriented":
                    "Your interests indicate a strong software orientation.",

                "ai_oriented":
                    "Your interests indicate an orientation toward AI and intelligent systems.",

                "research_oriented":
                    "Your interests indicate a research-oriented profile.",

                "technology_focused":
                    "Technology is an important part of your career preferences.",

                "strong_software_candidate":
                    "Multiple technical and software-related rules support this career.",

                "strong_data_candidate":
                    "Multiple analytical and data-related rules support this career.",

                "strong_ai_candidate":
                    "Multiple programming, analytical and AI-related rules support this career.",

                "strong_security_candidate":
                    "Multiple technical and security-related rules support this career."
            }


            if derived_fact in derived_facts:

                if derived_fact in derived_reason_map:

                    reasons.append(
                        derived_reason_map[derived_fact]
                    )


    # Remove duplicates

    unique_reasons = []

    for reason in reasons:

        if reason not in unique_reasons:

            unique_reasons.append(reason)


    return unique_reasons[:4]


# ==========================================
# CALCULATE CAREER MATCH
# ==========================================

def calculate_match(
    user_facts,
    derived_facts,
    conditions
):

    score = 0

    total_weight = 0


    for condition in conditions:

        weight = condition["weight"]

        total_weight += weight


        if condition_matches(
            condition,
            user_facts,
            derived_facts
        ):

            score += weight


    if total_weight == 0:

        return 0


    final_score = (
        score / total_weight
    ) * 100


    return round(final_score)


# ==========================================
# ANALYZE COMPLETE USER PROFILE
# ==========================================

def analyze_profile(user_facts):

    # ------------------------------------------
    # STEP 1: FORWARD CHAINING
    # ------------------------------------------

    derived_facts = perform_forward_chaining(
        user_facts
    )


    # ------------------------------------------
    # STEP 2: GENERATE REASONING TRACE
    # ------------------------------------------

    reasoning_trace = generate_reasoning_trace(
        user_facts,
        derived_facts
    )


    # ------------------------------------------
    # STEP 3: EVALUATE CAREERS
    # ------------------------------------------

    recommendations = []


    for career_rule in CAREER_RULES:

        score = calculate_match(
            user_facts,
            derived_facts,
            career_rule["conditions"]
        )


        reasons = generate_reasons(
            user_facts,
            derived_facts,
            career_rule["conditions"]
        )


        roadmap = CAREER_ROADMAPS.get(
            career_rule["career"],
            {}
        )


        if score >= 20:

            recommendations.append({

                "career":
                    career_rule["career"],

                "match":
                    score,

                "reason":
                    career_rule["reason"],

                "reasons":
                    reasons,

                "roadmap":
                    roadmap

            })


    # ------------------------------------------
    # STEP 4: SORT RESULTS
    # ------------------------------------------

    recommendations.sort(
        key=lambda x: x["match"],
        reverse=True
    )


    return {

        "recommendations":
            recommendations[:3],

        "derived_facts":
            derived_facts,

        "reasoning_trace":
            reasoning_trace
    }


# ==========================================
# MAIN AI FUNCTION
# ==========================================

def forward_chain(user_facts):

    analysis = analyze_profile(
        user_facts
    )


    return analysis["recommendations"]