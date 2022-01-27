from GDPlinearregres import GDP_estimated
from imports import *

df = pd.read_csv(r"..\CSV files\df_Full_DataBase.csv")
GDP_est = pd.read_csv(r"..\CSV files\GDP est.csv")

# Dictionary with countries and color (very pretty, much wow!)
Color_By_Country = {
    "United States": "b",
    "China": "r",
    "United Kingdom": "orchid",
    "Germany": "grey",
    "India": "orange",
    "France": "navy",
    "Japan": "firebrick",
    "Canada": "bisque",
    "Italy": "lime",
    "Australia": "indigo",
    "Sweden": "gold",
    "Others": "olive",
    "South Korea": "pink",
    "Brazil": "cyan",
    "South Sudan": "tan",
    "Turkey": "chocolate",
    "Mexico": "cyan",
    "Spain": "yellow",
    "Netherlands": "plum",
    "Russia": "wheat",
    "Indonesia": "darkgreen",
    "Switzerland": "darkblue",
    "Saudi Arabia": "darkred",
}

ARR_COLOR = [
    "red",
    "teal",
    "orange",
    "grey",
    "green",
    "yellow",
    "blue",
    "purple",
    "pink",
    "brown",
    "cyan",
    "darkgreen",
    "magenta",
    "tan",
    "aqua",
    "tomato",
    "chocolate",
    "olive",
    "gold",
    "plum",
    "wheat",
    "lime",
]


# def plot_frequent_elements(df, df_in_params):
#     col_amount = df_in_params.shape[0]
#     fig, axes = plt.subplots(1, col_amount, figsize=(20, 5))
#
#     for i in range(col_amount):
#         sr = get_frequent_elements(df,df_in_params['col_name'][i],df_in_params['num_top_elements'][i])
#         one_dim_plot(sr,df_in_params['plot_type'][i],axes[i])


# line plot
def line_plot(df):
    # fig, axes = plt.subplots(1, 1, figsize=(20, 5))

    x = df[df["Country"] == "Israel"]["GDP Total"]

    arr = list(x)
    plt.plot(arr, linestyle="dotted")
    plt.show()


def pie_per_year(ax, df, year):
    GDP = []
    labels = []
    df = df[df["Year"] == year]
    df = df.sort_values(by="GDP Total", ascending=False)
    df = df[["Country", "GDP Total"]]
    for c in df.head(15).values:
        GDP.append(c[1])
        labels.append(c[0])
    GDP.append(df["GDP Total"].sum() - df.head(15)["GDP Total"].sum())
    labels.append("Others")
    ax.pie(
        GDP,
        labels=labels,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=[Color_By_Country[key] for key in labels],
    )

    ax.set_title("GDP in %d" % year)
    return ax


def GDP_pie_plot():
    """Displays GDP plot pie
    Args:
        None
    Returns:
        None ()
    """
    # Create Subplot
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))

    # Get GDP estimates
    df_2030 = GDP_estimated()

    index = 0
    for i in [1960, 2020]:
        ax[index] = pie_per_year(ax[index], df[df["Year"] == i], i)
        index += 1

    ax[index] = pie_per_year(ax[index], df_2030, 2030)
    fig.suptitle("GDP in 1960 VS 2020 VS 2030")
    plt.show()

    # Pie chart containt all other countries (not top 15)
    df_2020 = df[df["Year"] == 2020].sort_values(by="GDP Total", ascending=False)
    df_2020 = df_2020[["Country", "GDP Total"]]
    df_2020 = df_2020.tail(-15)
    sum_of_gdp_2020 = df_2020["GDP Total"].sum()

    df_2020 = df_2020[df_2020["GDP Total"] >= 250000000000]

    others_gdp = []
    others_gdp_names = []

    # Extract data from 2020
    for c in df_2020.values:
        others_gdp.append(c[1])
        others_gdp_names.append(c[0])

    others_gdp.append(sum_of_gdp_2020 - df_2020["GDP Total"].sum())
    others_gdp_names.append("Others")

    plt.pie(
        others_gdp,
        labels=others_gdp_names,
        shadow=True,
        startangle=90,
        autopct="%1.1f%%",
        colors=ARR_COLOR,
    )
    # plt.legend(loc="best")
    plt.title("GDP in 2020 (Others)")
    plt.show()


# pie chart
def mix_plot(df):
    # ##check third_world vs other
    #
    # countries_name=df["Country"].unique()
    # third_world=not_third_world=0
    # for c in countries_name:
    #     if df[df["Country"]==c]["Third World"].unique()[0]:
    #         third_world+=1
    #     else:
    #         not_third_world+=1
    #
    # plt.pie([third_world,not_third_world],labels=["Third World","Other"])
    # plt.show()

    #
    # ##check Least Developed vs other
    #
    # countries_name = df["Country"].unique()
    # least_dev = not_least_dev = 0
    # for c in countries_name:
    #     if df[df["Country"] == c]["Least Developed Country"].unique()[0]:
    #         least_dev += 1
    #     else:
    #         not_least_dev += 1
    #
    # plt.pie([(least_dev/(least_dev+not_least_dev))*100, (not_least_dev/(least_dev+not_least_dev))*100], labels=["Least Developed Country", "Other"], autopct='%1.1f%%')
    # plt.title("Least developed countries VS rest of the world")
    # plt.show()

    #
    #
    # ## bar plot check how much of third_world is least developed countries
    # x=np.array([least_dev, third_world])
    # plt.bar(["Least Developed Country", "Total Third World"],x)
    # plt.show()
    #
    #
    #

    # show continent pie

    dict = {
        "Asia": 0,
        "Europe": 0,
        "Oceania": 0,
        "Africa": 0,
        "Central America": 0,
        "North America": 0,
        "South America": 0,
    }
    total = 0
    for c in df["Country"].unique():
        dict[df[df["Country"] == c]["Continent"].unique()[0]] += 1
        total += 1

    plt.pie(
        [
            (dict["Asia"] / total) * 100,
            (dict["Europe"] / total) * 100,
            (dict["Oceania"] / total) * 100,
            (dict["Africa"] / total) * 100,
            (dict["Central America"] / total) * 100,
            (dict["North America"] / total) * 100,
            (dict["South America"] / total) * 100,
        ],
        labels=[
            "Asia",
            "Europe",
            "Oceania",
            "Africa",
            "Central America",
            "North America",
            "South America",
        ],
        autopct="%1.1f%%",
    )
    plt.title("Countries distribution between continents")
    plt.show()

    # x = list(df[df["Year"] == 2020]["Population Total"])  ## Population
    # y = list(df[df["Year"] == 2020]["GDP Total"])  ## GDP
    #
    # i = 0
    # for continent in df["Continent"].unique():
    #     x = list(
    #         df[(df["Continent"] == continent) & (df["Year"] == 2020)][
    #             "Population Total"
    #         ]
    #     )
    #     y = list(df[(df["Continent"] == continent) & (df["Year"] == 2020)]["GDP Total"])
    #     plt.scatter(x, y, color=ARR_COLOR[i])
    #
    #     i += 1
    # plt.title("GDP/Population in 2020 With Continents")
    # plt.xlabel("Population")
    # plt.ylabel("GDP")
    # plt.legend(df["Continent"].unique(), loc="upper left")
    # plt.show()

    # Create GDP vs continents bar
    list_gdp = []
    for c in df["Continent"].unique():
        list_gdp.append(df[df["Continent"] == c]["GDP Total"].mean())

    plt.bar(df["Continent"].unique(), list_gdp, color=ARR_COLOR)
    plt.xlabel("Continents")
    plt.ylabel("GDP Total")
    plt.title("Continents vs GDP")
    plt.show()

    #
    # i = 0
    # for contint in df["Continent"].unique():
    #     x = []
    #     y = []
    #     for year in range(
    #         min(df[df["Continent"] == contint]["Year"]),
    #         max(df[df["Continent"] == contint]["Year"]),
    #     ):
    #         x.append(
    #             (
    #                 df[(df["Continent"] == contint) & (df["Year"] == year)][
    #                     "GDP Total"
    #                 ].median()
    #             )
    #         )
    #         y.append(year)
    #     plt.plot(y, x, color=ARR_COLOR[i])
    #     i += 1
    #
    # plt.xlabel("Year")
    # plt.ylabel("GDP")
    # plt.legend(df["Continent"].unique(), loc="upper left")
    # plt.title("AVG GDP per continent along 1960-2020")
    # plt.show()


def Stack_GDP(ax, df):
    """Stack GDP inorder to show stacked bar chart
    Args:
        ax: ax of the plot
        df: dataframe
    Returns:
        None
    """
    gdp_sum = 0
    for c in df["Country"].head(10).unique():
        ax.bar(
            df["Year"].unique(),
            df[df["Country"] == c]["GDP Total"],
            width=0.1,
            bottom=gdp_sum,
            color=Color_By_Country[c],
            label=c,
        )
        # Add text to each stack
        ax.text(
            df["Year"].unique(),
            gdp_sum + 100,
            "%.02f" % df[df["Country"] == c]["GDP Total"].sum(),
            ha="center",
            va="bottom",
        )
        gdp_sum += df[df["Country"] == c]["GDP Total"].sum()

    # Sum up the other countries (not in top 10)
    ax.bar(
        df["Year"].unique(),
        df["GDP Total"].sum() - gdp_sum,
        width=0.1,
        bottom=gdp_sum,
        color=Color_By_Country["Others"],
        label="Others",
    )
    ax.text(
        df["Year"].unique(),
        gdp_sum + 100,
        "%.02f" % (df["GDP Total"].sum() - gdp_sum),
        ha="center",
        va="bottom",
    )

    ax.set_ylabel("GDP")
    ax.set_title("GDP in 1960\n%.02f$" % df["GDP Total"].sum())
    ax.legend()
    return ax


def sum_of_gdp_bar_graph():
    """displays GDP stacked bar graph
    Args:
        None
    Returns:
        None
    """

    labels = ["1960", "2020", "2030"]
    fig, ax = plt.subplots(1, 3, figsize=(20, 5))

    index = 0
    for i in [1960, 2020]:
        ax[index] = Stack_GDP(
            ax[index],
            df[df["Year"] == i].sort_values(by=["GDP Total"], ascending=False),
        )
        index += 1
    ax[index] = Stack_GDP(
        ax[index],
        GDP_est[GDP_est["Year"] == 2030].sort_values(by=["GDP Total"], ascending=False),
    )

    plt.show()


def GDP_total_world_graph():
    """Display Graph Showing the total GDP of the world per year(line graph)

    Args:
        df
    Returns:
        displays graph
    """
    # Variable initialization
    arr = []
    country_list = []
    i = 0

    # Summing up each year total GDP
    GDP_total_world = [
        df[df["Year"] == year]["GDP Total"].sum() for year in df["Year"].unique()
    ]

    # Extract year 2020 and sort by GDP
    df_2020 = df[df["Year"] == 2020].sort_values(by=["GDP Total"], ascending=False)

    # Extract the top 10 coutries
    for c in df_2020["Country"].head(10).unique():
        arr.append(
            [
                df[(df["Country"] == c) & (df["Year"] == year)]["GDP Total"].sum()
                for year in df["Year"].unique()
            ]
        )
        country_list.append(c)

    fig, ax = plt.subplots(1, 1, figsize=(20, 5))
    ax.plot(df["Year"].unique(), GDP_total_world, label="World")
    # Add the top countries in 2020 to graph
    for j in arr:
        ax.plot(
            df["Year"].unique(),
            j,
            label=df_2020.head(10)["Country"].unique()[i],
            color=Color_By_Country[country_list[i]],
        )
        i += 1

    plt.xlabel("Year")
    plt.ylabel("World GDP Total")
    plt.title("World GDP Growth")
    ax.legend()
    plt.show()


# Driver Code:
if __name__ == "__main__":
    df = df.fillna(0)
    # line_plot(df)
    # mix_plot(df)
    GDP_pie_plot()
    sum_of_gdp_bar_graph()
    GDP_total_world_graph()
