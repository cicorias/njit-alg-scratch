



Undirected	37,700	289,003	Social network of Github developers.
https://snap.stanford.edu/data/github-social.html


Undirected	4,039	88,234	Social circles from Facebook (anonymized)
https://snap.stanford.edu/data/ego-Facebook.html


Weighted, Signed, Directed, Temporal	5,881	35,592	Bitcoin OTC web of trust network
https://snap.stanford.edu/data/soc-sign-bitcoin-otc.html



 Name | Directed | Nodes | Edges | Weights | Weight range | Weight skew | cite 
---|---|---|---|---|---|---|---
 Bitcoin OTC trust weighted signed network | Yes | 5881 | 35592 | Yes | \-10 \- \+10 | 89% positive | TBD 
 Social circles: Facebook | No | 4039 | 88234 | No |  |  | TBD 
 GitHub Social Network | No | 37700 | 289003 | No |  |  | TBD 


ddd
ddd
> Note:


 Name | Directed | Nodes | Edges | Weights | Weight range | Weight skew | Description | cite 
---|---|---|---|---|---|---|---|---
 Bitcoin OTC trust weighted signed network | Yes | 5881 | 35592 | Yes | \-10 \- \+10 | 89% positive | This is who\-trusts\-whom network of people who trade using Bitcoin on a platform called Bitcoin OTC\. Since Bitcoin users are anonymous, there is a need to maintain a record of users' reputation to prevent transactions with fraudulent and risky users\. Members of Bitcoin OTC rate other members in a scale of \-10 \(total distrust\) to \+10 \(total trust\) in steps of 1\. This is the first explicit weighted signed directed network available for research\. | TBD 
 Social circles: Facebook | No | 4039 | 88234 | No |  |  | This dataset consists of 'circles' \(or 'friends lists'\) from Facebook\. Facebook data was collected from survey participants using this Facebook app\. The dataset includes node features \(profiles\), circles, and ego networks\. | TBD 
 GitHub Social Network | No | 37700 | 289003 | No |  |  | A large social network of GitHub developers which was collected from the public API in June 2019\. Nodes are developers who have starred at least 10 repositories and edges are mutual follower relationships between them\. The vertex features are extracted based on the location, repositories starred, employer and e\-mail address\. The task related to the graph is binary node classification \- one has to predict whether the GitHub user is a web or a machine learning developer\. This target feature was derived from the job title of each user\. | TBD 

