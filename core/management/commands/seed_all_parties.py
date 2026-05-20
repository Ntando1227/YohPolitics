from django.core.management.base import BaseCommand
from core.models import Party, ManifestoPolicy def add_policy(party, category, title, position, analysis, strengths, weaknesses, affected, commentary): ManifestoPolicy.objects.create( party=party, category=category, policy_title=title, manifesto_position=position, simplified_explanation=analysis, possible_advantages=strengths, possible_concerns=weaknesses, affected_groups=affected, yoh_analysis=commentary, ) def create_party(**kwargs): return Party.objects.create(**kwargs) class Command(BaseCommand): help = "Seed all Yoh Politics parties with richer civic journalism and ideological analysis" def handle(self, *args, **kwargs): ManifestoPolicy.objects.all().delete() Party.objects.all().delete() # ===================================================== # DA # ===================================================== da = create_party( name="Democratic Alliance", abbreviation="DA", leader="John Steenhuisen", founded="2000", ideology="Liberal democracy, constitutionalism, market-oriented reform", political_position="Centre to centre-right", short_explainer="""
The Democratic Alliance presents itself as the party of competent government, institutional repair, anti-corruption politics, economic growth, public safety, and constitutional democracy. Its central argument is that South Africa is not short of slogans, manifestos, speeches, or promises. It is short of a state that works. The DA therefore places capable government at the centre of almost every issue: jobs, crime, healthcare, education, infrastructure, energy, water, poverty, and investment.
""", historical_context="""
The DA comes from South Africa's liberal opposition tradition and became the country's largest opposition party in the democratic era. Its identity has been shaped by opposition to ANC dominance, corruption, cadre deployment, weak municipalities, load-shedding, and failing public institutions. The party often presents its record in places where it governs as proof that better administration can improve people's lives. At the same time, the DA has struggled with a recurring political challenge: many voters see it as competent but emotionally distant from the lived reality of black poverty, historical dispossession, and structural inequality.
""", political_identity="""
The DA is fundamentally a constitutional liberal party. Its politics is built around the belief that South Africa's democratic institutions must be protected, professionalised, and rescued from political capture. It believes that when the state is captured by party loyalty, corruption, and incompetence, ordinary people suffer first. For the DA, the central political enemy is not only poverty or inequality in the abstract. It is a broken state that can no longer deliver water, electricity, policing, healthcare, education, and economic confidence. This makes the DA a party of institutional repair. It wants to replace political loyalty with merit, cadre deployment with professionalism, and ideological slogans with measurable delivery.
""", society_vision="""
The DA imagines a South Africa where public institutions work reliably and predictably. In that society:
- municipalities maintain infrastructure,
- schools teach children to read,
- clinics and hospitals treat patients with dignity,
- police respond to crime,
- corruption is punished,
- businesses invest,
- and citizens are not dependent on political connections to receive basic services. This vision is less revolutionary than managerial. The DA is not trying to completely redesign society through state ownership or radical redistribution. It wants to make the existing democratic and economic system function better, more fairly, and more efficiently. Its ideal society is rules-based, economically productive, administratively clean, and institutionally stable.
""", economic_approach="""
The DA's economic worldview is market-oriented but not completely anti-state. It believes economic growth comes from:
- investment confidence,
- reliable electricity,
- working ports and rail,
- lower corruption,
- less red tape,
- safer communities,
- better education,
- and a capable state. The DA generally trusts businesses, entrepreneurs, and investors more than state-owned companies as engines of job creation. It does not believe the government should directly control most sectors of the economy. Its critics argue that this approach may protect existing wealth patterns and move too slowly for people who are landless, unemployed, and excluded. Its supporters argue that without growth, stability, and investment, redistribution becomes impossible to sustain.
""", equality_view="""
The DA tends to understand equality through opportunity rather than aggressive redistribution. It argues that people become more equal when they have:
- quality education,
- safe communities,
- working municipalities,
- access to jobs,
- economic growth,
- and fair institutions. This differs sharply from parties that see equality mainly through land, ownership, race, and wealth redistribution. The DA does support redress, but it is uncomfortable with policies it believes create dependency, racial patronage, corruption, or elite enrichment. The criticism is that opportunity is not neutral in an unequal society. If some communities inherit land, networks, capital, safety, and good schools, while others inherit distance, debt, violence, and broken institutions, then simply saying "opportunity" may not be enough.
""", immigration_view="""
The DA generally treats immigration as a governance and documentation issue. It supports lawful immigration, better border systems, proper documentation, stronger Home Affairs capacity, and consequences for corruption in immigration administration. However, it usually avoids the more aggressive anti-immigrant tone used by parties such as ActionSA or the Patriotic Alliance. The DA's view is that the state must know who is in the country, who has legal status, who may work, who qualifies for services, and how migration is managed. Its critics from the right may say it is too soft. Critics from the left may say even moderate immigration language can become dangerous when unemployment and poverty are high.
""", crime_view="""
The DA treats crime as a crisis of freedom. Its argument is that people are not truly free if they cannot:
- walk safely,
- run a business,
- take public transport,
- attend evening classes,
- report abuse,
- or trust the police. The DA links crime to weak policing, poor prosecution, corruption, under-resourced detectives, broken intelligence systems, and failing courts. Its solution is institutional: professionalise policing, strengthen prosecution, reduce political interference, improve crime intelligence, and build trust in the justice system.
""", social_approach="""
The DA's social approach focuses on service delivery and institutional fairness. It supports social welfare and poverty relief, but it usually frames long-term dignity around jobs, education, safety, and functioning services. Its social policy is shaped by the idea that poor people are harmed most when public systems collapse. The DA's weakness is that this language can sound technical in a country where inequality is emotional, historical, racial, and deeply personal.
""", governance_style="""
The DA's governance style is technocratic, managerial, audit-driven, and institution-focused. It values:
- clean audits,
- measurable performance,
- professional appointments,
- stable finances,
- anti-corruption systems,
- and service delivery indicators. This style appeals to voters who are tired of chaos, corruption, and failing municipalities. But it can also sound cold to voters who want politics to speak more directly about land, race, pain, dignity, and historical injustice.
""", youth_relevance="""
Young people may connect with the DA because it speaks to issues that shape daily life:
- unemployment,
- bad schools,
- crime,
- load-shedding,
- poor public transport,
- corruption,
- and failing municipalities. But younger voters may also ask whether DA-style reform is bold enough for a generation facing extreme unemployment, unaffordable housing, student debt, and inherited inequality. For politically restless youth, the DA can feel competent but not emotionally radical enough.
""", major_support_base="""
The DA tends to appeal to urban voters, middle-class voters, professionals, business owners, some minority communities, governance-focused citizens, and people frustrated by corruption and poor service delivery.
""", common_criticisms="""
Supporters argue that the DA is the most credible party on governance. They see it as disciplined, practical, institutionally serious, and capable of running municipalities and provinces better than most competitors. Critics argue that the DA struggles to speak convincingly about black historical pain, landlessness, wealth inequality, and structural racial exclusion. Its language of merit, markets, and clean governance can sound sensible to the middle class but distant to people who want deeper transformation. The central debate around the DA is this: can South Africa fix poverty and inequality through competence, growth, and institutional repair, or does that approach leave the deeper ownership structure of the country untouched?
""", yoh_commentary="""
The DA is strongest when South Africans are exhausted by collapse. Its message is powerful because water outages, corruption, load-shedding, crime, bad roads, and failing clinics are not abstract. They are daily humiliations. But South Africa is not only asking, "Who can manage better?" It is also asking:
Who owns?
Who was dispossessed?
Who waits?
Who travels far?
Who gets protected?
Who gets believed?
Who gets rescued first? That is the DA's big challenge: proving that clean government can also deliver deep justice.
""", youth_appeal=6, ) add_policy( da, "Governance", "The capable state as the DA's main political argument", "The DA argues that South Africa cannot solve unemployment, poverty, crime, education failure, healthcare collapse, or infrastructure breakdown without first rebuilding the state itself.", "The deeper political argument is that corruption and cadre deployment do not only waste money. They destroy the basic machinery through which justice, development, and opportunity are supposed to happen.", "A capable state could improve municipalities, policing, hospitals, schools, water systems, procurement, and public trust.", "Critics argue that a capable state is necessary but not sufficient. It may improve delivery without changing deeper patterns of ownership, land, wealth, and class power.", "Municipal residents, taxpayers, public servants, poor communities, businesses, school learners, patients, commuters, and jobseekers.", "The DA's politics becomes most convincing when people feel the state failing in ordinary life. Its weakness is that fixing the machine does not automatically answer who the machine was built to serve." ) add_policy( da, "Employment", "Jobs through growth rather than mass state employment", "The DA links job creation to investment, energy security, infrastructure, private-sector confidence, skills, and less corruption.", "This approach treats employment as the outcome of a functioning economy. The DA believes that when businesses can operate safely and predictably, they are more likely to hire.", "Could create more sustainable jobs if growth spreads widely and if small businesses are supported properly.", "The risk is that growth may remain concentrated in cities, formal sectors, and already-connected communities.", "Young jobseekers, graduates, township entrepreneurs, small businesses, investors, workers, and households.", "The youth question is not only, 'Will the economy grow?' It is, 'Will that growth reach people without networks, capital, transport, or family safety nets?'" ) # ===================================================== # EFF # ===================================================== eff = create_party( name="Economic Freedom Fighters", abbreviation="EFF", leader="Julius Malema", founded="2013", ideology="Marxism-Leninism, Pan-Africanism, radical economic transformation", political_position="Left-wing", short_explainer="""
The EFF argues that South Africa's political freedom did not become economic freedom. Its manifesto is built around land, jobs, electricity, ownership, free education, public healthcare, state capacity, and the belief that the post-1994 settlement left the economic structure of apartheid largely intact.
""", historical_context="""
The EFF was formed in 2013 and quickly became the loudest parliamentary voice for radical economic transformation. It positioned itself as a generational rebellion against both the ANC's slow transformation and the DA's liberal reformism. Its politics is shaped by the claim that South Africa changed politically in 1994, but not economically. For the EFF, the black majority gained the vote but not land, mines, banks, factories, or meaningful ownership.
""", political_identity="""
The EFF is a radical economic transformation movement. It sees South Africa as a country where colonialism and apartheid continue through land ownership, wealth concentration, unemployment, racialised poverty, and control of the economy. The party believes the state must actively restructure society. This means:
- expropriating land without compensation,
- nationalising mines and banks,
- expanding public services,
- creating state-led jobs,
- protecting workers,
- and using government power to change ownership patterns. The EFF is not trying to soften capitalism. It wants to confront it.
""", society_vision="""
The EFF imagines a South Africa where wealth, land, and opportunity are redistributed more aggressively. Its ideal society is:
- black-led,
- African-centred,
- economically redistributive,
- state-driven,
- and committed to material equality. The EFF does not believe South Africa's current economy can be made fair through small adjustments. It argues that the existing structure was built through conquest, dispossession, and racial capitalism. Therefore, justice requires structural change, not only better management.
""", economic_approach="""
The EFF's economic approach is state-led and redistributive. It supports:
- land expropriation without compensation,
- nationalisation of mines and banks,
- industrialisation,
- localisation,
- public employment,
- expanded state capacity,
- free education,
- and stronger worker protections. The EFF believes the state must take control of strategic sectors so that national wealth serves the majority. Critics worry about investor flight, corruption, state capacity, public finances, and food security. Supporters argue that markets have already failed the majority and that stability without justice is simply organised exclusion.
""", equality_view="""
For the EFF, equality is about ownership. The party rejects the idea that legal equality is enough when most black people remain landless, unemployed, indebted, and excluded from economic power. It believes true equality requires:
- land redistribution,
- public ownership,
- free education,
- worker power,
- state-led development,
- and direct confrontation with racialised wealth. This makes the EFF very different from parties that focus on opportunity or service delivery. The EFF asks: opportunity to enter whose economy, on whose terms, and from what starting point?
""", immigration_view="""
The EFF generally presents itself as pan-African and anti-xenophobic. It often argues that migrants are not the real cause of unemployment, crime, or poverty. Instead, it points to capitalism, corruption, weak borders, poor planning, and economic inequality. This does not mean immigration is politically easy for the EFF. Many of its supporters live in communities where jobs, housing, clinics, and informal trading spaces are under pressure. The party therefore tries to balance African solidarity with domestic frustration.
""", crime_view="""
The EFF links crime to economic exclusion and social collapse. Its argument is that violent crime cannot be separated from:
- unemployment,
- drugs,
- poverty,
- broken schools,
- weak policing,
- inequality,
- and hopelessness. The party supports public safety, but it does not usually frame crime only as individual moral failure. For the EFF, crime is also a symptom of a society that has abandoned millions of people economically.
""", social_approach="""
The EFF's social approach is expansive and rights-based. It supports:
- free education,
- public healthcare,
- housing,
- sanitation,
- gender justice,
- LGBTQIA+ rights,
- disability rights,
- youth development,
- and social protection. But unlike moderate social democrats, the EFF ties these rights to a larger economic revolution. For the EFF, social justice without economic ownership is incomplete.
""", governance_style="""
The EFF's governance style is militant, confrontational, movement-driven, and activist. It uses political drama deliberately. Parliament, protest, courts, media, and public confrontation are all part of its political method. Supporters see this as necessary disruption in a country that ignores polite suffering. Critics see it as instability, intimidation, and performative politics.
""", youth_relevance="""
The EFF has strong youth appeal because it speaks to:
- unemployment,
- student debt,
- landlessness,
- exclusion,
- racial inequality,
- unaffordable education,
- and anger at slow transformation. It gives political language to young people who feel democracy has not delivered material dignity. For many young supporters, the EFF does not sound extreme. It sounds honest.
""", major_support_base="""
The EFF appeals to students, unemployed youth, township residents, working-class communities, radical intellectuals, young professionals frustrated by inequality, and voters who want faster economic transformation.
""", common_criticisms="""
Supporters argue that the EFF says what many excluded South Africans feel: freedom without land, jobs, ownership, and dignity is incomplete. Critics argue that the EFF's programme could create economic instability, weaken property rights, scare investors, damage food security, and place too much power in a state that already struggles with corruption and capacity. The central debate around the EFF is whether South Africa can achieve justice through gradual reform, or whether the economy is so unequal that only radical redistribution can change people's lives.
""", yoh_commentary="""
The EFF is powerful because it refuses to treat inequality as unfortunate. It treats inequality as designed. That is why its politics hits emotionally. It tells the unemployed graduate, the landless family, the indebted student, and the township youth that their suffering is political, not personal failure. Its challenge is equally serious:
Can a state that currently struggles to fix potholes, corruption, and procurement be trusted to run mines, banks, land, and industrial policy at massive scale? The EFF asks the right moral question: who owns South Africa? Its hardest question is: who manages the transition?
""", youth_appeal=9, ) add_policy( eff, "Transformation", "Land, ownership, and unfinished freedom", "The EFF argues that real freedom requires changing who owns land, mines, banks, and productive assets.", "The deeper argument is that democracy without economic ownership leaves the majority politically included but economically trapped.", "Could force serious action on land, ownership, rural development, and economic inclusion.", "Could create instability if redistribution is badly planned, corruptly administered, or economically reckless.", "Landless communities, young people, farm workers, commercial farmers, banks, investors, traditional communities, and township households.", "The EFF makes land emotional because land is emotional. It is history, dignity, housing, food, memory, and power." ) add_policy( eff, "Employment", "Jobs through industrialisation and state power", "The EFF argues that unemployment will not be solved by waiting for private markets. It wants the state to actively build industries, direct procurement, protect workers, and create jobs.", "This is a direct challenge to market-led job creation. The EFF believes the state must shape the economy because the current economy excludes too many people by design.", "Could support local manufacturing, public employment, worker protections, and industrial expansion.", "Could fail if state capacity, corruption, procurement abuse, and weak planning undermine implementation.", "Unemployed youth, trade unions, factory workers, township economies, women-owned businesses, and local producers.", "The EFF's jobs message is powerful because it does not simply tell young people to become employable. It says the economy must be rebuilt to need them." ) # ===================================================== # ACTIONSA # ===================================================== actionsa = create_party( name="ActionSA", abbreviation="ActionSA", leader="Herman Mashaba", founded="2020", ideology="Reformism, anti-corruption politics, market-oriented social intervention", political_position="Centre-right", short_explainer="""
ActionSA presents itself as a party of urgency. Its message is direct: fix crime, fix corruption, support businesses, secure borders, improve education, rebuild services, and stop making excuses for government failure.
""", historical_context="""
ActionSA was formed by Herman Mashaba after his time as Mayor of Johannesburg. Its political brand grew from frustration with old parties, coalition instability, municipal dysfunction, crime, illegal immigration debates, and public anger at corruption. It positions itself as practical rather than ideological, although its politics clearly leans toward law and order, entrepreneurship, anti-corruption, and stricter border control.
""", political_identity="""
ActionSA is an action-oriented reform party. It does not present itself primarily as a party of theory. It presents itself as a party of execution. Its political identity is built around:
- urgency,
- visible delivery,
- anti-corruption,
- law and order,
- entrepreneurship,
- border control,
- and practical governance. It speaks to voters who are tired of hearing that problems are complicated and want government to act.
""", society_vision="""
ActionSA imagines a South Africa that is safer, cleaner, more orderly, more entrepreneurial, and less tolerant of corruption. Its ideal society is one where:
- criminals fear consequences,
- borders are managed,
- businesses can operate,
- informal traders are supported,
- corrupt officials are punished,
- and citizens see government acting visibly. It is not a revolutionary vision. It is a repair-and-discipline vision.
""", economic_approach="""
ActionSA's economy is built around entrepreneurship, small business, investment, infrastructure, and opportunity. It believes South Africa needs to make it easier for people to start and grow businesses. The party supports direct poverty support such as a Universal Basic Income Stimulus, but its broader economic imagination is entrepreneurial rather than socialist. It wants poor people to survive, but also to participate economically.
""", equality_view="""
ActionSA supports transformation but tries to frame equality differently from both the ANC and EFF. It talks about opportunity, entrepreneurship, education, targeted empowerment, and participation. Its approach is to say that people need access to tools, funding, education, infrastructure, and business opportunity rather than only symbolic representation. Critics argue that this may underplay the depth of structural inequality. Supporters argue that dignity comes from participation, ownership, and self-reliance.
""", immigration_view="""
Immigration is one of ActionSA's defining issues. The party strongly emphasises:
- border control,
- documentation,
- action against illegal immigration,
- and enforcement of immigration law. Supporters argue that weak border management places pressure on housing, clinics, schools, policing, jobs, and public trust. Critics argue that this politics can become too harsh and may risk blaming migrants for failures created by the South African state. This is one of the most sensitive parts of ActionSA's identity.
""", crime_view="""
ActionSA treats crime as an emergency. Its argument is that crime destroys everything:
- business,
- schooling,
- transport,
- nightlife,
- investment,
- community trust,
- and daily dignity. The party favours stronger policing, specialised units, anti-corruption bodies, and visible enforcement. Its tone is more forceful than many centrist parties, which helps explain its appeal in communities tired of fear.
""", social_approach="""
ActionSA combines social support with discipline. It supports income relief, education reform, healthcare access, and poverty reduction, but also places strong emphasis on responsibility, law enforcement, and economic participation. Its politics often says: help people, but also restore order.
""", governance_style="""
ActionSA's governance style is managerial, blunt, visible, and action-driven. It wants government to move quickly, punish corruption, enforce rules, and focus on practical outcomes. Its strength is urgency. Its weakness is that complex national problems often require slow institution-building, coalition management, and long-term planning.
""", youth_relevance="""
Young people may connect with ActionSA because it speaks to:
- unemployment,
- crime,
- entrepreneurship,
- bad schools,
- urban decay,
- and the cost of looking for work. Its challenge is immigration politics. Some young people may support its hard line. Others may see it as scapegoating vulnerable migrants.
""", major_support_base="""
ActionSA appeals to urban voters, entrepreneurs, anti-corruption voters, township business owners, middle-class voters, and people who feel old parties have failed.
""", common_criticisms="""
Supporters argue that ActionSA says what many people feel: South Africa is tired of excuses and needs visible action. Critics argue that the party can make complex problems sound too simple, especially around immigration, unemployment, and urban decay. The central debate is whether ActionSA's politics of urgency can become a serious national governing programme, or whether it works best as a protest against broken administration.
""", yoh_commentary="""
ActionSA understands frustration. It speaks to the person who is tired of being told to be patient while crime rises, businesses close, borders fail, and corruption continues. Its strongest message is: act now. Its biggest challenge is turning urgency into depth. National government is not only about being angry at failure. It requires institutions, budgets, coalitions, tradeoffs, and long-term capacity.
""", youth_appeal=7, ) add_policy( actionsa, "Youth Development", "Entrepreneurship, skills, and the cost of being unemployed", "ActionSA links youth development to entrepreneurship, skills, education reform, and direct income support.", "It recognises that unemployment is not free. Looking for work costs transport money, data, printing, food, time, and emotional energy.", "Could support young entrepreneurs, jobseekers, vocational pathways, and township business activity.", "Could underperform if support does not reach informal economies, rural youth, and young people without networks.", "Unemployed youth, TVET students, graduates, township entrepreneurs, informal traders, and poor households.", "ActionSA's youth message works because it understands that young people do not only need motivation. They need money, safety, skills, and openings." ) add_policy( actionsa, "Crime", "Safety, order, and the politics of fear", "ActionSA argues that South Africa cannot grow while citizens live under fear of crime, corruption, gangs, and lawlessness.", "The deeper argument is that safety is not only a policing issue. It is an economic issue, a youth issue, a gender issue, and a dignity issue.", "Could restore confidence in communities, support businesses, and improve everyday freedom.", "A hard-line safety agenda can fail if it does not also address poverty, addiction, policing corruption, and court backlogs.", "Women, commuters, young people, township businesses, families, schools, police, and courts.", "Crime politics is powerful because fear is immediate. But real safety requires both enforcement and prevention." ) # ===================================================== # ANC # ===================================================== anc = create_party( name="African National Congress", abbreviation="ANC", leader="Cyril Ramaphosa", founded="1912", ideology="Social democracy, liberation movement politics, developmental state", political_position="Centre-left", short_explainer="""
The ANC remains the central party of post-apartheid South Africa. Its political offer is built around liberation history, transformation, social grants, public investment, constitutional democracy, and the claim that it is still the most legitimate vehicle for completing the democratic project.
""", historical_context="""
The ANC led the liberation struggle and became South Africa's governing party in 1994. Its historic legitimacy comes from its role in defeating apartheid and building the democratic state. But after decades in power, the ANC is now judged not only by history, but by unemployment, corruption, load-shedding, weak municipalities, inequality, crime, and state failure. This makes the ANC both the party of democratic achievement and the party associated with many democratic disappointments.
""", political_identity="""
The ANC is both a liberation movement and a governing party. It sees itself as the custodian of South Africa's democratic transition and the main vehicle for transformation. Its politics combines:
- non-racialism,
- social democracy,
- state-led development,
- black economic empowerment,
- social protection,
- public services,
- and liberation movement identity. The ANC believes the state must actively correct apartheid's legacy. Its problem is credibility: many voters agree with the need for transformation but doubt whether the ANC can still deliver it honestly.
""", society_vision="""
The ANC imagines a non-racial, developmental, socially protective South Africa. Its ideal society is one where the democratic state expands access to:
- housing,
- water,
- electricity,
- education,
- healthcare,
- grants,
- jobs,
- land reform,
- and black economic participation. The ANC does not reject markets, but it believes the state must guide development and correct historical exclusion. It wants gradual transformation, not revolutionary rupture.
""", economic_approach="""
The ANC supports a mixed economy. It believes the state should play a major role in:
- infrastructure,
- industrial policy,
- public employment,
- social spending,
- land reform,
- BEE,
- procurement,
- and strategic sectors. The ANC's economic challenge is implementation. Its developmental-state language is ambitious, but critics argue that corruption, cadre deployment, weak SOEs, and policy uncertainty have weakened the state's ability to lead development.
""", equality_view="""
The ANC sees equality through transformation and redress. For the ANC, apartheid created structural racial inequality that cannot be solved through formal legal equality alone. This is why it supports:
- BEE,
- employment equity,
- land reform,
- public procurement,
- social grants,
- and expanded public services. Supporters argue these policies are necessary. Critics argue the ANC's transformation model has too often enriched politically connected elites rather than transforming the lives of the poor majority.
""", immigration_view="""
The ANC officially supports African solidarity, regional cooperation, and lawful migration. But it also faces pressure from communities angry about undocumented migration, unemployment, housing shortages, and pressure on public services. Its position is often caught between liberation-era pan-African commitments and domestic frustration. This makes ANC immigration politics appear cautious, inconsistent, and reactive.
""", crime_view="""
The ANC recognises crime as a serious national crisis. It often links crime to poverty, unemployment, inequality, drugs, and social breakdown. However, critics argue that the ANC has had decades to fix policing and justice systems and has failed to deal decisively with corruption, weak investigation, poor prosecution, and community mistrust. The ANC's crime problem is therefore not only policy. It is trust.
""", social_approach="""
The ANC's social approach is welfare-oriented and developmental. It supports:
- social grants,
- public healthcare,
- public education,
- housing,
- water and sanitation,
- youth programmes,
- and protection for vulnerable groups. The ANC's strongest social legacy is the expansion of basic services and grants after apartheid. Its weakness is that many services remain unreliable, unequal, and poorly managed.
""", governance_style="""
The ANC speaks about a developmental state, renewal, and institutional reform. But its governance reputation is damaged by:
- corruption,
- cadre deployment,
- state capture,
- weak municipalities,
- failing SOEs,
- and internal factionalism. Its governance challenge is not explaining what should be done. It is proving that it can still do it.
""", youth_relevance="""
Young South Africans often inherit the ANC as history but experience it as government. Many respect its liberation role, but judge it through:
- unemployment,
- NSFAS problems,
- load-shedding,
- corruption,
- crime,
- and weak local services. The ANC's youth challenge is generational: liberation memory is fading, and lived experience is becoming more important than historical loyalty.
""", major_support_base="""
The ANC's support has historically come from working-class voters, rural communities, older voters, liberation loyalists, public-sector-linked constituencies, and communities that value social grants and transformation.
""", common_criticisms="""
Supporters argue that the ANC built democratic South Africa and remains the party most committed to transformation, social protection, and correcting apartheid's legacy. Critics argue that the ANC has become too closely associated with corruption, cadre deployment, unemployment, failing municipalities, load-shedding, and state collapse. The central debate is whether the ANC can renew itself from within, or whether the party that built democratic South Africa has become one of the biggest obstacles to its next stage.
""", yoh_commentary="""
The ANC's story is complicated. It is not only a failed party, and it is not only a liberation hero. It is both. It built much of democratic South Africa, but also presided over many of its deepest failures. The ANC's biggest problem is that its moral language still sounds historic, but many people's daily lives feel stuck, unsafe, unemployed, and poorly served. Its question is no longer only:
What did you do for freedom? It is:
What are you doing with power now?
""", youth_appeal=5, ) add_policy( anc, "Transformation", "Redress, state power, and the limits of liberation politics", "The ANC argues that the democratic state must continue correcting apartheid's legacy through transformation, land reform, public investment, BEE, employment equity, and social protection.", "The deeper argument is that apartheid's damage was structural, so the democratic state must actively restructure access to opportunity.", "Could sustain redress, expand public services, protect poor households, and support black participation in the economy.", "Critics argue that ANC transformation has too often benefited elites, tender networks, and politically connected insiders.", "Black entrepreneurs, workers, rural communities, young people, grant recipients, public servants, and taxpayers.", "The ANC's transformation problem is not that transformation is unnecessary. It is that people increasingly ask who transformation has actually transformed." ) add_policy( anc, "Employment", "Jobs, public investment, and the developmental state", "The ANC links employment to infrastructure, industrial policy, public employment, investment, education, and transformation.", "Its employment theory depends on the state coordinating development and using public investment to unlock growth.", "Could support construction, industrial expansion, public employment, and infrastructure-led development.", "Fails if corruption, weak implementation, energy failure, and poor planning undermine state capacity.", "Unemployed youth, construction workers, public servants, businesses, municipalities, and households.", "The ANC's jobs promise depends on the very thing voters doubt most: whether the state can still execute." ) # ===================================================== # RISE # ===================================================== rise = create_party( name="RISE Mzansi", abbreviation="RISE", leader="Songezo Zibi", founded="2023", ideology="Social democracy, civic reform, anti-corruption, democratic renewal", political_position="Centre-left reformist", short_explainer="""
RISE Mzansi presents itself as a new civic-minded party focused on leadership renewal, social justice, safety, jobs, dignity, and rebuilding trust in democracy.
""", historical_context="""
RISE emerged in a period of voter disillusionment, ANC decline, coalition instability, and public frustration with old political language. It positions itself as a serious, ethical, values-driven alternative for citizens who feel politically homeless.
""", political_identity="""
RISE is a civic reform party. Its politics is built around:
- ethical leadership,
- active citizenship,
- social justice,
- anti-corruption,
- democratic renewal,
- and restoring dignity to public life. It does not rely on liberation nostalgia, radical militancy, or hard populism. Instead, it tries to sound thoughtful, responsible, and values-driven.
""", society_vision="""
RISE imagines a South Africa where democracy feels meaningful again. Its ideal society is one where:
- leaders are ethical,
- communities are safe,
- institutions are trusted,
- citizens participate,
- public services work,
- and social justice is pursued without political arrogance. RISE wants a political culture that is less cynical, less corrupt, and less trapped in old party wars.
""", economic_approach="""
RISE supports inclusive growth, job creation, public service repair, and economic participation for excluded communities. It is not as market-centred as the DA and not as radically redistributive as the EFF. Its economic position is reformist social democracy: grow the economy, but make it more inclusive and socially responsible.
""", equality_view="""
RISE sees equality as both material and democratic. People need jobs, housing, safety, and services, but they also need dignity, voice, and leaders who treat them as citizens rather than voting blocs. Its equality language is moral and civic rather than purely ideological.
""", immigration_view="""
RISE tends to approach migration through constitutionalism, documentation, fairness, and social cohesion. It avoids making migrants the centre of South Africa's crisis and focuses more on governance failure, poverty, unemployment, and public trust. Its position is less emotionally aggressive than ActionSA or PA.
""", crime_view="""
RISE treats safety as a democratic issue. Its argument is that freedom means little if communities are ruled by fear, extortion, violence, and weak policing. It links safety to dignity, trust, and the state's duty to protect citizens.
""", social_approach="""
RISE focuses on dignity, safety, education, social justice, service delivery, and rebuilding community trust. Its social politics is rooted in the idea that democracy must be felt in people's daily lives.
""", governance_style="""
RISE is professional, civic-minded, values-driven, and focused on ethical leadership. Its style is calm and serious, which appeals to some voters but may feel too gentle to people who want louder political confrontation.
""", youth_relevance="""
RISE may appeal to young people who want change but do not feel represented by old liberation politics, radical populism, or technocratic liberalism. It speaks to politically tired youth who want seriousness, ethics, and a new political culture.
""", major_support_base="""
RISE may appeal to young professionals, urban reform-minded voters, civil society voters, anti-corruption voters, first-time voters, and citizens who feel politically homeless.
""", common_criticisms="""
Supporters argue that RISE represents serious new politics: ethical, thoughtful, civic, and less trapped by old party wars. Critics argue that the party may sound good to educated urban voters but still needs to prove grassroots reach, organisational depth, and governing capacity. The central debate is whether South Africa is ready for values-driven civic reform politics, or whether politics is still too shaped by identity, history, anger, and material survival.
""", yoh_commentary="""
RISE speaks to people who are tired of political noise. Its strength is seriousness. Its weakness is that South African politics is brutal. A calm civic message must still survive unemployment, identity politics, populism, inequality, and coalition chaos. The question is whether ethics can mobilise people as powerfully as anger does.
""", youth_appeal=7, ) add_policy( rise, "Youth Development", "A new political culture for a tired generation", "RISE positions political renewal and ethical leadership as central to fixing South Africa.", "Its deeper argument is that South Africa's crisis is not only policy failure. It is leadership failure, trust failure, and democratic fatigue.", "Could attract young voters tired of corruption, old party battles, and empty slogans.", "Newness does not automatically create capacity, mass support, or grassroots organisation.", "Young voters, first-time voters, civil society, professionals, and disillusioned citizens.", "Many young people do not only want a new party. They want politics to feel less embarrassing." ) # Keep remaining parties shorter but still richer mk = create_party( name="uMkhonto weSizwe Party", abbreviation="MK", leader="Jacob Zuma", founded="2023", ideology="Populism, African nationalism, constitutional reform politics", political_position="Populist nationalist", short_explainer="MK is a disruptive anti-establishment party drawing from Zuma loyalty, ANC disappointment, cultural identity, and anger at the post-1994 settlement.", political_identity="MK is shaped by populism, African nationalism, cultural politics, anti-establishment anger, and the belief that the current constitutional order has failed many people.", society_vision="MK imagines a South Africa where the post-1994 settlement is challenged more directly and ordinary people feel less controlled by distant elites, courts, technocrats, and institutions they do not trust.", economic_approach="MK leans toward state intervention, redistribution, nationalist economic control, and criticism of the current economic settlement.", equality_view="MK frames equality as unfinished because political freedom did not give many people material power, dignity, land, or ownership.", immigration_view="MK's immigration stance is shaped by nationalist and community-protection language, with emphasis on order, borders, and state authority.", crime_view="MK links crime to state weakness, social decay, and loss of authority, calling implicitly for stronger order and decisive leadership.", social_approach="MK appeals to tradition, dignity, identity, cultural authority, and anger at political elites.", governance_style="MK is populist, confrontational, personality-driven, and strongly tied to Jacob Zuma's political brand.", youth_relevance="Some young people may see MK as protest against ANC failure and economic exclusion. Others may reject it as old politics wearing new colours.", major_support_base="Zuma loyalists, KwaZulu-Natal voters, disillusioned ANC supporters, traditionalist voters, and anti-establishment constituencies.", common_criticisms="Supporters say MK gives voice to people betrayed by the ANC and excluded by the post-1994 order.\n\nCritics argue MK is too personality-driven and tied to Zuma-era controversies.\n\nThe central debate is whether MK is a genuine new political force or an ANC revolt with a new logo.", yoh_commentary="MK shows that anger at ANC failure does not automatically become liberal reform. It can become nationalist, populist, cultural, and deeply personal.", youth_appeal=6, ) add_policy( mk, "Governance", "Anti-establishment anger and constitutional frustration", "MK questions the existing political order and speaks to voters who believe the current system has failed.", "The deeper argument is not only that government has failed, but that the settlement itself may be illegitimate or incomplete.", "Could force debate about authority, traditional leadership, courts, and democratic accountability.", "Could weaken constitutional stability if anger becomes anti-institutional rather than reformist.", "Disillusioned voters, courts, Parliament, traditional leaders, young voters, and communities angry at government failure.", "MK's rise says many people do not feel protected by the system they were told to trust." ) ifp = create_party( name="Inkatha Freedom Party", abbreviation="IFP", leader="Velenkosini Hlabisa", founded="1975", ideology="Conservatism, federalism, traditional leadership, social democracy elements", political_position="Centre-right conservative", short_explainer="The IFP is rooted in KwaZulu-Natal politics, traditional leadership, federalism, community stability, and cautious governance.", political_identity="The IFP combines Zulu cultural identity, traditional leadership, decentralisation, social stability, and anti-corruption messaging.", society_vision="The IFP imagines a society where community, tradition, local authority, family, and stable governance matter deeply.", economic_approach="The IFP supports local economic growth, infrastructure, agriculture, small business, and practical service delivery rather than radical restructuring.", equality_view="The IFP tends to view equality through community upliftment, local development, dignity, and access to services.", immigration_view="The IFP favours lawful migration, order, and the state's responsibility to manage borders while protecting communities.", crime_view="The IFP treats crime as a direct threat to community stability, family life, rural safety, and local development.", social_approach="The party emphasises family, community, traditional authority, safety, social support, and cultural institutions.", governance_style="The IFP presents itself as disciplined, community-rooted, experienced, and less chaotic than newer populist movements.", youth_relevance="Young people may connect with the IFP through local service delivery, safety, identity, education, and community belonging.", major_support_base="KwaZulu-Natal voters, traditional communities, conservative voters, rural communities, and voters loyal to the IFP's historical role.", common_criticisms="Supporters argue the IFP understands local communities, traditional leadership, rural life, and KwaZulu-Natal politics.\n\nCritics argue it can feel too regionally concentrated and tied to older forms of politics.\n\nThe central debate is whether rooted community politics is a strength or a limitation in national politics.", yoh_commentary="The IFP reminds us that politics is not only national TV debates. It is also rural authority, community memory, local trust, and whether government feels close enough to people's lives.", youth_appeal=5, ) add_policy( ifp, "Governance", "Decentralisation and local accountability", "The IFP favours stronger local and provincial authority and practical service delivery.", "Its deeper argument is that communities should have more direct control over development and governance.", "Could make government more responsive to local needs.", "Could become uneven if local institutions lack capacity or are captured by local elites.", "Rural communities, municipalities, traditional leaders, provincial governments, and local businesses.", "Local government is where politics becomes real: water, roads, clinics, safety, and whether someone answers when people complain." ) good = create_party( name="GOOD", abbreviation="GOOD", leader="Patricia de Lille", founded="2018", ideology="Social democracy, spatial justice, anti-poverty reform", political_position="Centre-left", short_explainer="GOOD focuses on poverty, spatial inequality, land, housing, public transport, ethical government, and the everyday geography of apartheid.", political_identity="GOOD's politics focuses on dignity, fairness, anti-corruption, and correcting spatial apartheid through housing, transport, and social policy.", society_vision="GOOD imagines a South Africa where where you live does not determine access to work, safety, schools, transport, and dignity.", economic_approach="GOOD supports inclusive growth, anti-poverty measures, public investment, and a stronger role for government in correcting inequality.", equality_view="GOOD sees equality through spatial justice, housing access, transport fairness, land access, and daily dignity.", immigration_view="GOOD generally avoids extreme migration politics and frames social pressure through poverty, housing, inequality, and governance failure.", crime_view="GOOD links safety to community stability, urban planning, service delivery, and functioning local government.", social_approach="GOOD emphasises housing, land access, public transport, gender justice, poverty reduction, and reducing daily inequality.", governance_style="GOOD presents itself as pragmatic, reformist, anti-corruption, and focused on practical social justice.", youth_relevance="Young people may connect with GOOD through housing, transport costs, land access, and urban inequality issues.", major_support_base="Urban voters, social justice voters, anti-corruption voters, and communities concerned with housing and spatial exclusion.", common_criticisms="Supporters argue GOOD focuses on the everyday geography of inequality: where people live, how far they travel, and what transport costs.\n\nCritics argue GOOD remains small and too dependent on Patricia de Lille's personal brand.\n\nThe central debate is whether smaller reformist parties can reshape politics or become coalition accessories.", yoh_commentary="GOOD's strongest contribution is spatial justice. It reminds voters that apartheid did not only create racial inequality. It designed where people live, work, travel, and struggle.", youth_appeal=5, ) add_policy( good, "Social Justice", "Spatial justice and the politics of distance", "GOOD treats housing, land, transport, and spatial inequality as central democratic issues.", "The deeper argument is that apartheid geography still shapes opportunity long after apartheid law ended.", "Could improve housing access, transport fairness, and urban opportunity.", "Housing reform is expensive, slow, and politically difficult, especially in cities with high land values.", "Backyard dwellers, young workers, commuters, informal settlement residents, municipalities, and landlords.", "Where you live decides how much of your life is spent waiting, travelling, and surviving." ) ff = create_party( name="Freedom Front Plus", abbreviation="FF+", leader="Pieter Groenewald", founded="1994", ideology="Minority rights, conservatism, federalism, property rights", political_position="Right-wing conservative", short_explainer="The FF Plus focuses on minority rights, property rights, federalism, language rights, community autonomy, and opposition to race-based policy.", political_identity="The FF Plus represents conservative minority politics, especially around Afrikaner interests, language, culture, property rights, and decentralised power.", society_vision="The FF Plus imagines a South Africa where communities have strong rights to language, culture, property, self-management, and protection from majoritarian overreach.", economic_approach="The FF Plus supports market economics, property protection, lower state interference, and opposition to policies it sees as racialised or punitive.", equality_view="The FF Plus tends to define equality as equal treatment before the law and protection from racial discrimination. Critics argue this underplays historic black dispossession and structural inequality.", immigration_view="The FF Plus supports stronger border control, lawful immigration systems, and stricter enforcement.", crime_view="The FF Plus treats crime, especially rural crime and farm attacks, as a major threat to community survival, property security, and social stability.", social_approach="It emphasises cultural rights, community self-determination, language protection, family, and conservative social values.", governance_style="The FF Plus favours decentralisation, community autonomy, federalism, and limiting central state power.", youth_relevance="Young people may engage with the FF Plus through debates on language, universities, property rights, minority identity, and affirmative action.", major_support_base="Afrikaans-speaking voters, minority rights voters, conservative voters, farmers, and people opposed to race-based policy.", common_criticisms="Supporters argue the FF Plus protects communities ignored or targeted by majoritarian politics.\n\nCritics argue it can appear too focused on minority anxiety and insufficiently responsive to black poverty and historical dispossession.\n\nThe central debate is whether minority protection strengthens democracy or becomes resistance to necessary redress.", yoh_commentary="The FF Plus forces a difficult democratic question: how do you protect minority rights while still transforming a deeply unequal society?", youth_appeal=4, ) add_policy( ff, "Transformation", "Property rights and redress debates", "The FF Plus strongly defends property rights and opposes expropriation without compensation.", "Its deeper argument is that property rights are essential for stability, investment, food security, and minority protection.", "Could reassure property owners, farmers, and investors.", "May be seen as too defensive in a country still shaped by land dispossession.", "Farmers, property owners, investors, rural workers, landless communities, and minority groups.", "This debate is one of South Africa's hardest: security of ownership versus justice for dispossession." ) pa = create_party( name="Patriotic Alliance", abbreviation="PA", leader="Gayton McKenzie", founded="2013", ideology="Populism, patriotism, law and order, coloured community advocacy", political_position="Populist conservative", short_explainer="The PA presents itself as a tough, patriotic, community-focused party with strong messaging on crime, immigration, drugs, service delivery, and coloured community representation.", political_identity="The PA mixes populist leadership, law-and-order politics, patriotic language, anti-illegal-immigration messaging, and direct appeals to communities that feel ignored.", society_vision="The PA imagines a South Africa where communities feel protected, borders are controlled, criminals fear consequences, drugs are confronted, and ignored groups are recognised.", economic_approach="The PA speaks about jobs, local opportunity, small business, community upliftment, and using government power to deliver quickly.", equality_view="The PA often speaks from the perspective of coloured communities and others who feel overlooked in national transformation debates.", immigration_view="The PA takes a hard line on illegal immigration and border control. Supporters see this as protecting jobs and communities. Critics worry it encourages scapegoating.", crime_view="The PA places crime, gangs, and drugs at the centre of its message. It treats safety as the first condition of dignity.", social_approach="The PA emphasises crime, drugs, community safety, border control, patriotism, and dignity for neglected communities.", governance_style="The PA is direct, personality-driven, populist, blunt, and focused on visible action.", youth_relevance="Young people may connect with its blunt language on crime, drugs, unemployment, and community neglect.", major_support_base="Coloured communities, anti-crime voters, populist voters, anti-illegal-immigration voters, and Gayton McKenzie supporters.", common_criticisms="Supporters argue the PA says what many communities are afraid to say publicly: crime, drugs, unemployment, and illegal immigration are destroying neighbourhoods.\n\nCritics argue the PA can become too personality-driven and too harsh toward migrants.\n\nThe central debate is whether blunt populism gives ignored communities a voice or turns pain into scapegoating.", yoh_commentary="The PA understands political emotion: anger, fear, pride, neglect, and recognition. The question is whether that emotional connection can become responsible governance.", youth_appeal=6, ) add_policy( pa, "Crime", "Drugs, gangs, and community fear", "The PA places strong emphasis on crime, drugs, gangs, and safer communities.", "Its deeper argument is that safety is the first condition for dignity and opportunity.", "Could appeal strongly in communities where crime shapes daily life.", "Hardline crime politics can fail if it does not address poverty, addiction, policing corruption, and youth exclusion.", "Young men, families, schools, township communities, coloured communities, police, and local businesses.", "Crime politics is powerful because fear is immediate. But safety needs more than toughness. It needs prevention, opportunity, policing reform, and trust." ) self.stdout.write(self.style.SUCCESS("Seeded all parties with expanded DA-style ideological analysis.")) 
