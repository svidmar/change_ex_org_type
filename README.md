# Bulk change type of external organisation in Elsevier's Pure

This Python script can be used to bulk change the "type" of external organisation in Elsevier's Pure system based on a list of UUID's in a csv file. Handy for cleaning data, migrating to different classifications and so on.

## Prerequisites
- An API Key for Pure with write permission to the /external-organizations/ endpoint (Remember to keep your key secure)
- Access to Pure's classifications and reporting module
- Libraries: requests, csv, time

### Deployment

Download the script, and open in your editor of choice: 
- Replace 'my_api_key' with your Pure API key.
- Replace 'pure_instance_url' with the URL of your Pure instance.
- Replace uri with your uri of choice, depending on what type you wish to change to. See available types in the classification scheme 'ueoexternalorganisationtypes' in your Pure.
- Save the script. 

- Extract the UUID's of the external organisations you want to change the type on from Pure (from the Pure reporting module). Save as a csv file named 'uuids.csv' in the same folder as this script.
- Run the script using your method of choice and get coffee. 
