import json
import pprint

# Full list of ingredients
ingredients = [ "Hydroponic Root", "Ferrite Dust", "Stellar Herb", "Cryocrystal", "Cryopaste", "Nebula Moss", "Carbon Flakes", "Fungi", "S̵̡͇̽̾͜͝p̷̪̪̻͂o̸̢̼̞͌̃r̶̳̘͖͝ë̸̤̱́̄̍s̶͍̗̓", "Root Extract", "Ground Root", "Fine Ferrite Dust",
               "Ferrite Nuggets", "Stellar Herb Extract", "Ground Stellar Herb", "Cryocrystal Powder", "Activated Moss", "Nebula Extract",
               "Carbon Fibrils", "Fungi Extract", "E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚", "Root Concentrate", "Root Essence", "Finely Ground Root", "Ferrite Weave", "Ferrite Plate", "Stellar Paste", "Herb Essence", "Finely Ground Stellar Herb",
               "Cryocrystalline Shards", "Nebula Moss Concentrate", "Nebula Resin", "Nebula Essence", "Carbon Sheet", "Carbon Powder", "Fungi Essence"]

starters = ["Hydroponic Root", 'Ferrite Dust', 'Stellar Herb', 'Cryocrystal', 'Nebula Moss', 'Carbon Flakes', 'Fungi', 'S̵̡͇̽̾͜͝p̷̪̪̻͂o̸̢̼̞͌̃r̶̳̘͖͝ë̸̤̱́̄̍s̶͍̗̓']

alchemy_dict = {"Starting":{}, "Ingredients":{},"Recipes":{}}

for ingredient in ingredients:
    alchemy_dict["Ingredients"][ingredient] = {
        "Heater": None,
        "Extractor": None,
        "Grinder": None,
    }
for ing in starters:
    alchemy_dict["Starting"][ing] = 0
    

alchemy_dict["Ingredients"]["Hydroponic Root"]["Extractor"] = "Root Extract"
alchemy_dict["Ingredients"]["Hydroponic Root"]["Grinder"] = "Ground Root"
alchemy_dict["Ingredients"]["Ferrite Dust"]["Grinder"] = "Fine Ferrite Dust"
alchemy_dict["Ingredients"]["Ferrite Dust"]["Heater"] = "Ferrite Nuggets"
alchemy_dict["Ingredients"]["Stellar Herb"]["Extractor"] = "Stellar Herb Extract"
alchemy_dict["Ingredients"]["Stellar Herb"]["Grinder"] = "Ground Stellar Herb"
alchemy_dict["Ingredients"]["Cryocrystal"]["Grinder"] = "Cryocrystal Powder"
alchemy_dict["Ingredients"]["Cryocrystal"]["Heater"] = "Cryopaste"
alchemy_dict["Ingredients"]["Nebula Moss"]["Heater"] = "Activated Moss"
alchemy_dict["Ingredients"]["Nebula Moss"]["Extractor"] = "Nebula Extract"
alchemy_dict["Ingredients"]["Carbon Flakes"]["Heater"] = "Carbon Fibrils"
alchemy_dict["Ingredients"]["Fungi"]["Extractor"] = "Fungi Extract"
alchemy_dict["Ingredients"]["S̵̡͇̽̾͜͝p̷̪̪̻͂o̸̢̼̞͌̃r̶̳̘͖͝ë̸̤̱́̄̍s̶͍̗̓"]["Extractor"] = "E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚"

alchemy_dict["Ingredients"]["Root Extract"]["Heater"] = "Root Concentrate"
alchemy_dict["Ingredients"]["Root Extract"]["Extractor"] = "Root Essence"

alchemy_dict["Ingredients"]["Ground Root"]["Extractor"] = "Root Essence"
alchemy_dict["Ingredients"]["Ground Root"]["Grinder"] = "Finely Ground Root"

alchemy_dict["Ingredients"]["Fine Ferrite Dust"]["Heater"] = "Ferrite Weave"

alchemy_dict["Ingredients"]["Ferrite Nuggets"]["Heater"] = "Ferrite Plate"

alchemy_dict["Ingredients"]["Stellar Herb Extract"]["Heater"] = "Stellar Paste"

alchemy_dict["Ingredients"]["Ground Stellar Herb"]["Extractor"] = "Herb Essence"
alchemy_dict["Ingredients"]["Ground Stellar Herb"]["Grinder"] = "Finely Ground Stellar Herb"

alchemy_dict["Ingredients"]["Cryocrystal Powder"]["Heater"] = "Cryocrystalline Shards"

alchemy_dict["Ingredients"]["Activated Moss"]["Extractor"] = "Nebula Moss Concentrate"

alchemy_dict["Ingredients"]["Nebula Extract"]["Heater"] = "Nebula Resin"
alchemy_dict["Ingredients"]["Nebula Extract"]["Extractor"] = "Nebula Essence"

alchemy_dict["Ingredients"]["Carbon Fibrils"]["Heater"] = "Carbon Sheet"
alchemy_dict["Ingredients"]["Carbon Fibrils"]["Grinder"] = "Carbon Powder"

alchemy_dict["Ingredients"]["Fungi Extract"]["Extractor"] = "Fungi Essence"

alchemy_dict["Recipes"] = {
    "Anti-Radiation Shield": ["Ferrite Dust", "Nebula Extract"],
    "Life Support Supplement": ["Cryocrystal", "Activated Moss"],
    "Hyperdrive Enhancer": ["Cryocrystal Powder", "Cryopaste"],
    "Atmospheric Cleaner": ["Nebula Moss", "Hydroponic Root"],
    "Nutrient Enrichment": ["Stellar Herb", "Ground Root"],
    "Alien Detoxifier": ["S̵̡͇̽̾͜͝p̷̪̪̻͂o̸̢̼̞͌̃r̶̳̘͖͝ë̸̤̱́̄̍s̶͍̗̓", "Carbon Fibrils"],
    "Bio-Rejuvenation Tonic": ["Fungi", "Nebula Extract"],
    "Shield Strengthener": ["Ferrite Plate", "Ferrite Weave"],
    "Optical Fluid": ["Cryocrystal", "Hydroponic Root"],
    "Medicinal Balm": ["Fungi Essence", "Nebula Resin"],
    "Thermal Coat": ["Cryocrystalline Shards", "Ferrite Nuggets"],
    "Space Detox Drink": ["Activated Moss", "Ground Stellar Herb"],
    "Super Adhesive": ["Carbon Sheet", "Ferrite Weave"],
    "Organic Shield": ["Root Extract", "Fungi Extract"],
    "Healing Ointment": ["Nebula Extract", "Cryocrystal Powder"],
    "Radiation Barrier": ["Ferrite Dust", "Stellar Herb Extract"],
    "Oxygen Booster": ["Cryocrystal", "Root Essence"],
    "Engine Coolant": ["Cryocrystal Powder", "Ground Root"],
    "Air Purifier": ["Nebula Moss", "Ferrite Plate"],
    "Growth Enhancer": ["Stellar Herb", "Cryopaste"],
    "Alien Remedy": ["E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚", "Ferrite Weave"],
    "Bio-Revitalizer": ["Fungi", "Root Extract"],
    "Shield Coating": ["Ferrite Plate", "Cryocrystal Powder"],
    "Visual Aid": ["Cryocrystal", "Stellar Herb Extract"],
    "Healing Gel": ["Fungi Essence", "Cryopaste"],
    "Heat Shield": ["Cryocrystalline Shards", "Root Concentrate"],
    "Space Cleanser": ["Activated Moss", "Ground Root"],
    "Binding Agent": ["Carbon Sheet", "Ground Stellar Herb"],
    "Organic Armor": ["Root Extract", "Ferrite Dust"],
    "Restorative Cream": ["Nebula Extract", "Root Essence"],
    "Energy Shield": ["Ferrite Dust", "Stellar Paste"],
    "Air Refresher": ["Cryocrystal", "Nebula Moss Concentrate"],
    "Coolant Paste": ["Cryocrystal Powder", "Carbon Fibrils"],
    "Atmospheric Reagent": ["Nebula Moss", "Cryocrystal Powder"],
    "Plant Fertilizer": ["Stellar Herb", "Cryocrystalline Shards"],
    "Alien Cure": ["E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚", "Stellar Herb Extract"],
    "Bio-Elixir": ["Fungi", "Activated Moss"],
    "Shield Enhancer": ["Ferrite Plate", "Ground Root"],
    "Optical Solution": ["Cryocrystal", "Nebula Essence"],
    "Healing Potion": ["Fungi Essence", "Stellar Herb Extract"],
    "Thermal Barrier": ["Cryocrystalline Shards", "Ferrite Weave"],
    "Space Purifier": ["Activated Moss", "Cryocrystal Powder"],
    "Sealing Compound": ["Carbon Sheet", "Fungi Extract"],
    "Organic Booster": ["Root Extract", "Cryopaste"],
    "Regenerative Balm": ["Nebula Extract", "Stellar Herb Extract"],
    "Radiation Shield": ["Ferrite Dust", "Root Extract"],
    "Oxygenator": ["Cryocrystal", "Ground Stellar Herb"],
    "Engine Lubricant": ["Cryocrystal Powder", "Nebula Moss"],
    "Atmosphere Stabilizer": ["Nebula Moss", "Fungi Essence"],
    "Plant Tonic": ["Stellar Herb", "Cryocrystal"],
    "Alien Medicine": ["S̵̡͇̽̾͜͝p̷̪̪̻͂o̸̢̼̞͌̃r̶̳̘͖͝ë̸̤̱́̍s̶͍̗̓", "Ground Stellar Herb"],
    "Bio-Restorer": ["Fungi", "Cryocrystal Powder"],
    "Shield Hardener": ["Ferrite Plate", "Cryocrystalline Shards"],
    "Optical Enhancer": ["Cryocrystal", "Stellar Paste"],
    "Healing Remedy": ["Fungi Essence", "Root Extract"],
    "Thermal Wrap": ["Cryocrystalline Shards", "Stellar Herb Extract"],
    "Space Sanitizer": ["Activated Moss", "Ferrite Dust"],
    "Bonding Agent": ["Carbon Sheet", "Ground Root"],
    "Organic Armor Booster": ["Root Extract", "Ferrite Plate"],
    "Restorative Lotion": ["Nebula Extract", "Ground Stellar Herb"],
    "Energy Coating": ["Ferrite Dust", "Nebula Resin"],
    "Air Freshener": ["Cryocrystal", "Ground Root"],
    "Coolant Gel": ["Cryocrystal Powder", "Ferrite Plate"],
    "Atmosphere Enricher": ["Nebula Moss", "Cryocrystalline Shards"],
    "Plant Booster": ["Stellar Herb", "Activated Moss"],
    "Alien Treatment": ["E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚", "Cryocrystal Powder"],
    "Bio-Tonic": ["Fungi", "Ferrite Dust"],
    "Shield Fortifier": ["Ferrite Plate", "Root Essence"],
    "Optical Booster": ["Cryocrystal", "Ferrite Nuggets"],
    "Healing Elixir": ["Fungi Essence", "Cryocrystal Powder"],
    "Thermal Guard": ["Cryocrystalline Shards", "Fungi Extract"],
    "Space Cleaner": ["Activated Moss", "Cryocrystal"],
    "Super Bond": ["Carbon Sheet", "Root Essence"],
    "Organic Shield Enhancer": ["Root Extract", "Activated Moss"],
    "Rejuvenation Balm": ["Nebula Extract", "Ground Root"],
    "Radiation Coating": ["Ferrite Dust", "Stellar Paste"],
    "Oxygen Enhancer": ["Cryocrystal", "Ground Root"],
    "Engine Shield": ["Cryocrystal Powder", "Fungi Essence"],
    "Atmosphere Cleaner": ["Nebula Moss", "Ferrite Nuggets"],
    "Plant Growth Serum": ["Stellar Herb", "Carbon Powder"],
    "Alien Elixir": ["E̸̜̋s̸̨̙̆̀͝ṩ̷̲͂̏ͅẽ̸̜̬̣̕n̶̩̕c̷̼̱̅è̷͕͎̚", "Root Concentrate"],
    "Bio-Serum": ["Fungi", "Cryocrystalline Shards"],
    "Shield Layer": ["Ferrite Plate", "Ground Root"],
    "Optical Enhancing Fluid": ["Cryocrystal", "Carbon Fibrils"],
    "Healing Draught": ["Fungi Essence", "Nebula Extract"],
    "Thermal Buffer": ["Cryocrystalline Shards", "Carbon Sheet"],
    "Space Detoxifier": ["Activated Moss", "Ferrite Plate"],
    "High-Bond Adhesive": ["Carbon Sheet", "Cryocrystal"],
    "Organic Fortifier": ["Root Extract", "Cryocrystal Powder"],
    "Rejuvenation Cream": ["Nebula Extract", "Ferrite Weave"],
    "Radiation Armor": ["Ferrite Dust", "Ground Root"],
    "Oxygen Infuser": ["Cryocrystal", "Carbon Sheet"],
    "Engine Fortifier": ["Cryocrystal Powder", "Cryocrystalline Shards"],
    "Atmosphere Purifier": ["Nebula Moss", "Carbon Powder"],
    "Plant Enhancer": ["Stellar Herb", "Cryocrystal Powder"]
}

def get_origin(alchemy_dict, target_product): 
    verbs = {"Extractor":'Extract', 'Grinder': 'Grind', 'Heater': 'Heat'}

    if target_product in alchemy_dict["Ingredients"]:
        print(target_product)

get_origin(alchemy_dict, "Carbon Powder")

with open("alchemy.json", "w") as json_file:
    json.dump(alchemy_dict, json_file, indent=4)
