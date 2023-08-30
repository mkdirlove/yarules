import argparse

def create_yara_rule(rule_name, strings, string_count, condition):
    rule_content = f"""
rule {rule_name}
{{
    strings:
        {strings}
    condition:
        {condition}
    {string_count}
}}
"""
    return rule_content

def main():
    parser = argparse.ArgumentParser(description="Generate YARA rule")
    parser.add_argument("--rule-name", required=True, help="Name of the YARA rule")
    parser.add_argument("--string-count", type=int, required=True, help="Number of strings required to match")
    parser.add_argument("--strings", required=True, help="Strings for the YARA rule (use format 'string = \"text\" [wide ascii]')")
    parser.add_argument("--condition", choices=["all of them", "any of them", "all of them except"], default="any of them", help="Condition for the YARA rule")
    args = parser.parse_args()

    try:
        # Validate and format the strings
        formatted_strings = "\n".join(["        " + s for s in args.strings.split("\n")])
        
        # Create the YARA rule
        yara_rule = create_yara_rule(args.rule_name, formatted_strings, args.string_count, args.condition)
        
        # Save the YARA rule to a file
        output_filename = f"{args.rule_name}.yar"
        with open(output_filename, "w") as f:
            f.write(yara_rule)
        
        print(f"YARA rule saved to {output_filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
