from src.pre_built.sorting import sort_by
from src.insights.jobs import read


def test_sort_by_criteria():
    results = ['383416', '19857', "2020-05-08"]
    criteria = ["max_salary", "min_salary", "date_posted"]
    jobs = read('data/jobs.csv')

    for index in range(len(criteria)):
        sort_by(jobs, criteria[index])
        assert jobs[0][criteria[index]] == results[index]
