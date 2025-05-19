import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    df.columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education_num',
        'marital_status', 'occupation', 'relationship', 'race',
        'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
        'native_country', 'income'
    ]
    df = df.map(lambda x: x.strip().title() if isinstance(x, str) else x)
    return df

def count_high_earners(df):
    return int(df['income'].value_counts().get('>50K', 0))


def average_age_by_gender(df, gender):
    return df[df['sex'] == gender]['age'].mean()

def race_counts(df):
    return df['race'].value_counts()

def percentage_bachelors(df):
    return (df['education'] == 'Bachelors').mean() * 100

def percentage_high_income_advanced_education(df):
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    adv_df = df[df['education'].isin(advanced)]
    return (adv_df['income'] == '>50K').mean() * 100

def percentage_high_income_non_advanced(df):
    advanced = ['Bachelors', 'Masters', 'Doctorate']
    non_adv_df = df[~df['education'].isin(advanced)]
    return (non_adv_df['income'] == '>50K').mean() * 100

def min_work_hours(df):
    return df['hours_per_week'].min()

def percentage_rich_min_hours(df):
    min_hours = df['hours_per_week'].min()
    min_workers = df[df['hours_per_week'] == min_hours]
    return (min_workers['income'] == '>50K').mean() * 100

def country_with_highest_rich_percentage(df):
    total = df['native_country'].value_counts()
    rich = df[df['income'] == '>50K']['native_country'].value_counts()
    percentage = (rich / total) * 100
    return percentage.idxmax(), percentage.max()

def most_common_high_income_occupation_india(df):
    india_rich = df[(df['native_country'] == 'India') & (df['income'] == '>50K')]
    return india_rich['occupation'].value_counts().idxmax()
