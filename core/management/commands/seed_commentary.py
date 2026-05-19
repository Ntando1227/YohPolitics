from django.core.management.base import BaseCommand
from core.models import CommentaryArticle


class Command(BaseCommand):
    help = "Seed Yoh Politics commentary articles"

    def handle(self, *args, **kwargs):
        CommentaryArticle.objects.all().delete()

        articles = [
            {
                "title": "Why young South Africans are politically restless",
                "category": "Youth Politics",
                "summary": "Young people are not politically lazy. Many are politically exhausted, economically blocked, and unconvinced that old party language speaks to their actual lives.",
                "body": """
There is a lazy way people speak about young South Africans and politics. They say young people are apathetic, uninterested, lazy, or too distracted by social media.

That explanation is too easy.

Many young South Africans are not politically empty. They are politically tired.

They have grown up hearing promises about jobs, transformation, education, service delivery, and safety. Yet many of them experience politics through unemployment, NSFAS stress, high transport costs, broken municipalities, crime, and the humiliation of applying for jobs that never respond.

This is why youth politics in South Africa is restless.

Young voters are not only asking who governed in the past. They are asking who can make adulthood possible.

For older generations, politics was often about liberation, identity, and loyalty. For many young people, politics is about survival: getting a job, getting home safely, paying for data, escaping debt, finding housing, and not feeling trapped before life has even started.

This is why parties that speak strongly about jobs, land, safety, corruption, and dignity can attract young people even when their policies are controversial.

The key issue is not whether young people care about politics.

The key issue is whether politics cares about young people in a way that feels real.
"""
            },
            {
                "title": "The DA’s biggest problem is not competence. It is emotional distance.",
                "category": "Party Analysis",
                "summary": "The DA has built a strong message around clean governance, but South African politics is also about history, pain, race, dignity, and belonging.",
                "body": """
The DA's strongest political message is competence.

It tells voters that South Africa cannot fix unemployment, crime, education, healthcare, infrastructure, or poverty if the state itself is broken. That argument is serious. It matters.

A country cannot deliver justice through collapsed institutions.

But the DA's challenge is that South African politics is not only administrative. It is emotional and historical.

People are not only asking whether a municipality can get a clean audit. They are asking who owns land, who has inherited wealth, who travels furthest to work, who gets treated with dignity, and whose pain is recognised by political language.

This is where the DA often struggles.

Its language can sound technically correct but emotionally thin.

Competence matters. Clean government matters. Professional administration matters.

But in South Africa, a party must also speak to historical injury. It must explain how efficiency becomes justice.

The DA's future depends on whether it can connect capable government to deeper transformation.

Without that, it risks being respected by many voters but loved by fewer.
"""
            },
            {
                "title": "The EFF understands the politics of pain",
                "category": "Party Analysis",
                "summary": "The EFF’s power is that it gives language to economic humiliation. Its challenge is proving that radical justice can be governed responsibly.",
                "body": """
The EFF's strength is not only its policies. It is its emotional accuracy.

The party speaks directly to people who feel that democracy gave them the vote but not ownership, dignity, land, jobs, or real power.

That message lands because it names something many people experience.

A young person with a degree but no job understands economic exclusion.

A family without land understands historical dispossession.

A student blocked by fees understands that opportunity is not equal.

The EFF says these are not personal failures. They are political outcomes.

That is why its message is powerful.

But moral clarity is not the same as governing capacity.

The EFF's challenge is implementation. Nationalisation, land redistribution, free education, and massive state-led development require a capable, honest, technically skilled state.

South Africa's current state already struggles with procurement, corruption, maintenance, and basic service delivery.

So the EFF asks one of the most important questions in South African politics: who owns the country?

But voters must also ask: who can manage the transition?
"""
            },
            {
                "title": "Coalitions are not automatically democratic maturity",
                "category": "Coalition Watch",
                "summary": "Coalitions can improve accountability, but they can also become vehicles for instability, patronage, and political bargaining without public benefit.",
                "body": """
Coalitions are often presented as a sign of democratic maturity.

That can be true.

When no party dominates, parties must negotiate. They must compromise. They must listen. They must share power.

But South Africa's experience with coalitions has also shown the darker side.

Coalitions can become unstable. They can collapse over positions, budgets, tenders, and personal ambition. Voters may choose parties for policy reasons, only to watch those parties trade power in ways that feel disconnected from public needs.

The real question is not whether coalitions are good or bad.

The question is what kind of coalition politics South Africa is building.

A healthy coalition has:
- clear agreements,
- public accountability,
- policy alignment,
- dispute mechanisms,
- and consequences for betrayal.

An unhealthy coalition becomes a revolving door of mayors, motions of no confidence, and backroom deals.

Coalitions can make democracy deeper.

But only if parties treat voters as citizens, not bargaining chips.
"""
            },
            {
                "title": "Crime is now one of South Africa’s biggest political languages",
                "category": "Public Safety",
                "summary": "Crime is not only a policing issue. It shapes freedom, business, education, gender, transport, and whether people feel the state exists.",
                "body": """
Crime has become one of South Africa's most powerful political languages.

This is because crime is not abstract.

It affects whether a student can study late at the library. Whether a woman can walk home. Whether a small business can survive. Whether a commuter feels safe. Whether a child grows up seeing violence as normal.

Parties understand this.

That is why crime appears so strongly in manifestos.

But parties differ in how they explain crime.

Some treat it mainly as a policing problem.

Some link it to poverty and unemployment.

Some emphasise stronger sentencing.

Some focus on corruption in the police and courts.

Some use crime to talk about immigration.

The danger is that crime politics can become performative. It is easy to promise toughness. It is harder to build working detective units, trusted police stations, functioning courts, addiction treatment, youth programmes, and safer urban spaces.

South Africans do not only need politicians who sound angry about crime.

They need a state that can make ordinary life feel safe again.
"""
            },
        ]

        for article in articles:
            CommentaryArticle.objects.create(**article)

        self.stdout.write(self.style.SUCCESS("Seeded Yoh Politics commentary articles."))
