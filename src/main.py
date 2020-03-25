import os
import click
import pandas as pd
import pathlib
from downloading_fulltext import save_fulltext
from downloading_metadata import save_json
import multiprocessing


def build_urls_path(dataset):
    """
    Builds the path to the desired URLs dataset
    :param dataset: string
    :return: string
    """

    this_file = os.path.abspath(__file__)
    this_folder = os.path.dirname(this_file)
    datasets_path = pathlib.Path(this_folder) / ".." / 'datasets'

    if dataset == 'inventory':
        return datasets_path / 'inv_urls.csv'
    if dataset == 'repatriation':
        return datasets_path / 'repatriation_urls.csv'


def start_parallel_job(func, urls, keys):
    """
    Starts a data retrieval job, with the desired function set of urls and keys
    :param func: callable
    :param urls: iterable
    :param keys: iterable
    """

    job_input = list(zip(urls, keys))
    job_workers = multiprocessing.cpu_count() * 2
    job_chunksize = len(job_input) // job_workers

    with multiprocessing.Pool(job_workers) as p:
        p.starmap(func, job_input, job_chunksize)


@click.group()
def main():
    pass


@main.command()
@click.option('--dataset', nargs=1, type=str)
def fulltext(dataset):
    urls_path = build_urls_path(dataset)
    urls_data = pd.read_csv(urls_path)

    start_parallel_job(
        func=save_fulltext,
        urls=urls_data['fulltext_url'],
        keys=urls_data['key'],
    )


@main.command()
@click.option('--dataset', nargs=1, type=str)
def metadata(dataset):
    urls_path = build_urls_path(dataset)
    urls_data = pd.read_csv(urls_path)

    start_parallel_job(
        func=save_json,
        urls=urls_data['json_url'],
        keys=urls_data['key'],
    )


if __name__ == "__main__":
    main()
