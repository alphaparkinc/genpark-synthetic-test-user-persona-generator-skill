from client import SyntheticTestUserPersonaGeneratorClient

def main():
    client = SyntheticTestUserPersonaGeneratorClient()
    res = client.generate_personas("B2B SaaS Users", 2)
    print("Generated Test Personas:")
    for p in res["generated_personas"]:
        print(f"  - {p['name']}: {p['behavior']}")

if __name__ == "__main__":
    main()
