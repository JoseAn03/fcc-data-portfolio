import pandas as pd

def calculate_demographic_data(print_data=True):
    # Columnas del dataset
    columns = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]

    # En freeCodeCamp el archivo ya tiene headers, pero por si acaso
    try:
        df = pd.read_csv("adult.data.csv")
        # Si la primera columna se lee como 'age', tiene headers
        if df.columns[0] != 'age':
            raise ValueError
    except:
        df = pd.read_csv("adult.data.csv", names=columns, skipinitialspace=True)

    # 1. ¿Cuántas personas de cada raza?
    race_count = df['race'].value_counts()

    # 2. Edad promedio de los hombres
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentaje con licenciatura (Bachelors)
    total = len(df)
    bachelors = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors / total) * 100, 1)

    # 4. Porcentaje con educación avanzada que ganan >50K
    advanced_edu = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    advanced_high_salary = len(advanced_edu[advanced_edu['salary'] == '>50K'])
    higher_education_rich = round((advanced_high_salary / len(advanced_edu)) * 100, 1)

    # 5. Porcentaje sin educación avanzada que ganan >50K
    no_advanced = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    no_advanced_high_salary = len(no_advanced[no_advanced['salary'] == '>50K'])
    lower_education_rich = round((no_advanced_high_salary / len(no_advanced)) * 100, 1)

    # 6. Mínimo de horas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentaje de los que trabajan el mínimo de horas y ganan >50K
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    rich_min_workers = len(df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')])
    rich_percentage = round((rich_min_workers / num_min_workers) * 100, 1)

    # 8. País con el porcentaje más alto de personas que ganan >50K
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_total = df['native-country'].value_counts()
    country_percent = (country_salary / country_total * 100).dropna()
    highest_earning_country = country_percent.idxmax()
    highest_earning_country_percentage = round(country_percent.max(), 1)

    # 9. Ocupación más popular para quienes ganan >50K en India
    india_high = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_high['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
