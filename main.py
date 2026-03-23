from ai_engine.test_generator import generate_test_cases

with open("test_data/sample_requirement.txt", "r") as file:
    requirement = file.read()

test_cases = generate_test_cases(requirement)

print("\nGenerated Test Cases:\n")
print(test_cases)
