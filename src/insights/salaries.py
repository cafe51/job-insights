from typing import Union, List, Dict
# from jobs import read
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
    # return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    return min(get_salaries(path))


def is_digit(value):
    return str((value)).strip().replace('-', '').isdigit()


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:

    if ("min_salary" not in job or "max_salary" not in job):
        raise ValueError()

    if (not is_digit(job["min_salary"]) or not is_digit(job["max_salary"])):
        raise ValueError()

    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError()

    if (
            not isinstance(salary, str)
            and not isinstance(salary, int)
            and not is_digit(salary)):
        raise ValueError()

    # if (isinstance(salary, str) and not is_digit(salary)):
    #     raise ValueError()

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


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

# jobs = [
#     {"max_salary": 10000, "min_salary": 200},
#     {"max_salary": 1500, "min_salary": 0},
# ]

# [False, False, False, True, True, False, False],
# [True, True, True, True, False, False, False],
# invalid_types = [None, "", "aloha", [], {}, lambda: 1]

# salaries = [0, 1, 5, 1000, 2000, -1, -2]


# for salarie in salaries:
#     print(
#         matches_salary_range({"max_salary": 1500, "min_salary": 0}, salarie
#                              ))


# print(matches_salary_range({"max_salary": "1000"}, 10))
