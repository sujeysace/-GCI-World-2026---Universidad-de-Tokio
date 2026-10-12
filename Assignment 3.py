def homework(anime_data, metric_column, n):
    df = anime_data.copy()
    df["rank"] = df[metric_column].rank(method="first", ascending=False)
    labels = [f"Group {i}" for i in range(1, n + 1)]
    df["group"] = pd.qcut(df["rank"], q=n, labels=labels)
    
    total_sum = df[metric_column].sum()
    group_sums = df.groupby("group", observed=False)[metric_column].sum()
    proportions = group_sums / total_sum
    
    return proportions.sort_values(ascending=False)
