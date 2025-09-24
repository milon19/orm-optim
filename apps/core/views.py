import logging
from django.utils.translation import gettext as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)


class HelloWorldAPIView(APIView):
    def get(self, request):
        logger.error("Hello, World!", exc_info=True)
        logger.info("Hello, World! - Info level")
        return Response(
            {"message": "Hello, World!"},
            status=status.HTTP_200_OK
        )

class TestView(APIView):
    def get(self, request):
        base_sentences = [
            _("This is a simple sentence just for the test"),
            _("Learning to code can improve your life very quickly"),
            _("Never underestimate the power of a good attitude"),
            _("We all start as beginners and grow through experience"),
            _("Stay focused and consistent to reach your biggest goals"),
            _("This coffee is exactly what I needed this morning"),
            _("Technology keeps evolving and shaping our modern digital world"),
            _("He writes code like poetry — clean and beautiful"),
            _("Every product should prioritize accessibility from day one"),
            _("Design thinking helps solve complex problems with user focus"),
            _("Creativity often thrives under pressure and strict deadlines"),
            _("Feedback loops are vital for improving any software system"),
            _("Always write code that others can understand and maintain"),
            _("Testing saves time and prevents bugs in the future"),
            _("Let’s automate the boring stuff and focus on creativity"),
            _("Use version control to track changes and collaborate better"),
            _("Sleep is essential for both mental and physical performance"),
            _("Communication is key in every successful engineering team ever"),
            _("Make documentation part of your development workflow always"),
            _("You should back up your files early and often"),
            _("Strong teams are built on trust, clarity, and respect"),
            _("Deployments should be safe, repeatable, and fully automated too"),
            _("A productive morning sets the tone for your day"),
            _("You can’t optimize what you don’t measure effectively"),
            _("Simplicity wins over cleverness in long-term code maintenance"),
            _("Failures are stepping stones toward long-term sustainable growth"),
            _("Developing empathy improves software quality and user experience"),
            _("A great developer keeps learning throughout their whole life"),
            _("Every keyboard shortcut you learn saves hours long-term"),
            _("Push small commits with clear messages for easy tracking"),
            _("Daily standups help keep everyone aligned and accountable too"),
            _("Naming variables clearly avoids confusion down the road"),
            _("Code reviews help teams share knowledge and prevent errors"),
            _("Start small, iterate fast, and improve with every feedback"),
            _("Curiosity drives innovation in every successful tech company"),
            _("Avoid scope creep by defining clear goals from beginning"),
            _("Open-source contributions grow skills and expand your network"),
            _("Be kind in code reviews and give actionable suggestions"),
            _("Small bugs often hide inside big complex legacy systems"),
            _("Great products come from solving real-world user problems"),
            _("Prioritize learning over perfection — progress is what matters"),
            _("Even experienced developers ask questions and seek help"),
            _("Clean code is like a good joke — obvious later"),
            _("Always validate user input to avoid unexpected application errors"),
            _("Context switching kills productivity — batch related tasks together"),
            _("Read the documentation before reinventing something that already exists"),
            _("Deadlines exist, but quality should never be compromised ever"),
            _("Your tools matter less than how you actually use them"),
            _("Refactor often — technical debt will haunt your future self"),
            _("A good CLI makes repetitive tasks fun and fast"),
            _("Strong typing helps avoid entire categories of runtime bugs"),
            _("Debugging is an essential skill every dev must master"),
            _("Know when to stop optimizing and ship the thing"),
            _("Passion fuels consistency and drives long-term career growth"),
            _("Celebrate small wins to stay motivated and mentally healthy"),
            _("Protect your time — not every meeting needs your presence"),
            _("Clarity in code reduces stress for future maintainers definitely"),
            _("Good UX starts with understanding your users very deeply"),
            _("Don’t blindly follow trends — evaluate them carefully first"),
            _("A feature is done only when fully tested too"),
            _("Write pseudocode to clarify logic before jumping into implementation"),
            _("Good software balances performance, usability, and maintainability altogether"),
            _("Never ship code on a Friday — trust the wisdom"),
            _("Document why something was done — not just how"),
            _("Edge cases will break your app if not tested"),
            _("Users don’t care about your stack — only experience"),
            _("Keep functions small and focused for better reusability always"),
            _("Ask for feedback regularly and grow from each response"),
            _("APIs should be intuitive, well-documented, and versioned carefully"),
            _("Break big problems into smaller manageable chunks of work"),
            _("Mentorship accelerates growth for juniors and seniors alike"),
            _("Complexity is the enemy of reliability in production systems"),
            _("Team rituals build culture and strengthen communication naturally"),
            _("Don’t assume — validate ideas with real user research"),
            _("Make error messages helpful and human-readable whenever possible"),
            _("System architecture should be driven by actual product needs"),
            _("Write tests like they are documentation for future developers"),
            _("Great ideas are useless without good execution and follow-through"),
            _("Know your tools inside-out — it saves tons of time"),
            _("Empower users instead of restricting them without good reason"),
            _("Bad onboarding can ruin the best product experience ever"),
            _("Your product’s first impression really matters to every user"),
            _("Startups need to move fast, but not recklessly fast"),
            _("Avoid magic in code — be explicit where possible"),
            _("Don’t refactor blindly — have a clear objective always"),
            _("Your job isn’t just code — it’s solving problems"),
            _("Legacy code deserves love too — don’t trash it blindly"),
            _("Innovation thrives where experimentation and failure are encouraged"),
            _("Use logs to trace, debug, and learn from issues"),
            _("Prioritize developer experience to build faster and better software"),
            _("Code should read like a story, not a puzzle"),
            _("Push often, pull often — avoid nasty merge conflicts later"),
            _("Track KPIs to ensure your product delivers real value"),
            _("Avoid burnout — balance work with rest and hobbies"),
            _("Great software solves a real pain with elegant simplicity"),
            _("DevOps culture brings developers and operations closer together efficiently"),
            _("Onboarding should feel like mentorship, not a scavenger hunt"),
            _("Always run performance tests before major feature releases"),
            _("Security isn’t optional — build it in from start"),
            _("Clear folder structures help others navigate your codebase faster"),
            _("Use feature flags to release incrementally and test safely"),
            _("Every commit tells a story — write them intentionally"),
            _("Retrospectives help teams reflect, learn, and continuously improve"),
            _("Celebrate the progress, not just the end goal achieved")
        ]
        _help = _(
            "This is a test view that returns a list of base sentences in English."
        )

        return Response(
            base_sentences,
            status=status.HTTP_200_OK
        )
