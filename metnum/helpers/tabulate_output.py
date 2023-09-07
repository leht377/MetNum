from tabulate import tabulate


def tabulate_output(historial: dict):
    table = tabulate(historial, headers='keys',
                     tablefmt='grid', showindex=True)
    print(table)
