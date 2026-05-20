from django.core.management.base import BaseCommand
from core.models import Party, ManifestoPolicy


class Command(BaseCommand):
    help = "Seed EFF party data"


    def handle(self, *args, **kwargs):

        party, created = Party.objects.update_or_create(
            slug="eff",
            defaults={
                "name": "Economic Freedom Fighters",
                "abbreviation": "EFF",
                "political_position": "Far-left",
                "ideology": "Revolutionary socialism, economic emancipation, state-led redistribution",
                "short_explainer": "The EFF argues that political freedom without economic ownership is incomplete. Its message centres land redistribution, jobs, state ownership, industrialisation, anti-corruption politics, and economic justice.",
                "political_identity": "The EFF presents itself as a revolutionary movement fighting economic apartheid. It argues that political democracy in South Africa did not fundamentally change ownership of land, wealth, industry, and economic power.",
                "society_vision": "The EFF imagines a South Africa where land, mines, banks, and strategic sectors are controlled in ways that benefit the black majority. It believes economic power must shift dramatically away from existing concentrations of wealth.",
                "economic_approach": "The EFF supports state-led industrialisation, nationalisation of strategic sectors, stronger state capacity, localisation, labour absorption, and aggressive economic redistribution. The party believes the market alone cannot solve inequality or unemployment.",
                "equality_view": "The EFF sees race, land ownership, wealth inequality, and economic exclusion as central political questions. It believes structural redistribution is necessary to undo apartheid-era economic patterns.",
                "immigration_view": "The EFF generally frames migration within broader African solidarity politics, although critics argue that tensions sometimes emerge between pan-African rhetoric and pressures around unemployment and local frustration.",
                "crime_view": "The EFF supports stronger policing and state intervention against violent crime, corruption, gangsterism, and economic crimes. It also argues that poverty and inequality contribute heavily to criminality.",
                "governance_style": "The EFF uses confrontational, populist, activist-style politics. It positions itself as disruptive, anti-establishment, youth-driven, and impatient with slow reform.",
                "historical_context": "The EFF was founded in 2013 after a split from the ANC Youth League. It emerged during growing frustration around unemployment, corruption, inequality, student debt, land reform, and youth exclusion.",
                "yoh_commentary": "The EFF's politics are emotionally powerful because they speak directly to anger, exclusion, inequality, and unfinished liberation. Its supporters see urgency and justice. Its critics worry about feasibility, institutional stability, and economic risk.",
                "youth_appeal": 9,
            }
        )

        ManifestoPolicy.objects.filter(party=party).delete()

        policies = [

            {
                "category": "Land",
                "policy_title": "Expropriation of land without compensation",
                "manifesto_position": "The EFF supports expropriation of land without compensation and argues that the state should become custodian of all land in South Africa.",
                "simplified_explanation": "The party believes land ownership patterns remain deeply unequal and that major redistribution is necessary.",
                "affected_groups": "Landless communities, rural residents, farmers, agricultural workers, property owners, and municipalities.",
                "possible_advantages": "Could accelerate redistribution and expand access to land for housing, farming, and economic participation.",
                "possible_concerns": "Critics worry about agricultural disruption, legal uncertainty, investment fears, and implementation capacity.",
                "yoh_analysis": "Land is the emotional centre of the EFF project. The party argues that freedom without land ownership is incomplete."
            },

            {
                "category": "Jobs",
                "policy_title": "Massive state-led job creation",
                "manifesto_position": "The EFF promises large-scale industrialisation, localisation, public infrastructure, and state companies to create millions of jobs.",
                "simplified_explanation": "The party believes government must directly drive economic growth and employment instead of relying mainly on private markets.",
                "affected_groups": "Unemployed youth, graduates, workers, township economies, SMMEs, and industrial sectors.",
                "possible_advantages": "Could create employment through infrastructure, manufacturing, and expanded state investment.",
                "possible_concerns": "Would require major state capacity, large budgets, and efficient governance to avoid corruption or waste.",
                "yoh_analysis": "The EFF speaks directly to unemployed people who feel abandoned by the economy. Jobs are not just economic in this manifesto. They are political dignity."
            },

            {
                "category": "Energy",
                "policy_title": "State-controlled electricity expansion",
                "manifesto_position": "The EFF supports expanding Eskom, repairing generation capacity, investing in energy infrastructure, and opposing full privatisation.",
                "simplified_explanation": "The party argues that electricity is too important to be left mainly to private interests.",
                "affected_groups": "Households, businesses, municipalities, workers, and industrial sectors.",
                "possible_advantages": "Could strengthen long-term state energy planning and infrastructure coordination.",
                "possible_concerns": "Large energy investment programmes require stable management and significant technical expertise.",
                "yoh_analysis": "The EFF treats loadshedding as proof that the state has lost strategic control over development."
            },

            {
                "category": "Education",
                "policy_title": "Free quality education",
                "manifesto_position": "The EFF supports free education, expanded student support, insourcing of workers, and broader access to higher education.",
                "simplified_explanation": "The party argues that poor students should not be excluded from education because of money.",
                "affected_groups": "Students, universities, families, academic workers, and graduates.",
                "possible_advantages": "Could improve educational access and reduce exclusion for working-class students.",
                "possible_concerns": "Funding universal higher education sustainably would require major fiscal planning.",
                "yoh_analysis": "The EFF's student politics helped shape a generation of politically active youth who connected education directly to inequality."
            },

            {
                "category": "Economy",
                "policy_title": "Nationalisation of strategic sectors",
                "manifesto_position": "The EFF supports state ownership of mines, banks, and strategic economic sectors.",
                "simplified_explanation": "The party believes key industries should benefit the majority instead of concentrating wealth in a few hands.",
                "affected_groups": "Mining companies, financial institutions, workers, investors, and the broader economy.",
                "possible_advantages": "Could allow greater state control over national resources and developmental planning.",
                "possible_concerns": "Critics fear inefficiency, investor flight, corruption risks, and fiscal instability.",
                "yoh_analysis": "This is where the EFF becomes most polarising. Supporters see justice and sovereignty. Critics see economic danger."
            }

        ]

        for item in policies:
            ManifestoPolicy.objects.create(
                party=party,
                **item
            )

        self.stdout.write(self.style.SUCCESS("EFF seeded successfully"))
