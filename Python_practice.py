# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# if counties[1] != 'Jefferson':
#     print(counties[2])

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not in the list of counties.")

# if "Araphahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties yo.")

# if "Araphahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso are in the list of counties.")
# else:
#     print("Arapahoe and El Paso is not in the list of counties yo.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)  

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])

#counties_tuple = ["Arapahoe","Denver","Jefferson"]
# for i in range(len(counties_tuple)):

#       print(counties_tuple[i])

# for county in counties_tuple:

#       print(county)

# for county in counties_tuple:

#       print(counties)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.keys():
#     print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict.values():
#     print(county)

# for voters in counties_dict.values():
#     print(voters)

# for county in counties_dict:
#     print(counties_dict[county])

# for county, voters in counties_dict.items():
#     print(county, 'county has', voters, 'registered voters.')

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):

#       print(voting_data[i]['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:

#      print(county_dict['county'])

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")

# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver":463353, "Jefferson": 432438}
for county in counties_dict:
    print(county)  

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
{"county":"Denver", "registered_voters": 463353},
{"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

    for county_dict in voting_data:
        for value in county_dict.values():
            print(value)

# print each county and registered voter from the counties dictionary.
    for county, voters in counties_dict.items():
        print(county + " county has " + str(voters) + " registered voters.")

# use f-stings to rewrite the print statement above to be more intuitive and clear
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
    
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv' 
# Open election results and use 'r' to read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.
# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: perform analysis.
     print(election_data)
