import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from datasets.custom.data_creator import f1, f2, f3, f4
from src.fitness.supervised_learning.supervised_learning import KG, KP, KS


def juntar_resultados():
    df = pd.DataFrame(columns=
                      'pop_size cross_prob mut_prob max_genome_len max_wraps tournament generation phenotype genotype '
                      'fitness function dir'.split(' '))
    dics = glob.glob('results/_/DESKTOP*')
    for dic in dics:
        with open(dic + "/parameters.txt", "r") as file:
            # Lee todas las líneas del archivo
            lines = file.readlines()

        population_sizes = int(lines[44].split(' ')[-1].strip())
        crossover_probabilities = float(lines[5].split(' ')[-1].strip())
        mutation_probabilities = float(lines[38].split(' ')[-1].strip())
        max_genome_lengths = int(lines[27].split(' ')[-1].strip())
        max_wraps = int(lines[31].split(' ')[-1].strip())
        tournament_sizes = int(lines[63].split(' ')[-1].strip())
        func = lines[8].split('/')[-1].split('_')[0]

        with open(dic + "/best.txt", "r") as file:
            # Lee todas las líneas del archivo
            lines = file.readlines()

        generation = int(lines[1])
        phenotype = lines[4].strip()
        genotype = [int(x) for x in lines[7].strip("[]\n").split(", ")]
        fitness = float(lines[12])

        df.loc[len(df)] = [population_sizes, crossover_probabilities, mutation_probabilities, max_genome_lengths,
                           max_wraps, tournament_sizes, generation, phenotype, genotype, fitness, func, dic]

    df.to_csv('results/results_.csv')


def main(file):
    df = pd.read_csv('results/' + file, index_col=0)

    df1 = df[df.function == 'f1']
    df2 = df[df.function == 'f2']

    # print(df1.sort_values(by='fitness')['phenotype'].iloc[0])
    # print(df2.sort_values(by='fitness')['phenotype'].iloc[0])

    # calculamos el fitness medio entre ejecuciones

    media_df1 = df1.groupby(list(df1.columns)[:6]).mean()['fitness']
    media_df2 = df2.groupby(list(df2.columns)[:6]).mean()['fitness']

    print(media_df1.sort_values().head(10))
    print(media_df2.sort_values().head(10))

    print(media_df1.sort_values().tail(20))
    print(media_df2.sort_values().tail(20))

    # pop_size 500 mut_prob 0.1 resto ??
    # decido cross_prob 0.9 max_genom_len 500 max_wraps 1 tournament 5


def plot_f(file, func):
    pop_size = 500
    mut_prob = 0.1
    cross_prob = 0.9
    max_genome_len = 500
    max_wraps = 1
    tournament = 5

    num = 41
    if func == 'f1':
        interval = [-2, 4]
        num = 61
        f = f1
    elif func == 'f2':
        interval = [-1, 3]
        f = f2
    elif func == 'f3':
        interval = [0, 4]
        f = f3
    else:
        interval = [0, 4]
        f = f4

    df = pd.read_csv('results/' + file, index_col=0)
    df_loc = df[df.pop_size == pop_size]
    df_loc = df_loc[df_loc.mut_prob == mut_prob]
    df_loc = df_loc[df_loc.cross_prob == cross_prob]
    df_loc = df_loc[df_loc.max_genome_len == max_genome_len]
    df_loc = df_loc[df_loc.max_wraps == max_wraps]
    df_loc = df_loc[df_loc.tournament == tournament]
    df_loc = df_loc[df_loc.function == func]

    expr = df_loc.sort_values('fitness')['phenotype'].values[0]
    print(expr)
    print(df_loc.sort_values('fitness')['fitness'].values[0])

    x = np.linspace(interval[0], interval[1], num).reshape(num, 1)
    ys = f(x)
    y_hats = eval(expr)

    plt.plot(x, y_hats)
    plt.plot(x, ys)
    plt.legend(['y_hat', 'y'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == '__main__':


    df = pd.read_csv('results/results_f3_f4.csv', index_col=0)
    print(df[['function', 'fitness']])
    # main('results.csv')

    plot_f('results.csv', 'f1')
    plot_f('results.csv', 'f2')
    plot_f('results_f3_f4.csv', 'f3')
    plot_f('results_f3_f4.csv', 'f4')
    plot_f('results_local_f4.csv', 'f4')
    plot_f('results_mo_f4.csv', 'f4')
