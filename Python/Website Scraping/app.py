import requests
from bs4 import BeautifulSoup


def extract_ability_name(image_path):
    # Split the image path by slashes
    parts = image_path.split('/')

    # Get the part after the third slash
    substring = parts[3]

    # Skip everything until the first dash
    substring = substring.split('-', 1)[-1]

    # Take everything before the dot
    substring = substring.split('.')[0]

    # Replace dashes with spaces
    substring = substring.replace('-', ' ')

    # Capitalize the first letter and every subsequent word
    substring = ' '.join(word.capitalize() for word in substring.split())

    return substring


url = "https://www.mobafire.com/league-of-legends/abilities"
output_file = "output.json"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find all the links with class "ability-list__item"
links = soup.find_all("a", class_="ability-list__item")

# Iterate over the links and extract the desired information
with open(output_file, "w") as file:
    file.write("[\n")
    for link in links:
        img_tag = link.find("img", class_="ability-list__item__pic")
        if img_tag:
            data_original = img_tag.get("data-original")
        else:
            data_original = None

        champion_tag = link.find("img", class_="ability-list__item__champ")
        if champion_tag:
            champion = champion_tag.get("champ")
        else:
            champion = None

        name = extract_ability_name(data_original)

        file.write("{\n")
        file.write(f"\t\"champion\": \"{champion}\",\n")
        file.write(f"\t\"name\": \"{name}\",\n")
        file.write(f"\t\"image_url\": \"https://www.mobafire.com{data_original}\",\n")
        file.write(f"\t\"is_passive\": false\n")
        file.write("},\n")
    file.write("]")

print("Data has been written to the file:", output_file)
