import pandas as pd
import matplotlib.pyplot as plt

steel_df = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')
wood_df = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')


# function to plot rankings over time for 1 roller coaster:
def rank_over_time(coaster, park, lst):
    list_of_ranks = lst[(lst['Name'] == coaster) & (lst['Park'] == park)]
    ax = plt.subplot()
    plt.plot(list_of_ranks['Year of Rank'], list_of_ranks['Rank'], marker='s')
    ax.set_yticks(list_of_ranks['Rank'].values)
    ax.set_xticks(list_of_ranks['Year of Rank'].values)
    plt.title('{} Rankings'.format(coaster))
    plt.xlabel('Year')
    plt.ylabel('Rankings')
    ax.invert_yaxis()
    plt.show()


# function to plot rankings over time for 2 roller coasters
def rank_2_over_time(coaster1, coaster2, park1, park2, lst):
    list_of_ranks_1 = lst[(lst.Name == coaster1) & (lst.Park == park1)]
    list_of_ranks_2 = lst[(lst.Name == coaster2) & (lst.Park == park2)]

    plt.figure(figsize=(10, 8))
    ax = plt.subplot()

    plt.plot(list_of_ranks_1['Year of Rank'], list_of_ranks_1.Rank, marker='o')
    plt.plot(list_of_ranks_2['Year of Rank'], list_of_ranks_2.Rank, marker='o')

    plt.title('{} vs {} Rankings'.format(coaster1, coaster2))
    plt.xlabel('Year')
    plt.ylabel('Ranking')

    ax.invert_yaxis()

    plt.legend([coaster1, coaster2])

    plt.show()


# function to plot the top n rankings for a dataframe
def plot_top_n(lst, n):
    list_of_ranks = lst[lst.Rank <= n]

    for each in set(list_of_ranks.Name):
        coaster = list_of_ranks[list_of_ranks.Name == each]
        ax = plt.subplot()
        plt.plot(coaster['Year of Rank'], coaster.Rank, marker='o')
        ax.invert_yaxis()
        ax.set_yticks(coaster.Rank)
        ax.set_xticks(coaster['Year of Rank'])
        plt.title('{} Rankings'.format(each))
        plt.xlabel('Year')
        plt.ylabel('Rank')

        plt.show()


# load data of statistics of roller coasters
coasters = pd.read_csv('roller_coasters.csv')
print(coasters.head())
# function to plot histogram of a numeric variable in a data frame


def plot_histogram(dataframe, variable):
    plt.hist(dataframe[variable])
    plt.xlabel(variable)
    plt.ylabel('Count')
    plt.title('{} Count'.format(variable))
    plt.show()

# function to plot a bar chart of the number of inversions of the roller-coasters at a park


def plot_bar(dataframe, park_name):
    list_of_coasters = dataframe[dataframe.park == park_name]
    list_of_coasters = list_of_coasters.sort_values(
        'num_inversions', ascending=False)
    coaster_names = list_of_coasters.name
    inversions = list_of_coasters.num_inversions
    plt.figure(figsize=(10, 8))
    plt.bar(range(len(coaster_names)), inversions)
    ax = plt.subplot()
    ax.set_xticks(range(len(coaster_names)))
    ax.set_xticklabels(coaster_names, rotation=90)
    plt.xlabel('Coaster')
    plt.ylabel('Number of Inversions')
    plt.title('Number of inversions for the roller-coasters at {}'.format(park_name))
    plt.show()

# function to plot the operating status of roller-coasters in a dataframe


def operating_status(dataframe):
    operating_list = dataframe[dataframe.status == 'status.operating']
    not_operating_list = dataframe[dataframe.status ==
                                   'status.closed.definitely']
    num_operating = len(operating_list)
    num_not_operating = len(not_operating_list)
    data = [num_operating, num_not_operating]
    plt.pie(data, explode=[0.0, 0.1], autopct='%0.2f%%',
            labels=['Operating', 'Not Operating'])
    plt.title('Operating vs Not Operating Roller-Coasters')
    plt.axis('equal')
    plt.show()


# function to plot a scatter plot of two numeric variables of a dataframe
def plot_scatter(dataframe, column_1, column_2):
    x_values = dataframe[column_1].values
    y_values = dataframe[column_2].values
    plt.scatter(x_values, y_values)
    plt.title('Scatter plot of {} vs {}'.format(column_1, column_2))
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.show()
