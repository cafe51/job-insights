from typing import List, Dict
# from src.insights.jobs import read
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    return list(set([element['industry']
                for element in read(path)
                if element['industry']]))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    if industry not in get_unique_industries('data/jobs.csv'):
        return []

    job_list = [element for
                element in jobs
                if element['industry'] == industry
                and bool(element['job_type'])]

    return job_list
