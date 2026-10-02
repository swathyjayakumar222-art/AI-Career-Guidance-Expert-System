# ==========================================
# KNOWLEDGE BASE
# ==========================================


# ==========================================
# FORWARD-CHAINING INFERENCE RULES
# ==========================================

INFERENCE_RULES = [

    # --------------------------------------
    # STRONG TECHNICAL PROFILE
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "programming",
                "values": ["advanced", "intermediate"]
            },
            {
                "fact": "problem_solving",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "strong_technical_profile"
    },


    # --------------------------------------
    # STRONG ANALYTICAL PROFILE
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "mathematics",
                "values": ["high"]
            },
            {
                "fact": "problem_solving",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "strong_analytical_profile"
    },


    # --------------------------------------
    # DATA ORIENTED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "mathematics",
                "values": ["high", "medium"]
            },
            {
                "fact": "data_interest",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "data_oriented"
    },


    # --------------------------------------
    # SECURITY ORIENTED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "security_interest",
                "values": ["high", "medium"]
            },
            {
                "fact": "technology",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "security_oriented"
    },


    # --------------------------------------
    # CREATIVE PROFILE
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "creativity",
                "values": ["high", "medium"]
            },
            {
                "fact": "work_style",
                "values": ["creative"]
            }
        ],
        "conclusion": "creative_profile"
    },


    # --------------------------------------
    # COLLABORATIVE LEADER
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "work_style",
                "values": ["leadership", "people"]
            },
            {
                "fact": "teamwork",
                "values": ["team", "both"]
            }
        ],
        "conclusion": "collaborative_leader"
    },


    # --------------------------------------
    # SOFTWARE ORIENTED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "activity",
                "values": ["software"]
            },
            {
                "fact": "technology",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "software_oriented"
    },


    # --------------------------------------
    # AI ORIENTED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "activity",
                "values": ["ai"]
            },
            {
                "fact": "programming",
                "values": ["advanced", "intermediate"]
            }
        ],
        "conclusion": "ai_oriented"
    },


    # --------------------------------------
    # RESEARCH ORIENTED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "career_priority",
                "values": ["research"]
            },
            {
                "fact": "problem_solving",
                "values": ["high", "medium"]
            }
        ],
        "conclusion": "research_oriented"
    },


    # --------------------------------------
    # TECHNOLOGY FOCUSED
    # --------------------------------------

    {
        "conditions": [
            {
                "fact": "technology",
                "values": ["high"]
            },
            {
                "fact": "career_priority",
                "values": ["technology"]
            }
        ],
        "conclusion": "technology_focused"
    },


    # ======================================
    # SECOND-LEVEL RULES
    # ======================================

    # Strong technical + software
    {
        "conditions": [
            {
                "derived": "strong_technical_profile"
            },
            {
                "derived": "software_oriented"
            }
        ],
        "conclusion": "strong_software_candidate"
    },


    # Strong analytical + data
    {
        "conditions": [
            {
                "derived": "strong_analytical_profile"
            },
            {
                "derived": "data_oriented"
            }
        ],
        "conclusion": "strong_data_candidate"
    },


    # Technical + AI
    {
        "conditions": [
            {
                "derived": "strong_technical_profile"
            },
            {
                "derived": "ai_oriented"
            }
        ],
        "conclusion": "strong_ai_candidate"
    },


    # Technical + security
    {
        "conditions": [
            {
                "derived": "strong_technical_profile"
            },
            {
                "derived": "security_oriented"
            }
        ],
        "conclusion": "strong_security_candidate"
    }

]


# ==========================================
# CAREER RULES
# ==========================================

CAREER_RULES = [

    # --------------------------------------
    # SOFTWARE ENGINEER
    # --------------------------------------

    {
        "career": "Software Engineer",

        "conditions": [

            {
                "fact": "programming",
                "values": ["advanced", "intermediate"],
                "weight": 25
            },

            {
                "fact": "problem_solving",
                "values": ["high", "medium"],
                "weight": 20
            },

            {
                "fact": "technology",
                "values": ["high", "medium"],
                "weight": 15
            },

            {
                "derived": "strong_technical_profile",
                "weight": 20
            },

            {
                "derived": "strong_software_candidate",
                "weight": 20
            }

        ],

        "reason":
            "Your programming ability, problem-solving skills "
            "and technical interests strongly align with software development."
    },


    # --------------------------------------
    # AI / ML ENGINEER
    # --------------------------------------

    {
        "career": "AI / ML Engineer",

        "conditions": [

            {
                "fact": "programming",
                "values": ["advanced", "intermediate"],
                "weight": 20
            },

            {
                "fact": "mathematics",
                "values": ["high", "medium"],
                "weight": 20
            },

            {
                "fact": "data_interest",
                "values": ["high", "medium"],
                "weight": 15
            },

            {
                "derived": "strong_analytical_profile",
                "weight": 15
            },

            {
                "derived": "strong_ai_candidate",
                "weight": 30
            }

        ],

        "reason":
            "Your programming, mathematical and analytical interests "
            "align well with artificial intelligence and machine learning."
    },


    # --------------------------------------
    # DATA SCIENTIST
    # --------------------------------------

    {
        "career": "Data Scientist",

        "conditions": [

            {
                "fact": "mathematics",
                "values": ["high", "medium"],
                "weight": 25
            },

            {
                "fact": "data_interest",
                "values": ["high", "medium"],
                "weight": 25
            },

            {
                "fact": "problem_solving",
                "values": ["high", "medium"],
                "weight": 15
            },

            {
                "derived": "data_oriented",
                "weight": 15
            },

            {
                "derived": "strong_data_candidate",
                "weight": 20
            }

        ],

        "reason":
            "Your interest in mathematics, data and analytical "
            "problem solving fits data science."
    },


    # --------------------------------------
    # CYBERSECURITY ANALYST
    # --------------------------------------

    {
        "career": "Cybersecurity Analyst",

        "conditions": [

            {
                "fact": "security_interest",
                "values": ["high", "medium"],
                "weight": 30
            },

            {
                "fact": "problem_solving",
                "values": ["high", "medium"],
                "weight": 20
            },

            {
                "fact": "technology",
                "values": ["high", "medium"],
                "weight": 15
            },

            {
                "derived": "security_oriented",
                "weight": 15
            },

            {
                "derived": "strong_security_candidate",
                "weight": 20
            }

        ],

        "reason":
            "Your interest in cybersecurity, technology and "
            "problem solving matches cybersecurity-oriented work."
    },


    # --------------------------------------
    # UI/UX DESIGNER
    # --------------------------------------

    {
        "career": "UI/UX Designer",

        "conditions": [

            {
                "fact": "creativity",
                "values": ["high", "medium"],
                "weight": 30
            },

            {
                "fact": "work_style",
                "values": ["creative"],
                "weight": 25
            },

            {
                "fact": "activity",
                "values": ["design"],
                "weight": 25
            },

            {
                "derived": "creative_profile",
                "weight": 20
            }

        ],

        "reason":
            "Your creativity and preference for design-oriented "
            "work fit UI/UX design."
    },


    # --------------------------------------
    # WEB / APP DEVELOPER
    # --------------------------------------

    {
        "career": "Web / App Developer",

        "conditions": [

            {
                "fact": "programming",
                "values": ["advanced", "intermediate", "beginner"],
                "weight": 25
            },

            {
                "fact": "technology",
                "values": ["high", "medium"],
                "weight": 20
            },

            {
                "fact": "activity",
                "values": ["software"],
                "weight": 25
            },

            {
                "derived": "software_oriented",
                "weight": 15
            },

            {
                "fact": "creativity",
                "values": ["high", "medium"],
                "weight": 15
            }

        ],

        "reason":
            "Your interest in programming, software development "
            "and technology fits web and application development."
    },


    # --------------------------------------
    # TECHNOLOGY PRODUCT MANAGER
    # --------------------------------------

    {
        "career": "Technology Product Manager",

        "conditions": [

            {
                "fact": "technology",
                "values": ["high", "medium"],
                "weight": 20
            },

            {
                "fact": "work_style",
                "values": ["leadership", "people"],
                "weight": 25
            },

            {
                "fact": "teamwork",
                "values": ["team", "both"],
                "weight": 20
            },

            {
                "derived": "collaborative_leader",
                "weight": 25
            },

            {
                "derived": "technology_focused",
                "weight": 10
            }

        ],

        "reason":
            "Your technology interest, teamwork and leadership "
            "preferences align with technology product management."
    }

]


# ==========================================
# CAREER LEARNING ROADMAPS
# ==========================================

CAREER_ROADMAPS = {

    "Software Engineer": {

        "skills": [
            "Programming fundamentals",
            "Data Structures and Algorithms",
            "Object-Oriented Programming",
            "Git and GitHub",
            "Databases and SQL",
            "Software development and testing"
        ],

        "technologies": [
            "C++ / Java / Python",
            "Git",
            "GitHub",
            "MySQL",
            "REST APIs"
        ],

        "projects": [
            "Build a Student Management System",
            "Build a REST API",
            "Build a full-stack web application"
        ]
    },


    "AI / ML Engineer": {

        "skills": [
            "Python programming",
            "Mathematics for Machine Learning",
            "Statistics",
            "Data Structures and Algorithms",
            "Machine Learning",
            "Deep Learning"
        ],

        "technologies": [
            "Python",
            "NumPy",
            "Pandas",
            "Scikit-learn",
            "TensorFlow / PyTorch"
        ],

        "projects": [
            "Build a prediction model",
            "Build a classification project",
            "Build an AI-powered application"
        ]
    },


    "Data Scientist": {

        "skills": [
            "Python",
            "Statistics",
            "Probability",
            "Data Analysis",
            "Data Visualization",
            "Machine Learning"
        ],

        "technologies": [
            "Python",
            "Pandas",
            "NumPy",
            "Matplotlib",
            "SQL",
            "Scikit-learn"
        ],

        "projects": [
            "Analyze a real-world dataset",
            "Build a data visualization dashboard",
            "Build a machine learning prediction project"
        ]
    },


    "Cybersecurity Analyst": {

        "skills": [
            "Computer Networks",
            "Operating Systems",
            "Linux",
            "Cybersecurity fundamentals",
            "Cryptography",
            "Security analysis"
        ],

        "technologies": [
            "Linux",
            "Wireshark",
            "Python",
            "Networking tools",
            "Security testing tools"
        ],

        "projects": [
            "Build a network monitoring tool",
            "Create a password security analyzer",
            "Build a basic vulnerability scanner"
        ]
    },


    "UI/UX Designer": {

        "skills": [
            "UI design",
            "UX principles",
            "User research",
            "Wireframing",
            "Prototyping",
            "Visual design"
        ],

        "technologies": [
            "Figma",
            "Adobe XD",
            "HTML",
            "CSS",
            "Design systems"
        ],

        "projects": [
            "Design a mobile application",
            "Create a website prototype",
            "Redesign an existing application"
        ]
    },


    "Web / App Developer": {

        "skills": [
            "Programming fundamentals",
            "HTML and CSS",
            "JavaScript",
            "Frontend development",
            "Backend development",
            "Databases"
        ],

        "technologies": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "MySQL"
        ],

        "projects": [
            "Build a responsive website",
            "Build a CRUD application",
            "Build a full-stack web application"
        ]
    },


    "Technology Product Manager": {

        "skills": [
            "Product management",
            "Communication",
            "Leadership",
            "Problem solving",
            "Market research",
            "Project management"
        ],

        "technologies": [
            "Jira",
            "Notion",
            "Figma",
            "Google Analytics",
            "Product analytics tools"
        ],

        "projects": [
            "Create a product requirements document",
            "Design a product roadmap",
            "Analyze and improve an existing product"
        ]
    }

}