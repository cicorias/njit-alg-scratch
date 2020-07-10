---
author: "Shawn CIcoria"
date: "July 11, 2020"
subject: "Miniproject 2 - Milestone 1"
class: "CS 610 Algorithms and Data Structures"
email: "sc2443@njit.edu"
---

# Introduction
For mini-project 2, I've initially selected the following three datasets:

1. Social circles from Facebook - https://snap.stanford.edu/data/ego-Facebook.html
2. Social network of GitHub developers - https://snap.stanford.edu/data/github-social.html
3. Bitcoin OTC web of trust network - https://snap.stanford.edu/data/soc-sign-bitcoin-otc.html


## Social circles from Facebook
This data set contains both raw and processed data. The raw data to be used is contained in `facebook_combined.txt` which has `88,234` rows of data with each row the connected nodes - essentially each row represents a connected edge.

Each node is identified by an integer in the rage of `0-4038`.

### Example data
An example set of rows shown below. The data set is tagged as undirected.

```csv
0 1
0 2
0 3
0 4
0 5
```

### Loading data as edges

```python
edges = import_data('./data/facebook_combined.txt', skip_header=False, sep=' ', cols=2)
print(len(edges)) # result is 88234
```

## Social network of GitHub developers
This data set contains both raw and processed data. The raw data to be used is contained in `musae_git_edges.csv` which has `289,003` rows of data with each row the connected nodes - again, the edges.

Each node is identified by an integer in the rage of `0-37,699`.

### Example data
An example set of rows shown below with first row a header. The data set is tagged as undirected.

```csv
id_1,id_2
0,23977
1,34526
1,2370
1,14683
```

### Loading data as edges

```python
# importing GitHub graph data
edges_github = import_data('./data/git_web_ml/musae_git_edges.csv', skip_header=True, sep=',', cols=2)
print(len(edges_github)). # 289003
```


## Bitcoin OTC web of trust network
This data is a directed graph with weights. Weights can be positive or negative (signed).

Data is contained in `soc-sign-bitcointotc.csv`. The file is headerless, with four values for each row. Each line has one rating, sorted by time, with the following format:

```
SOURCE, TARGET, RATING, TIME
```

SOURCE: node id of source, i.e., rater
TARGET: node id of target, i.e., ratee
RATING: the source's rating for the target, ranging from -10 to +10 in steps of 1
TIME: the time of the rating, measured as seconds since Epoch


Thus, our edges are the first two columns, with a direction and weight (rating).

Each node is identified by an integer in the rage of `0-5880`.

### Example of data

```csv
6,2,4,1289241911.72836
6,5,2,1289241941.53378
1,15,1,1289243140.39049
4,3,7,1289245277.36975
13,16,8,1289254254.44746
```

### Loading data as edges

```python
# import btc data
edges_btc = import_data('./data/soc-sign-bitcoinotc.csv', skip_header=False, sep=',', cols=3)
print(len(edges_btc)). # 35592
```

## Data Import function

```python
# importing graph data
def import_data(filename, skip_header = False, sep = ',', cols = 2):
    rv = []
    with open(filename, 'rt') as f:
        for line in f:
            if skip_header:
                skip_header = False
                continue
            rv.append(line.strip().split(sep)[0:cols])
            assert len(rv[len(rv) - 1]) == cols

    return rv

```


# Data Summary

 Name | Directed | Nodes | Edges
---|---|---|---|---
 Social circles: Facebook | No | 4,039 | 88,234
 GitHub Social Network | No | 37,700 | 289,003
 Bitcoin OTC trust weighted signed network | Yes | 5,881 | 35,592


## Data descriptions


 Name | Description
---|---
 Bitcoin OTC trust weighted signed network | This is who\-trusts\-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC\. Since Bitcoin users are anonymous, there is a need to maintain a record of users' reputation to prevent transactions with fraudulent and risky users\. Members of Bitcoin OTC rate other members in a scale of \-10 \(total distrust\) to \+10 \(total trust\) in steps of 1\. This is the first explicit weighted signed directed network available for research\. 
 Social circles: Facebook | This dataset consists of 'circles' \(or 'friends lists'\) from Facebook\. Facebook data was collected from survey participants using this Facebook app\. The dataset includes node features \(profiles\), circles, and ego networks\.
 GitHub Social Network | A large social network of GitHub developers which was collected from the public API in June 2019\. Nodes are developers who have starred at least 10 repositories and edges are mutual follower relationships between them\. The vertex features are extracted based on the location, repositories starred, employer and e\-mail address\. The task related to the graph is binary node classification \- one has to predict whether the GitHub user is a web or a machine learning developer\. This target feature was derived from the job title of each user\. 



