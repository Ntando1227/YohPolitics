from django.shortcuts import render, get_object_or_404
from .models import Party, ManifestoPolicy


POLICY_ANALYZER_DATA = {

    "nationalisation": {
        "title": "Nationalisation",
        "summary": "State ownership of major industries such as mines, banks, energy and strategic sectors.",

        "real_argument": "Nationalisation is not fundamentally about ownership alone. It is about sovereignty, developmental control, and the political question of who directs accumulation in society. The underlying argument is that South Africa's democratic transition transferred political authority without meaningfully restructuring economic power. Supporters therefore argue that leaving strategic sectors such as mining, banking, energy and logistics under concentrated private ownership permanently weakens the state's ability to drive redistribution, industrialisation and long-term developmental planning.",

        "public_support": "Support for nationalisation emerges from a historical reading of the South African economy. Many citizens observe that despite political democracy, wealth concentration, racial inequality and ownership patterns remain structurally intact. Nationalisation therefore resonates not only economically, but symbolically. It communicates the idea that political liberation without economic control is incomplete.",

        "public_concern": "The core concern is institutional rather than ideological. Critics question whether the South African state currently possesses the bureaucratic capacity, technical competence, procurement integrity and political insulation required to manage large-scale state ownership effectively. State capture significantly damaged public confidence in the state's developmental ability.",

        "cost": "Extremely expensive. State acquisition, restructuring, legal disputes, compensation battles, operational funding and management reform would require massive long-term fiscal commitment.",

        "difficulty": "Very high. Nationalisation requires institutional coordination, sector expertise, legislative restructuring and administrative competence at a scale the current state often struggles to demonstrate.",

        "corruption_risk": "High. Expanding state control without strengthening governance systems could create larger opportunities for procurement abuse, cadre deployment and elite capture.",

        "winners": "Potential beneficiaries include organised labour, historically excluded communities, developmental sectors and citizens who support stronger public ownership.",

        "losers": "Large corporations, investors dependent on policy certainty, shareholders and sectors reliant on private-sector confidence may experience instability or resistance.",

        "state_capacity": "This policy succeeds or fails on state capacity. Without institutional competence, nationalisation risks expanding dysfunction rather than developmental transformation.",

        "daily_life": "If managed effectively, citizens could see expanded infrastructure investment, strategic planning and stronger developmental coordination. If managed poorly, the result could be declining services, inefficiency and economic instability.",

        "political_risk": "The political risk is that nationalisation becomes rhetorically revolutionary but administratively hollow. States can inherit ownership without inheriting operational capacity. In that scenario, public ownership may deepen fiscal pressure without producing developmental transformation.",

        "hard_question": "Can South Africa construct a capable developmental state before attempting large-scale expansion of state ownership?",

        "yoh_view": "What is really happening here is a struggle over the meaning of liberation itself. Nationalisation debates are ultimately arguments about whether democracy should merely change governments, or fundamentally reorganise economic power. The emotional force behind the policy comes from the perception that the economy still feels socially distant from the majority population."
    },


    "free_education": {
        "title": "Free Education",
        "summary": "Government-funded higher education and reduced financial barriers to learning.",

        "real_argument": "Free education is fundamentally an argument about social reproduction and intergenerational inequality. The policy assumes that access to higher education is no longer a luxury, but a structural requirement for economic participation in a technologically advanced economy. Supporters therefore argue that excluding poor students through fees reproduces class inequality across generations.",

        "public_support": "The policy resonates because education occupies a unique emotional position in South African political culture. For many households, education represents the primary imagined route out of poverty, unemployment and historical exclusion. Student debt is therefore experienced not only financially, but psychologically and politically.",

        "public_concern": "The concern is whether expansion can occur without institutional degradation. Universities require stable funding, research capacity, infrastructure investment, staffing expansion and administrative competence. A system that increases numerical access while collapsing academically can produce mass disillusionment rather than mobility.",

        "cost": "Very expensive. Sustainable funding would require long-term fiscal expansion, higher taxation, spending reprioritisation or economic growth strong enough to support expanded social investment.",

        "difficulty": "High. Expanding access while protecting quality, infrastructure, accommodation and institutional capacity is administratively complex.",

        "corruption_risk": "Moderate to high. Student funding systems can become vulnerable to administrative failure, ghost beneficiaries, procurement abuse and delayed payments.",

        "winners": "Working-class students, poor households, rural youth, first-generation graduates and historically excluded communities.",

        "losers": "Taxpayers facing increased fiscal pressure and institutions forced to absorb expansion without sufficient resources may experience strain.",

        "state_capacity": "The policy depends heavily on competent administration, reliable funding pipelines and long-term educational planning.",

        "daily_life": "Students may experience reduced financial anxiety, improved access and greater educational mobility. However, underfunded expansion could also increase overcrowding and declining institutional quality.",

        "political_risk": "The political danger is that governments may frame access as transformation while quietly underfunding institutional quality. This creates a situation where students enter the system but graduate into weak labour absorption and declining institutional prestige.",

        "hard_question": "Can South Africa massify higher education without reproducing a low-quality, underfunded system that ultimately fails working-class students?",

        "yoh_view": "The deeper issue here is not simply fees. It is whether post-apartheid South Africa has built an economy capable of converting educational expansion into meaningful economic inclusion. Degrees alone cannot resolve structural unemployment."
    },


    "land_expropriation": {
        "title": "Land Expropriation",
        "summary": "Redistribution of land through expropriation with reduced or no compensation.",

        "real_argument": "Land expropriation is fundamentally a debate about historical justice, territorial belonging and the unfinished nature of post-apartheid restructuring. Supporters argue that racial land concentration remains one of the clearest visible continuities between apartheid and democracy. Land therefore becomes both a material and symbolic question.",

        "public_support": "Support emerges because land carries meanings beyond economics. It represents dignity, ancestry, citizenship, identity, security and historical recognition. For many South Africans, unresolved land inequality signifies that historical dispossession was politically acknowledged but never materially corrected.",

        "public_concern": "The concern is whether redistribution can occur without administrative collapse, elite capture or agricultural instability. Internationally, land reform outcomes vary dramatically depending on institutional planning, beneficiary support, infrastructure, financing and post-transfer governance.",

        "cost": "Moderate to very high depending on implementation design, agricultural support systems and legal disputes.",

        "difficulty": "Extremely high. Successful redistribution requires land audits, infrastructure, water access, financing, training and long-term governance support.",

        "corruption_risk": "High. Redistribution programmes globally are vulnerable to politically connected beneficiaries and elite capture.",

        "winners": "Landless communities, emerging farmers, housing applicants and historically dispossessed populations.",

        "losers": "Commercial landholders, sectors dependent on agricultural certainty and investors worried about legal stability.",

        "state_capacity": "The state would need strong institutional systems for allocation, mediation, support and agricultural planning.",

        "daily_life": "If implemented effectively, redistribution could expand housing access, farming opportunities and economic participation. Poor implementation could create instability, uncertainty and declining productivity.",

        "political_risk": "The political risk is that land reform becomes permanently symbolic. Political parties may repeatedly invoke land emotionally while redistribution remains slow, selective or captured by connected elites.",

        "hard_question": "Can South Africa pursue meaningful redistribution while simultaneously protecting agricultural productivity, institutional legitimacy and social stability?",

        "yoh_view": "At its deepest level, this debate is about whether political reconciliation without substantial economic restructuring can remain socially sustainable over generations."
    }

}


def home(request):
    return render(request, "core/home.html")


def parties(request):
    parties = Party.objects.all()
    return render(request, "core/parties.html", {"parties": parties})


def party_detail(request, slug):
    party = get_object_or_404(Party, slug=slug)
    policies = ManifestoPolicy.objects.filter(party=party)

    return render(request, "core/party_detail.html", {
        "party": party,
        "policies": policies,
    })


def policy_feasibility(request):

    selected_key = request.GET.get("policy", "nationalisation")

    selected_policy = POLICY_ANALYZER_DATA.get(
        selected_key,
        POLICY_ANALYZER_DATA["nationalisation"]
    )

    return render(request, "core/policy_feasibility.html", {
        "policies": POLICY_ANALYZER_DATA,
        "selected_policy": selected_policy,
        "selected_key": selected_key,
    })

def learn(request):
    return render(request, "core/learn.html")


def campus_politics(request):
    return render(request, "core/campus_politics.html")


def political_glossary(request):
    query = request.GET.get("q", "").lower().strip()

    try:
        terms = GLOSSARY_TERMS
    except NameError:
        terms = []

    if query:
        terms = [
            item for item in terms
            if query in item.get("term", "").lower()
            or query in item.get("full", "").lower()
            or query in item.get("meaning", "").lower()
            or query in item.get("why", "").lower()
        ]

    return render(request, "core/political_glossary.html", {
        "terms": terms,
        "query": query,
    })


def policy_compare(request):
    parties = Party.objects.all().order_by("name")
    return render(request, "core/policy_compare.html", {
        "parties": parties,
    })


def compass(request):
    return render(request, "core/compass.html", {
        "questions": [],
        "result": None,
    })


def affects_you(request):
    return render(request, "core/affects_you.html")


def everyday_politics(request):
    return render(request, "core/everyday_politics.html")


def party_worldviews(request):
    parties = Party.objects.all().order_by("name")
    return render(request, "core/party_worldviews.html", {
        "parties": parties,
    })


def political_archetypes(request):
    return render(request, "core/political_archetypes.html")


def politics_identity(request):
    return render(request, "core/politics_identity.html")


def debate_simulator(request):
    parties = Party.objects.all().order_by("name")
    return render(request, "core/debate_simulator.html", {
        "parties": parties,
        "topics": {},
        "selected_topic": "",
        "selected_slugs": [],
        "debate_rows": [],
        "topic": {},
    })


def commentary(request):
    from .models import CommentaryArticle

    articles = CommentaryArticle.objects.all().order_by("-id")

    return render(request, "core/commentary.html", {
        "articles": articles,
        "commentary_articles": articles,
        "featured_article": articles.first(),
    })


def article_detail(request, article_id):
    from .models import CommentaryArticle

    article = CommentaryArticle.objects.get(id=article_id)
    related_articles = CommentaryArticle.objects.exclude(id=article_id)[:3]

    return render(request, "core/article_detail.html", {
        "article": article,
        "related_articles": related_articles,
    })


def site_search(request):
    query = request.GET.get("q", "").strip()
    return render(request, "core/search.html", {
        "query": query,
        "party_results": [],
        "policy_results": [],
        "commentary_results": [],
        "glossary_results": [],
    })


def about(request):
    return render(request, "core/about.html")

COMPASS_QUESTIONS = [
    {"id": "q1", "text": "Government should play a bigger role in reducing inequality.", "axis": "economic", "left": 1, "right": -1},
    {"id": "q2", "text": "Private businesses are usually better than government at creating jobs.", "axis": "economic", "left": -1, "right": 1},
    {"id": "q3", "text": "Land reform is necessary to correct historical injustice.", "axis": "transformation", "left": 1, "right": -1},
    {"id": "q4", "text": "South Africa needs stronger anti-corruption institutions more than new political promises.", "axis": "governance", "left": 1, "right": -1},
    {"id": "q5", "text": "Crime should be handled with much tougher policing and sentencing.", "axis": "crime", "left": 1, "right": -1},
    {"id": "q6", "text": "Poverty and unemployment are major causes of crime.", "axis": "crime", "left": -1, "right": 1},
    {"id": "q7", "text": "South Africa should enforce immigration laws much more strictly.", "axis": "immigration", "left": 1, "right": -1},
    {"id": "q8", "text": "South Africa should remain open and compassionate toward migrants from the continent.", "axis": "immigration", "left": -1, "right": 1},
    {"id": "q9", "text": "Free education should be a major national priority.", "axis": "economic", "left": 1, "right": -1},
    {"id": "q10", "text": "Government failure is mainly caused by corruption and weak institutions.", "axis": "governance", "left": 1, "right": -1},
]

PERSONALITY_QUESTIONS = [
    {"id": "p1", "text": "I feel young educated people are being failed by the economy.", "type": "frustrated_graduate"},
    {"id": "p2", "text": "I am tired of paying into a state that does not deliver.", "type": "exhausted_taxpayer"},
    {"id": "p3", "text": "Liberation history still matters when judging parties.", "type": "liberation_loyalist"},
    {"id": "p4", "text": "Immigration pressure is one of South Africa's biggest problems.", "type": "border_control_voter"},
    {"id": "p5", "text": "Corruption is the main reason South Africa is failing.", "type": "anti_corruption_voter"},
    {"id": "p6", "text": "I care more about practical delivery than ideology.", "type": "township_pragmatist"},
    {"id": "p7", "text": "No political party fully represents me.", "type": "politically_homeless"},
]

PERSONALITY_TYPES = {
    "frustrated_graduate": "The Frustrated Graduate",
    "exhausted_taxpayer": "The Exhausted Taxpayer",
    "liberation_loyalist": "The Liberation Loyalist",
    "border_control_voter": "The Border-Control Voter",
    "anti_corruption_voter": "The Anti-Corruption Voter",
    "township_pragmatist": "The Township Pragmatist",
    "politically_homeless": "The Politically Homeless Voter",
}

PARTY_PROFILES = {
    "ANC": {"economic": 7, "transformation": 8, "governance": 4, "crime": 5, "immigration": 5},
    "DA": {"economic": 3, "transformation": 3, "governance": 9, "crime": 7, "immigration": 6},
    "EFF": {"economic": 9, "transformation": 10, "governance": 5, "crime": 6, "immigration": 4},
    "ActionSA": {"economic": 4, "transformation": 5, "governance": 8, "crime": 8, "immigration": 9},
    "IFP": {"economic": 5, "transformation": 6, "governance": 7, "crime": 8, "immigration": 6},
    "MK": {"economic": 8, "transformation": 9, "governance": 4, "crime": 7, "immigration": 6},
    "GOOD": {"economic": 6, "transformation": 7, "governance": 7, "crime": 5, "immigration": 5},
    "RISE": {"economic": 5, "transformation": 6, "governance": 8, "crime": 6, "immigration": 5},
}

def compass(request):
    result = None
    questions = COMPASS_QUESTIONS + PERSONALITY_QUESTIONS

    if request.method == "POST":
        axis_scores = {
            "economic": 5,
            "transformation": 5,
            "governance": 5,
            "crime": 5,
            "immigration": 5,
        }

        personality_scores = {key: 0 for key in PERSONALITY_TYPES.keys()}

        for question in COMPASS_QUESTIONS:
            answer = int(request.POST.get(question["id"], 0))
            axis_scores[question["axis"]] += answer

        for question in PERSONALITY_QUESTIONS:
            answer = int(request.POST.get(question["id"], 0))
            if answer > 0:
                personality_scores[question["type"]] += answer

        for key in axis_scores:
            axis_scores[key] = max(0, min(10, axis_scores[key]))

        matches = []

        for abbreviation, profile in PARTY_PROFILES.items():
            difference = 0

            for axis, score in axis_scores.items():
                difference += abs(score - profile.get(axis, 5))

            match = max(0, round(100 - difference * 4))
            party = Party.objects.filter(abbreviation=abbreviation).first()

            matches.append({
                "abbreviation": abbreviation,
                "party": party,
                "match": match,
            })

        matches = sorted(matches, key=lambda x: x["match"], reverse=True)

        top_personality_key = max(personality_scores, key=personality_scores.get)

        result = {
            "axis_scores": axis_scores,
            "matches": matches[:5],
            "personality": {
                "title": PERSONALITY_TYPES[top_personality_key],
                "description": "Your political instincts are shaped by the issues, fears, frustrations and hopes reflected in this voter type.",
                "likely_parties": ", ".join([m["abbreviation"] for m in matches[:3]]),
            },
            "economic_label": "Redistribution-focused" if axis_scores["economic"] >= 6 else "Market/growth-focused",
            "transformation_label": "Transformation-focused" if axis_scores["transformation"] >= 6 else "Gradual reform-focused",
            "governance_label": "Institution-first" if axis_scores["governance"] >= 6 else "Politics-first or mixed",
            "crime_label": "Law-and-order leaning" if axis_scores["crime"] >= 6 else "Social prevention leaning",
            "immigration_label": "Strict border-control leaning" if axis_scores["immigration"] >= 6 else "Migration-sensitive leaning",
            "secondary_personalities": [],
        }

    return render(request, "core/compass.html", {
        "questions": questions,
        "result": result,
    })

def policy_compare(request):
    parties = Party.objects.all().order_by("name")

    selected_category = request.GET.get("category", "overview")
    selected_slugs = request.GET.getlist("parties")

    if not selected_slugs:
        selected_parties = parties[:3]
        selected_slugs = [party.slug for party in selected_parties]
    else:
        selected_parties = Party.objects.filter(slug__in=selected_slugs).order_by("name")

    category_copy = {
        "overview": {
            "title": "Party overview",
            "intro": "This compares the broad political identity, ideological posture and deeper political argument each party is making."
        },
        "economy": {
            "title": "Economic comparison",
            "intro": "This compares how parties think about jobs, markets, redistribution, public ownership, entrepreneurship and the role of the state."
        },
        "governance": {
            "title": "Governance comparison",
            "intro": "This compares how parties understand corruption, institutional reform, public administration, state capacity and delivery."
        },
        "transformation": {
            "title": "Transformation comparison",
            "intro": "This compares how parties approach equality, historical redress, race, class, land, empowerment and social justice."
        },
        "crime": {
            "title": "Crime and safety comparison",
            "intro": "This compares how parties think about policing, courts, violence, prevention, punishment and public safety."
        },
        "immigration": {
            "title": "Immigration comparison",
            "intro": "This compares how parties approach borders, migration, documentation, African solidarity, jobs and social pressure."
        },
        "youth": {
            "title": "Youth politics comparison",
            "intro": "This compares how parties speak to young people, unemployment, education, opportunity and the future."
        },
    }

    current_copy = category_copy.get(selected_category, category_copy["overview"])

    return render(request, "core/policy_compare.html", {
        "parties": parties,
        "selected_parties": selected_parties,
        "selected_slugs": selected_slugs,
        "selected_category": selected_category,
        "category_title": current_copy["title"],
        "category_intro": current_copy["intro"],
    })
