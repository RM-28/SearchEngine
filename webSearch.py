import pandas as pd
from duckduckgo_search import DDGS

print("Enter a prompt: ")
search_query = input()
results = DDGS().text(keywords=search_query,region='wt-wt',safesearch="off",timelimit="7d",max_results=3)

results_df = pd.DataFrame(results)
results_df.to_csv("./results/website.csv",index = False)