import pandas as pd


def importing_datasets():
    train = pd.read_csv("./datasets/train.csv")
    campaign_data = pd.read_csv("./datasets/campaign_data.csv")
    item_data = pd.read_csv("./datasets/item_data.csv")
    coupon_item = pd.read_csv("./datasets/coupon_item_mapping.csv")
    customer_demographics = pd.read_csv("./datasets/customer_demographics.csv")
    return train, campaign_data,item_data, coupon_item, customer_demographics
if __name__ == "__main__":
    train, campaign_data,item_data, coupon_item, customer_demographics = importing_datasets()
    print(train)
