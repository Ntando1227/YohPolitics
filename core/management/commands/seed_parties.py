from django.core.management.base import BaseCommand
from core.models import Party, ManifestoPolicy def add_policy( party, category, title, position, analysis, strengths, weaknesses, affected, commentary
): ManifestoPolicy.objects.create( party=party, category=category, policy_title=title, manifesto_position=position, simplified_explanation=analysis, possible_advantages=strengths, possible_concerns=weaknesses, affected_groups=affected, yoh_analysis=commentary, ) class Command(BaseCommand): help = "Seed DA, EFF and ActionSA" def handle(self, *args, **kwargs): ManifestoPolicy.objects.all().delete() Party.objects.filter( abbreviation__in=["DA", "EFF", "ActionSA"] ).delete() # ===================================================== # DA # ===================================================== da = Party.objects.create( name="Democratic Alliance", abbreviation="DA", leader="John Steenhuisen", founded="2000", ideology="Liberal democracy, constitutionalism, market-oriented reform", political_position="Centre to centre-right", short_explainer="""
The Democratic Alliance presents itself as the party of competent government, institutional repair, economic growth, anti-corruption politics, and constitutional democracy. Its 2024 political messaging is built around the idea that South Africa's biggest problem is not a lack of policy promises, but the collapse of state capability itself.
""", historical_context="""
The DA emerged from South Africa's liberal opposition tradition. Over time it evolved from a smaller parliamentary opposition into the country's largest opposition party. The party's modern identity was shaped heavily by opposition to corruption, state capture, failing municipalities, load-shedding, and weakening public institutions during the ANC era. It has also spent years trying to expand beyond its earlier image as a party primarily supported by minorities and middle-class voters.
""", political_identity="""
The DA is fundamentally a constitutional liberal party. Its politics revolves around:
- rule of law,
- institutional stability,
- clean administration,
- accountability,
- economic growth,
- professional public service,
- and protection of constitutional democracy. The DA believes South Africa's biggest crisis is state failure. For the DA, corruption, cadre deployment, failing infrastructure, collapsing municipalities, weak policing, and broken public services are not separate issues. They are symptoms of a state that has lost capacity. This is why the party repeatedly talks about:
- merit-based appointments,
- functioning institutions,
- professional governance,
- infrastructure repair,
- and efficient administration. The DA's worldview is less revolutionary than managerial. It believes South Africa does not necessarily need to destroy its economic system entirely, but rather fix the institutions that allow the economy and society to function.
""", society_vision="""
The DA imagines a South Africa where:
- trains work,
- electricity is stable,
- municipalities function,
- schools teach properly,
- corruption is punished,
- and businesses feel confident enough to invest and hire. Its ideal society is:
- rules-based,
- economically productive,
- institutionally stable,
- infrastructure-driven,
- and governed through professional administration rather than political patronage. The DA generally prefers gradual reform over radical economic restructuring. It believes stability, investment, and growth create the conditions necessary for long-term poverty reduction and opportunity expansion.
""", economic_approach="""
The DA supports a mixed but market-oriented economy. It generally believes:
- businesses create jobs,
- investment drives growth,
- entrepreneurship matters,
- and the state's role is to create stable conditions for economic expansion. The party focuses heavily on:
- energy reform,
- transport infrastructure,
- investment confidence,
- reducing corruption,
- reducing administrative inefficiency,
- and improving public service delivery. The DA does not strongly support large-scale nationalisation or aggressive state ownership. Critics often argue that the party places too much faith in markets and private-sector-led growth. Supporters argue that without growth, South Africa cannot sustainably reduce unemployment or poverty.
""", equality_view="""
The DA approaches equality primarily through:
- opportunity,
- education,
- economic growth,
- institutional fairness,
- and service delivery. Its deeper argument is that equality cannot exist if:
- schools fail,
- corruption steals resources,
- municipalities collapse,
- and economic growth stagnates. The DA generally does not frame equality mainly through radical redistribution. Instead, it argues that expanding access to opportunity is more sustainable than aggressively restructuring ownership. This is one of the biggest ideological divides between the DA and parties like the EFF. Critics argue that the DA underestimates:
- structural racial inequality,
- historic dispossession,
- land concentration,
- and wealth inequality. Supporters argue that growth and institutional repair are necessary before meaningful inclusion can happen.
""", immigration_view="""
The DA generally supports:
- lawful immigration,
- border management,
- proper documentation systems,
- and stronger Home Affairs administration. However, it usually avoids the highly confrontational anti-immigration rhetoric used by more populist parties. The DA frames immigration more as:
- a governance issue,
- an administrative issue,
- and a state-capacity issue. It argues the state must know:
- who enters the country,
- who works,
- who qualifies for services,
- and how migration is managed. The party tends to avoid blaming immigrants for South Africa's economic crisis.
""", crime_view="""
The DA treats crime as one of the biggest threats to:
- freedom,
- dignity,
- investment,
- business activity,
- and everyday life. Its approach focuses heavily on:
- professional policing,
- stronger prosecution,
- intelligence capacity,
- anti-corruption systems,
- and rebuilding trust in law enforcement. The DA often frames crime as a symptom of institutional collapse. Its argument is that a state unable to police effectively cannot protect:
- democracy,
- communities,
- investment,
- or social stability.
""", social_approach="""
The DA supports:
- education reform,
- healthcare access,
- anti-poverty programmes,
- and social welfare systems. However, it generally frames social progress through:
- institutional efficiency,
- growth,
- service delivery,
- and opportunity creation. Its critics sometimes argue that the party's language can sound emotionally distant in a country with deep inequality and historical pain. Supporters argue that dignity comes from systems that actually work consistently.
""", governance_style="""
The DA's governance style is:
- technocratic,
- managerial,
- performance-driven,
- and institution-focused. It strongly opposes:
- cadre deployment,
- political interference in administration,
- and corruption networks. The party wants:
- merit-based appointments,
- clean audits,
- measurable outcomes,
- and administrative professionalism. Its political personality is strongest when discussing:
- budgets,
- municipalities,
- infrastructure,
- energy,
- policing,
- and governance performance.
""", youth_relevance="""
Young South Africans may connect strongly with the DA because the party speaks directly to:
- unemployment,
- load-shedding,
- infrastructure collapse,
- corruption,
- failing schools,
- and crime. However, the DA also faces challenges among younger voters who want:
- stronger redistribution,
- faster transformation,
- deeper social justice,
- and more emotional engagement with inequality. The major question for many young voters is:
Can competent administration alone fix historical injustice?
""", major_support_base="""
The DA generally performs strongly among:
- urban voters,
- middle-class communities,
- governance-focused voters,
- professionals,
- business-oriented citizens,
- and communities frustrated by corruption and service delivery collapse.
""", common_criticisms="""
Supporters argue the DA represents:
- clean government,
- institutional stability,
- accountability,
- and practical governance. Critics argue the party sometimes struggles to emotionally connect with:
- black historical pain,
- economic exclusion,
- land inequality,
- and transformation politics. The central debate around the DA is whether:
South Africa mainly needs competent reform,
or whether competence without deeper redistribution simply protects the existing economic order.
""", yoh_commentary="""
The DA's strongest political weapon is competence. Its argument is simple:
Nothing else works if the state itself collapses. But South Africa is not only debating efficiency. It is also debating:
- justice,
- ownership,
- race,
- dignity,
- belonging,
- and historical repair. The DA is strongest when people fear collapse.
Its biggest challenge is convincing voters that competence can also produce justice.
""", youth_appeal=6, ) add_policy( da, "Governance", "The capable state", """
The DA argues that South Africa cannot solve unemployment, poverty, crime, or failing services without rebuilding the state itself.
""", """
The deeper argument here is that institutional collapse produces social collapse. For the DA:
- corruption destroys opportunity,
- broken municipalities destroy dignity,
- and weak administration destroys growth.
""", """
Supporters believe competent governance is the foundation for all other progress.
""", """
Critics argue competent administration alone cannot solve structural inequality.
""", """
Taxpayers, municipalities, commuters, students, businesses, poor communities and public-service users.
""", """
The DA's politics becomes strongest when public frustration with state collapse becomes visible in daily life.
""" ) self.stdout.write( self.style.SUCCESS( "Seeded DA with deeper ideological analysis." ) ) 
