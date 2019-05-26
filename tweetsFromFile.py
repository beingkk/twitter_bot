import json

#reads the file line by line and appends the json to data array
data = []
with open('tweets.dat') as f:
    for line in f:
        data.append(json.loads(line))

#loop over data array and print tweet
for tweet in data:
    #print(json.dumps(tweet, indent=1))
    print(tweet['text'])
    print("\n_________________\n")
    #here tweet processing can be done
