def build_prompt(requirement):
    return f"""
    Convert the following requirement into structured QA test cases:
    Include:
    - Test Case ID
    - Steps
    - Expected Result

    Requirement:
    {requirement}
    """
