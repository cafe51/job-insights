from typing import Union, List, Dict
from src.insights.jobs import read


def get_salaries(path: str) -> List[int]:
    jobs = read(path)
    max_salaries = [int(element['max_salary'])
                    for element in jobs
                    if element['max_salary'].isdigit()]
    min_salaries = [int(element['min_salary'])
                    for element in jobs
                    if element['min_salary'].isdigit()]
    return max_salaries + min_salaries


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    return max(get_salaries(path))


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(get_salaries(path))


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greater than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (not bool(job["min_salary"]) or
            not bool(job["max_salary"])):
        raise ValueError()

    if (not job["min_salary"].strip().isnumeric() or
            not job["max_salary"].strip().isnumeric()):
        raise ValueError()

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError()

    if (not salary["max_salary"].strip().isnumeric()):
        raise ValueError()

    response = int(job['min_salary']) <= int(salary) <= int(job['max_salary'])
    return response


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
