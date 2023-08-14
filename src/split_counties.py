import json

# Read the contents of counties_list.json and states_hash.json
with open('counties_list.json', 'r') as f:
    counties = json.load(f)

with open('states_hash.json', 'r') as f:
    states = json.load(f)

# Create an empty dictionary to store the counties for each state
state_counties = {}
state_abbrs = {state_name: state_abbr for state_abbr,
               state_name in states.items()}


# Loop through the counties in counties_list.json
for county in counties:
    # Get the state abbreviation from the state field
    state_name = county['State']

    # Check if the state abbreviation exists in the dictionary
    if state_name in state_counties:
        # Append the county to the list of counties for that state
        state_counties[state_name].append(county)
    else:
        # Create a new key-value pair in the dictionary
        state_counties[state_name] = [county]

# Write the dictionary to separate JSON files for each state
for state_name, counties in state_counties.items():
    state_abbr = state_abbrs[state_name]
    with open(f'../dist/{state_abbr}.json', 'w') as f:
        sorted_counties = sorted(counties, key=lambda county: county['County'])
        json.dump(sorted_counties, f)
