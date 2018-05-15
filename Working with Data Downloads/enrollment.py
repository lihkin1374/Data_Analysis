if __name__ == "__main__":
    import pandas as pd
    dat = pd.read_csv("data/CRDC2013_14.csv", encoding = "Latin-1")
    dat["total_enrollment"] = dat["TOT_ENR_M"] + dat["TOT_ENR_F"]
    all_enrollment = dat["total_enrollment"].sum()
    
