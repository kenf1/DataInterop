#convert Scrape.ipynb to .py
import pandas as pd
import polars as pl

src = "https://en.wikipedia.org/wiki/Python_(programming_language)"
loc = 1

# temp = pd.read_html(src)
# pl_ver = pl.from_pandas(temp[1])

def scrape(src,loc):
    src = src
    temp = pd.read_html(src)
    pl_ver = pl.from_pandas(temp[loc])
    return pl_ver

#don't need to include file extension
# use write_csv for polars df
def save2csv(df,name):
    df.write_csv(f"./data/{name}.csv")
    
if __name__ == "__main__":
    df = scrape(src,loc)
    save2csv(df,"example")
    print("Success")
    