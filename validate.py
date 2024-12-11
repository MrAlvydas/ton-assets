import yaml

def validate_yaml(file):
    try:
        with open(file, encoding="utf-8") as f:
            content = yaml.safe_load(f)
            print(f"{file} is valid.")
    except yaml.YAMLError as e:
        print(f"Error in {file}: {e}")

validate_yaml("jettons/INVESV.yaml")
