@echo off

REM Archivo de parámetros
set parameters_file=regression_custom.txt

REM Valores para iterar
set population_sizes=50 100 500
set crossover_probabilities=0.5 0.6 0.7 0.8 0.9 1.0
set mutation_probabilities=0.0 0.1 0.2
set max_genome_lengths=50 100 500
set max_wraps=0 1 2
set tournament_sizes=2 3 5

REM Bucle anidado para iterar sobre los parámetros
for %%A in (%population_sizes%) do (
    for %%B in (%crossover_probabilities%) do (
        for %%C in (%mutation_probabilities%) do (
            for %%D in (%max_genome_lengths%) do (
                for %%E in (%max_wraps%) do (
                    for %%F in (%tournament_sizes%) do (
                        REM Ejecutar el archivo ponyge.py con los parámetros
                        python ponyge.py --parameters %parameters_file% ^
                            --population_size %%A ^
                            --crossover_probability %%B ^
                            --mutation_probability %%C ^
                            --max_genome_length %%D ^
                            --max_wraps %%E ^
                            --tournament_size %%F
                    )
                )
            )
        )
    )
)
