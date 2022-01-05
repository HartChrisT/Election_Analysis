counties = ["Arapahoe", "Denver", "Jefferson"]
counties.insert(2,"El Paso")
counties.pop(0)
counties.append("Denver")
counties.pop(0)
counties.append("Arapahoe")

print(counties)

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)
print(len(counties_dict))
print(counties_dict.items())
print(counties_dict.keys())
print(counties_dict.values())
print(counties_dict.get("Denver"))
print(counties_dict.get("Arapahoe"))
print(counties_dict['Arapahoe'])
voting_data = []
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
voting_data.append({'county': "Denver", 'registered_voters': 463353})
voting_data.append({'county':'Jefferson', 'registered_voters': 432438})
voting_data.insert(1,{'county': 'El Paso', 'registered_voters': 461149})
voting_data.pop(0)
voting_data.insert(1,{'county':'Jefferson', 'registered_voters': 432438})
voting_data.pop(3)
voting_data.append({'county':'Arapahoe', 'registered_voters': 422829})
print(voting_data)