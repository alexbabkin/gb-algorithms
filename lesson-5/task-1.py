"""
    1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия. 
    Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, 
    чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Company = namedtuple("Company", "name, p_mean")
comp_count = int(input("Введите количество предприятий: "))

companies = []
for i in range(comp_count):
    comp_name = input("Введите название предприятия: ")
    profits = [
        float(input(f"Введите прибыль за квартал {j+1}: ")) for j in range(4)]
    companies.append(Company(comp_name, sum(profits)/4))

print(companies)
p_mean_over_all = sum([c.p_mean for c in companies]) / comp_count
print("Предприятния с прибылью ниже среднего: ", [
      c.name for c in companies if c.p_mean < p_mean_over_all])
print("Предприятния с прибылью выше среднего: ", [
      c.name for c in companies if c.p_mean > p_mean_over_all])
