from django.core.management.base import BaseCommand
from core.models import CommentaryArticle


class Command(BaseCommand):
    help = "Seed additional Yoh Politics commentary"

    def handle(self, *args, **kwargs):

        articles = [

            {
                "title": "Why coalition politics feels emotionally exhausting",
                "category": "Coalition Watch",
                "summary": "Many South Africans no longer feel politically stable. Coalition collapses create a sense that politics has become permanent negotiation without clear direction.",
                "body": """
Coalition politics creates uncertainty.

Mayors change. Alliances collapse. Parties attack each other one week and negotiate the next.

For ordinary people, this creates emotional fatigue.

Citizens are trying to survive unemployment, crime, rising costs, poor transport, and infrastructure collapse. When politics appears unstable, people begin feeling that government itself has become unpredictable.

Coalitions can improve accountability.

But they can also make voters feel disconnected from power because decisions begin looking transactional rather than principled.

The long-term question is whether South Africa can build coalition culture rather than coalition chaos.
"""
            },

            {
                "title": "Why immigration became such an explosive political issue",
                "category": "Immigration",
                "summary": "Immigration debates in South Africa are not only about borders. They are about fear, unemployment, state failure, identity, and pressure on struggling communities.",
                "body": """
Immigration became politically explosive because it intersects with economic desperation.

In communities already struggling with jobs, housing, healthcare access, crime, and municipal collapse, migration becomes emotionally charged very quickly.

Some parties argue for much stricter border control and deportation systems.

Others warn that migrants are being blamed for structural failures caused by corruption, weak planning, and unemployment.

The danger is that immigration politics can become emotionally convenient.

When the state fails, vulnerable outsiders become easy political targets.

But communities also want functioning documentation systems and predictable migration policy.

The challenge is balancing humanity, law, economic pressure, and social stability.
"""
            },

            {
                "title": "Why unemployment changes how people experience democracy",
                "category": "Economy",
                "summary": "Mass unemployment changes how citizens think about dignity, politics, relationships, identity, and whether democracy itself is working.",
                "body": """
Unemployment is not only about money.

It changes how people experience adulthood itself.

Young people delay moving out. Relationships become financially stressful. Families absorb economic pressure for years. Graduates lose confidence. Informal work becomes survival.

Politics becomes emotional under these conditions.

People stop asking only whether policies sound good.

They ask whether life is actually becoming possible.

This is why unemployment shapes political anger so strongly in South Africa.

A democracy where millions feel economically trapped eventually creates frustration toward institutions, parties, elites, and even the idea of democratic patience itself.
"""
            },

            {
                "title": "Why South Africans are losing trust in institutions",
                "category": "Governance",
                "summary": "The crisis is not only corruption. It is the feeling that institutions no longer protect ordinary people consistently or fairly.",
                "body": """
Institutional trust is fragile.

People trust institutions when they believe rules matter, accountability exists, and systems function predictably.

But corruption scandals, state capture, collapsing municipalities, policing failures, electricity instability, and public sector dysfunction weaken public confidence.

The danger is larger than political embarrassment.

When people stop trusting institutions, they begin relying more on anger, personality politics, conspiracy, tribal identity, or strongman politics.

That is why institutional repair matters politically, economically, and socially.

A functioning democracy depends on citizens believing the system still belongs to them.
"""
            },

        ]

        for article in articles:
            CommentaryArticle.objects.create(**article)

        self.stdout.write(self.style.SUCCESS("Seeded extra commentary articles."))
