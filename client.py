class SyntheticTestUserPersonaGeneratorClient:
    def generate_personas(self, target_demographic: str, persona_count: int = 2) -> dict:
        personas = [
            {"name": "Tech Savvy Developer Alex", "behavior": "Fast clicks, uses keyboard shortcuts, tests edge cases"},
            {"name": "Casual User Sam", "behavior": "Reads onboarding guides, prefers simple UI buttons"}
        ]
        return {
            "generated_personas": personas[:persona_count]
        }
