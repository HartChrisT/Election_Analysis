#Analysis of Election Audit

##Overview of Election Audit
Purpose: To automate the Election-Audit through a python script and output the findings in a simple to read text file that can be sent to the Board of Elections.

##Election-Audit Results
![Results_txt](https://user-images.githubusercontent.com/92996865/148632923-7e5580f4-9395-40ba-b691-5f0808ead637.png)

•	369,711 votes were cast in the congressional election
•	Jefferson county received 10.5% of the vote and 38,855 total votes, Denver county received 82.8% of the vote and 306,055 total votes, and Arapahoe county received 6.7%% of the vote and 24,801 total votes.
•	Denver county had the largest number of votes
•	Charles Casper Stockham received 23.0% of the vote and 85,213 total votes, Diana DeGette received 73.8% of the vote and 272,892 total votes, and Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes.
•	Diana DeGette won the election with 73.8% of the vote and 272,892 total votes

##Election-Audit Summary
With a few simple modifications, this script can be used to audit almost any election. We would obviously have to modify the file_to_load and file_to_save variables to load and save election data from the election in question. Secondly, we may need to take a glance at the csv file and change some of the row numbers in our for row in reader for loop so they correspond with the data we want to retrieve.  If the file is not a csv file, we may need to import different dependencies for that particular file.
