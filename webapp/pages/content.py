"""Site copy, kept as plain Python data since nothing here needs a database."""

SITE_NAME = "Julius Kricheldorff"
SITE_TAGLINE = "Data Analyst | PhD Student - Carl von Ossietzky University"

SOCIAL_LINKS = [
    {"icon": "mail", "href": "mailto:julius@kricheldorff.com", "label": "Email"},
    {"icon": "github", "href": "https://github.com/shichik07/", "label": "GitHub"},
    {"icon": "bluesky", "href": "https://bsky.app/profile/berlincj.bsky.social", "label": "Bluesky"},
    {"icon": "linkedin", "href": "https://www.linkedin.com/in/julius-kricheldorff-b858a4177/", "label": "LinkedIn"},
    {"icon": "scholar", "href": "https://scholar.google.de/citations?hl=en&user=BuobG4hQmpgC", "label": "Google Scholar"},
    {"icon": "osf", "href": "https://osf.io/profile/", "label": "OSF"},
]

NAV_LINKS = [
    {"label": "Home", "url_name": "home"},
    {"label": "Projects", "url_name": "projects"},
    {"label": "Personal", "url_name": "personal"},
    {"label": "CV", "url_name": "cv"},
]

HOME_BIO = [
    "I am a Data Analyst with CGM Mare and a former PhD student at the Department of "
    "Neurology at Carl von Ossietzky University Oldenburg. My doctoral research focuses "
    "on investigating cognitive symptoms associated with Parkinson's disease (PD), with "
    "a particular emphasis on decision-making and cognitive control abilities.",
    "In my academic work, I employ a multifaceted approach combining behavioral "
    "experiments and EEG recordings. I utilize advanced analytical methods, including "
    "Bayesian statistical modeling and Drift-Diffusion model analyses.",
]

PROJECTS = [
    {
        "title": "Adaptive control in Parkinson's disease",
        "body": (
            "Our study investigated whether Parkinson's disease (PD) patients can adjust "
            "their cognitive control based on context, comparing them to age-matched "
            "healthy controls. We examined both proactive and reactive aspects of "
            "cognitive control, areas where previous research has shown mixed results. "
            "Our findings revealed that PD patients generally have impaired proactive "
            "control and reduced ability to modulate conflict information in reactive "
            "control. These results suggest PD affects multiple aspects of cognitive "
            "control, potentially impacting patients' adaptability to changing "
            "environments."
        ),
        "link": {"label": "Brain Communications", "href": "https://doi.org/10.1093/braincomms/fcad327"},
    },
    {
        "title": "Low-Frequency Deep Brain Stimulation Improves Response Inhibition in Parkinson's Disease",
        "body": (
            "In a recent study, we explored the effects of low-frequency deep brain "
            "stimulation (DBS) on cognitive function in Parkinson's disease patients. We "
            "compared 20Hz (beta band) stimulation of the subthalamic nucleus (STN) to "
            "standard high-frequency and no stimulation. The study involved 17 "
            "participants who underwent four neuropsychological experiments testing "
            "various aspects of cognitive control. Our results revealed that low-frequency "
            "STN-DBS improved reactive response inhibition compared to high-frequency and "
            "no stimulation. This finding suggests that beta-band STN-DBS may offer "
            "cognitive benefits for Parkinson's patients, potentially opening new "
            "possibilities for managing non-motor symptoms in Parkinson's disease using "
            "DBS technology."
        ),
        "link": {"label": "Brain Communications", "href": "https://academic.oup.com/braincomms/article/7/6/fcaf474/8363303"},
    },
    {
        "title": "Can individuals with Parkinson's disease use prior information in their decision-making?",
        "body": (
            "A forthcoming project, where we investigate how patients with PD can "
            "integrate prior information into their decisions. Stay tuned!"
        ),
        "link": None,
    },
]

RECIPES = [
    {
        "slug": "marinated-beef-fillet",
        "title": "Marinated Beef Fillet",
        "teaser": "The perfect recipe for your Christmas buffet - use as topping for salad or as charcuterie on top of bread.",
        "category": "Appetizers",
        "date": "December 14, 2025",
        "source": {"label": "Essen und Trinken", "href": "https://www.essen-und-trinken.de/", "note": "August 2006"},
        "ingredients": [
            "400g beef fillet",
            "150g coarse salt",
            "60g sugar",
            "3 tbs Vin Santo",
            "fresh thyme",
        ],
        "instructions": [
            "Remove thyme leaves from stems and chop them roughly. Crush the pepper-corns. Mix salt, sugar and wine into a paste.",
            "Pat the fillet dry - first roll in your thyme leaves, next the pepper.",
            "Spread the salt sugar paste around the fillet and leave it in the fridge for 24 hours.",
            "Remove the paste under running water, pat the fillet dry and tightly wrap it in cellophane wrap. Keep it in the fridge for another 24 hours.",
            "Cut it into thin slices and serve as you like - e.g. as a topping to a salad, on bread etc.",
        ],
        "tips": [
            "If you cut the fillet by hand, put it in the freezer for half an hour before.",
        ],
    },
    {
        "slug": "recipe-homemade-pizza",
        "title": "Homemade Pizza from Scratch",
        "teaser": "Create authentic Italian-style pizza at home with this simple recipe.",
        "category": "Main Courses",
        "date": "December 14, 2025",
        "source": None,
        "ingredients": [
            "360g all-purpose flour (Italian 00 flour or German 405)",
            "a pinch of yeast (depends how long you want your dough to rest)",
            "13g salt",
            "12g olive oil",
            "240g warm water",
        ],
        "instructions": [
            "Make the dough: Mix flour, yeast, and salt. Add water and oil, knead for 10 minutes. Let rise for at least 6 hours, best overnight in the fridge.",
            "Preheat oven: Set to highest temperature (usually 500°F/260°C).",
            "Shape the pizza: Cut the dough into chunks ~200g. Spread out your dough on a floured surface.",
            "Assemble: Spread sauce, add your toppings and drizzle with olive oil.",
            "Bake: 10-12 minutes until crust is golden and cheese is bubbly.",
            "Finish: Top with fresh basil before serving.",
        ],
        "tips": [
            "Use a pizza stone for crispy crust.",
            "Don't overload with toppings.",
            "Let the dough rest at room temperature for 30 minutes before shaping.",
        ],
    },
]

RECIPES_BY_SLUG = {recipe["slug"]: recipe for recipe in RECIPES}
