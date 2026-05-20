from django.core.management.base import BaseCommand
from core.models import Party, ManifestoPolicy


def add_policy(party, category, title, position, analysis, strengths, weaknesses, affected, commentary):
    ManifestoPolicy.objects.create(
        party=party,
        category=category,
        policy_title=title,
        manifesto_position=position,
        simplified_explanation=analysis,
        possible_advantages=strengths,
        possible_concerns=weaknesses,
        affected_groups=affected,
        yoh_analysis=commentary,
    )


def reset_party(abbreviation):
    Party.objects.filter(abbreviation=abbreviation).delete()


class Command(BaseCommand):
    help = "Seed additional South African political parties"

    def handle(self, *args, **kwargs):

        # ANC
        reset_party("ANC")
        anc = Party.objects.create(
            name="African National Congress",
            abbreviation="ANC",
            leader="Cyril Ramaphosa",
            founded="1912",
            ideology="Social democracy, liberation movement politics, developmental state",
            political_position="Centre-left",
            short_explainer="The ANC remains the central party of post-apartheid South Africa. Its political offer is built around transformation, social protection, public investment, and the claim that it is still the main vehicle for completing the democratic project.",
            historical_context="",
            political_identity="The ANC presents itself as both a liberation movement and a governing party. It argues that South Africa's democracy, Constitution, social grants, housing delivery, and transformation policies are rooted in its historic role.",
            economic_approach="The ANC supports a mixed economy with strong state involvement, industrial policy, infrastructure investment, social spending, and transformation through BEE and public procurement.",
            social_approach="The ANC emphasises social grants, public healthcare, education access, housing, transformation, and protection of vulnerable groups.",
            governance_style="The ANC speaks the language of a developmental state, but its record is heavily contested because of corruption, cadre deployment, weak municipalities, and state-owned enterprise failures.",
            youth_relevance="Young people may recognise the ANC's historical importance but may also associate it with unemployment, corruption, load-shedding, and slow change.",
            major_support_base="Older voters, rural communities, working-class voters, public sector-aligned constituencies, liberation movement loyalists, and some grant-dependent households.",
            common_criticisms="""
Supporters argue that the ANC built democratic South Africa and remains the party most committed to social protection, racial transformation, and correcting apartheid's legacy.

Critics argue that the ANC has become too closely associated with corruption, cadre deployment, failing municipalities, unemployment, and state collapse. For many young voters, the ANC is no longer judged mainly by its liberation history, but by the lived experience of broken services.

The central debate around the ANC is whether it can renew itself from within, or whether the very party that built democratic South Africa has become one of the biggest obstacles to its next stage.
""",
            yoh_commentary="The ANC's tragedy is that it carries both historic achievement and present disappointment. Its story is not simple: it built much of the democratic state, but also presided over many of its deepest failures.",
            youth_appeal=5,
        )

        add_policy(
            anc, "Governance", "Renewal, corruption, and the struggle to rebuild trust",
            "The ANC speaks about renewal, fighting corruption, and improving the capability of the state.",
            "This is the ANC trying to convince voters that its failures are fixable from inside the movement.",
            "If serious, renewal could improve government capacity, restore trust, and stabilise public institutions.",
            "Many voters are sceptical because renewal has been promised before while corruption and poor performance continued.",
            "Public servants, municipalities, taxpayers, poor communities, businesses, and young voters.",
            "The ANC does not only need new promises. It needs proof that it can discipline itself."
        )

        add_policy(
            anc, "Social Support", "Social grants and the politics of survival",
            "The ANC supports continued social protection for poor and vulnerable households.",
            "Social grants are one of the ANC's strongest links to poor communities because they provide direct survival support.",
            "They reduce extreme poverty and support households where unemployment is high.",
            "Grants do not solve unemployment and can become politically fragile if not linked to economic opportunity.",
            "Grant recipients, children, pensioners, unemployed households, caregivers, and taxpayers.",
            "In South Africa, grants are not laziness. They are often what keeps families alive. The deeper issue is why so many households still need them."
        )

        add_policy(
            anc, "Land / Property / Transformation", "Transformation through the state",
            "The ANC supports transformation through BEE, land reform, public procurement, and state-led development.",
            "The ANC believes the state must correct apartheid's economic legacy, but usually through gradual reform rather than EFF-style rupture.",
            "Could support black ownership, public investment, and inclusion in the formal economy.",
            "Critics argue transformation has often benefited politically connected elites more than ordinary people.",
            "Black entrepreneurs, workers, rural communities, politically connected firms, taxpayers, and excluded youth.",
            "The ANC's transformation problem is not the idea of transformation. It is whether transformation reaches the many or enriches the few."
        )

        # MK
        reset_party("MK")
        mk = Party.objects.create(
            name="uMkhonto weSizwe Party",
            abbreviation="MK",
            leader="Jacob Zuma",
            founded="2023",
            ideology="Populism, African nationalism, constitutional reform politics",
            political_position="Populist nationalist",
            short_explainer="The MK Party emerged as one of the most disruptive forces in South African politics, drawing support from voters angry at the ANC, loyal to Jacob Zuma, and frustrated with the post-1994 settlement.",
            historical_context="",
            political_identity="MK politics is built around anti-establishment anger, Zuma-aligned mobilisation, cultural identity, and the argument that the current constitutional order has failed many South Africans.",
            economic_approach="The party leans toward state intervention, redistribution, and stronger nationalist control over economic policy.",
            social_approach="MK appeals to identity, tradition, dignity, and anger at political elites. It speaks strongly to voters who feel betrayed by the ANC and ignored by mainstream politics.",
            governance_style="MK's style is populist, confrontational, personality-driven, and deeply tied to Jacob Zuma's political brand.",
            youth_relevance="Some young people may see MK as a protest vehicle against the ANC and economic exclusion. Others may reject it as too tied to old political battles.",
            major_support_base="Zuma loyalists, KwaZulu-Natal voters, disillusioned ANC supporters, traditionalist voters, and anti-establishment constituencies.",
            common_criticisms="""
Supporters argue that MK gives voice to people who feel betrayed by the ANC and excluded by the post-1994 political order. They see it as a correction to a system that promised freedom but delivered poverty and humiliation.

Critics argue that MK is too personality-driven and too closely linked to Jacob Zuma's political controversies. They worry that its rise is driven more by grievance and loyalty than by a clear governing programme.

The central debate around MK is whether it represents a genuine new political force, or whether it is mainly a revolt inside the ANC's historical support base.
""",
            yoh_commentary="MK is important because it shows that ANC decline does not automatically benefit liberal opposition politics. Anger can move in nationalist, populist, and identity-driven directions too.",
            youth_appeal=6,
        )

        add_policy(
            mk, "Governance", "Constitutional frustration and anti-establishment politics",
            "MK questions the existing political order and speaks to voters who believe the current system has failed.",
            "This is not just policy; it is a challenge to the legitimacy of the post-1994 settlement.",
            "Could force national debate about accountability, traditional authority, and whether institutions serve ordinary people.",
            "Could weaken constitutional stability if criticism becomes anti-institutional rather than reformist.",
            "Disillusioned voters, traditional leaders, courts, Parliament, young voters, and communities angry at government failure.",
            "MK's rise says something bigger than one party: many people do not feel protected by the system they were told to trust."
        )

        # IFP
        reset_party("IFP")
        ifp = Party.objects.create(
            name="Inkatha Freedom Party",
            abbreviation="IFP",
            leader="Velenkosini Hlabisa",
            founded="1975",
            ideology="Conservatism, federalism, traditional leadership, social democracy elements",
            political_position="Centre-right conservative",
            short_explainer="The IFP is a long-standing South African party rooted strongly in KwaZulu-Natal politics, traditional leadership, federalism, community stability, and cautious governance.",
            historical_context="",
            political_identity="The IFP combines Zulu cultural identity, traditional leadership, decentralisation, social stability, and anti-corruption messaging.",
            economic_approach="The IFP generally supports development, local economic growth, infrastructure, agriculture, and practical service delivery rather than radical economic restructuring.",
            social_approach="The party emphasises family, community, traditional authority, safety, social support, and respect for cultural institutions.",
            governance_style="The IFP presents itself as disciplined, community-rooted, experienced, and less chaotic than newer populist movements.",
            youth_relevance="Young people may connect with the IFP through local service delivery, safety, education, and identity, especially in KwaZulu-Natal.",
            major_support_base="KwaZulu-Natal voters, traditional communities, conservative voters, rural communities, and voters loyal to the IFP's historical role.",
            common_criticisms="""
Supporters argue that the IFP understands local communities, traditional leadership, rural life, and KwaZulu-Natal politics better than many national parties.

Critics argue that the IFP can feel too regionally concentrated and too tied to older forms of politics, making it harder to appeal to urban youth looking for bold national change.

The central debate around the IFP is whether rooted community politics is a strength in a fragmented South Africa, or whether the country needs a more nationally expansive political imagination.
""",
            yoh_commentary="The IFP reminds us that South African politics is not only national television debates. It is also rural authority, local identity, municipal trust, and community memory.",
            youth_appeal=5,
        )

        add_policy(
            ifp, "Governance", "Decentralisation and local accountability",
            "The IFP favours stronger local and provincial authority and practical service delivery.",
            "The party believes communities should have more direct control over development and governance.",
            "Could make government more responsive to local needs.",
            "Can become uneven if local institutions lack capacity or become captured by local elites.",
            "Rural communities, municipalities, traditional leaders, provincial governments, and local businesses.",
            "Local government is where politics becomes real. Water, roads, clinics, and safety are not abstract ideology."
        )

        # GOOD
        reset_party("GOOD")
        good = Party.objects.create(
            name="GOOD",
            abbreviation="GOOD",
            leader="Patricia de Lille",
            founded="2018",
            ideology="Social democracy, spatial justice, anti-poverty reform",
            political_position="Centre-left",
            short_explainer="GOOD positions itself as a social justice party focused on poverty, spatial inequality, land, housing, public transport, and ethical government.",
            historical_context="",
            political_identity="GOOD's politics focuses on dignity, fairness, anti-corruption, and correcting spatial apartheid through housing, transport, and social policy.",
            economic_approach="GOOD supports inclusive growth, anti-poverty measures, public investment, and a stronger role for government in correcting inequality.",
            social_approach="The party emphasises housing, land access, public transport, gender justice, and reducing inequality in daily life.",
            governance_style="GOOD presents itself as pragmatic, reformist, and anti-corruption, with Patricia de Lille's political brand central to its identity.",
            youth_relevance="Young people may connect with GOOD through housing, transport, land access, and urban inequality issues.",
            major_support_base="Urban voters, social justice voters, anti-corruption voters, and communities concerned with housing and spatial exclusion.",
            common_criticisms="""
Supporters argue that GOOD focuses on the everyday geography of inequality: where people live, how far they travel, what transport costs, and whether cities are designed for poor people.

Critics argue that GOOD remains too small and too dependent on Patricia de Lille's personal brand, raising questions about long-term national reach.

The central debate around GOOD is whether smaller reformist parties can meaningfully reshape South Africa, or whether they become coalition accessories to larger parties.
""",
            yoh_commentary="GOOD's strongest contribution is spatial justice. It reminds voters that apartheid did not only create racial inequality; it designed where people live, work, travel, and struggle.",
            youth_appeal=5,
        )

        add_policy(
            good, "Land / Property / Transformation", "Spatial justice and the city",
            "GOOD emphasises land, housing, and spatial inequality as central democratic issues.",
            "The party wants politics to focus on how apartheid geography still shapes opportunity.",
            "Could improve access to housing, transport, and urban opportunity.",
            "Housing reform is expensive and politically difficult, especially in cities with high land values.",
            "Backyard dwellers, young workers, commuters, informal settlement residents, municipalities, and landlords.",
            "Where you live decides how much of your life is spent waiting, travelling, and surviving."
        )

        # RISE
        reset_party("RISE")
        rise = Party.objects.create(
            name="RISE Mzansi",
            abbreviation="RISE",
            leader="Songezo Zibi",
            founded="2023",
            ideology="Social democracy, civic reform, anti-corruption, democratic renewal",
            political_position="Centre-left reformist",
            short_explainer="RISE Mzansi presents itself as a new civic-minded party focused on leadership renewal, social justice, safety, jobs, and rebuilding public trust.",
            historical_context="",
            political_identity="RISE Mzansi's identity is reformist, civic, anti-corruption, youth-aware, and focused on building a new political culture beyond liberation nostalgia.",
            economic_approach="The party supports inclusive growth, job creation, public service repair, and economic participation for excluded communities.",
            social_approach="RISE focuses on safety, dignity, education, social justice, and making democracy feel meaningful for ordinary people.",
            governance_style="Its style is professional, civic-minded, values-driven, and focused on ethical leadership.",
            youth_relevance="RISE may appeal to young people who want change but do not feel represented by either old liberation politics or radical populism.",
            major_support_base="Urban reform-minded voters, young professionals, civil society voters, anti-corruption voters, and politically homeless citizens.",
            common_criticisms="""
Supporters argue that RISE Mzansi represents a serious attempt to build new politics: ethical, thoughtful, civic, and less trapped by old party wars.

Critics argue that the party may sound good to educated urban voters but still needs to prove deep grassroots reach and governing capacity.

The central debate around RISE is whether South Africa is ready for a values-driven civic reform party, or whether politics is still too shaped by identity, history, and material survival.
""",
            yoh_commentary="RISE speaks to politically tired South Africans who want seriousness without nostalgia, anger without recklessness, and reform without arrogance.",
            youth_appeal=7,
        )

        add_policy(
            rise, "Youth", "Political renewal and a new generation of leadership",
            "RISE positions political renewal as central to fixing South Africa.",
            "The party argues that the crisis is not only policy failure but leadership failure.",
            "Could attract voters tired of old scandals, old loyalties, and old political language.",
            "Newness alone does not guarantee capacity, organisation, or mass support.",
            "Young voters, civil society, professionals, first-time voters, and disillusioned citizens.",
            "Many young people do not just want a new party. They want a new political culture."
        )

        # FF Plus
        reset_party("FF+")
        ff = Party.objects.create(
            name="Freedom Front Plus",
            abbreviation="FF+",
            leader="Pieter Groenewald",
            founded="1994",
            ideology="Minority rights, conservatism, federalism, property rights",
            political_position="Right-wing conservative",
            short_explainer="The FF Plus focuses on minority rights, property rights, federalism, language rights, community autonomy, and opposition to race-based policy.",
            historical_context="",
            political_identity="The FF Plus represents conservative minority politics, especially around Afrikaner interests, language, culture, property rights, and decentralised power.",
            economic_approach="The party supports market economics, property protection, lower state interference, and opposition to policies it sees as racialised or punitive.",
            social_approach="It emphasises cultural rights, community self-determination, language protection, and conservative social values.",
            governance_style="The FF Plus favours decentralisation, community autonomy, and limiting central state power.",
            youth_relevance="Young people may engage with the FF Plus through debates on language, universities, property rights, minority identity, and affirmative action.",
            major_support_base="Afrikaans-speaking voters, minority rights voters, conservative voters, farmers, and people opposed to race-based policy.",
            common_criticisms="""
Supporters argue that the FF Plus protects communities who feel ignored or targeted by majoritarian politics. They see it as a necessary voice for language rights, property rights, and decentralisation.

Critics argue that the party can appear too focused on minority anxiety and insufficiently responsive to black poverty, historical dispossession, and broader transformation.

The central debate around the FF Plus is whether minority protection strengthens democracy, or whether it can become a way of resisting necessary redress.
""",
            yoh_commentary="The FF Plus forces South Africa to confront a difficult democratic question: how do you protect minority rights while still transforming a deeply unequal society?",
            youth_appeal=4,
        )

        add_policy(
            ff, "Land / Property / Transformation", "Property rights and minority protection",
            "The FF Plus strongly defends property rights and opposes expropriation without compensation.",
            "The party sees property rights as essential to stability, investment, farming, and minority protection.",
            "Could reassure property owners, farmers, and investors.",
            "May be seen as too defensive in a country still shaped by land dispossession.",
            "Farmers, property owners, investors, rural workers, landless communities, and minority groups.",
            "This debate is one of South Africa's hardest: security of ownership versus justice for dispossession."
        )

        # Patriotic Alliance
        reset_party("PA")
        pa = Party.objects.create(
            name="Patriotic Alliance",
            abbreviation="PA",
            leader="Gayton McKenzie",
            founded="2013",
            ideology="Populism, patriotism, law and order, coloured community advocacy",
            political_position="Populist conservative",
            short_explainer="The Patriotic Alliance presents itself as a tough, patriotic, community-focused party with strong messaging on crime, immigration, service delivery, and coloured community representation.",
            historical_context="",
            political_identity="The PA mixes populist leadership, law-and-order politics, patriotic language, anti-illegal-immigration messaging, and direct appeals to communities that feel ignored.",
            economic_approach="The PA speaks about jobs, local opportunity, small business, and using government power to deliver quickly.",
            social_approach="The party strongly emphasises crime, drugs, community safety, border control, and dignity for coloured communities.",
            governance_style="The PA's style is direct, personality-driven, populist, and focused on visible action.",
            youth_relevance="Young people may connect with its blunt language on crime, drugs, unemployment, and community neglect, especially in areas that feel abandoned.",
            major_support_base="Coloured communities, anti-crime voters, populist voters, anti-illegal-immigration voters, and people drawn to Gayton McKenzie's leadership style.",
            common_criticisms="""
Supporters argue that the PA says what many communities are afraid to say publicly: that crime, drugs, unemployment, and illegal immigration are destroying neighbourhoods.

Critics argue that the PA's politics can become too personality-driven and too harsh toward migrants. They worry that simple slogans can hide complex social and economic problems.

The central debate around the PA is whether blunt populist politics gives ignored communities a voice, or whether it risks turning pain into scapegoating.
""",
            yoh_commentary="The PA understands political emotion. It speaks to anger, fear, pride, and neglect. The question is whether that emotional connection can become responsible governance.",
            youth_appeal=6,
        )

        add_policy(
            pa, "Crime", "Drugs, gangs, and community fear",
            "The PA places strong emphasis on crime, drugs, gangs, and safer communities.",
            "The party frames safety as the first condition for dignity and opportunity.",
            "Could appeal strongly in communities where crime shapes daily life.",
            "Hardline crime politics can fail if it does not address poverty, addiction, policing corruption, and youth exclusion.",
            "Young men, families, schools, township communities, coloured communities, police, and local businesses.",
            "Crime politics is powerful because fear is immediate. But safety needs more than toughness; it needs prevention, opportunity, and trust."
        )

        self.stdout.write(self.style.SUCCESS("Seeded ANC, MK, IFP, GOOD, RISE, FF Plus and PA."))
