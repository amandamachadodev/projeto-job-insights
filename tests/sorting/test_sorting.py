from src.insights import get_max_salary, get_min_salary
from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    path = "src/jobs.csv"
    jobs = read(path)

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == str(get_min_salary(path))

    sort_by(jobs, "max_salary")
    assert jobs[0]["max_salary"] == str(get_max_salary(path))
