#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    csv.register_dialect('empDialect',skipinitialspace=True,strict=True)
    employee_file=csv.DictReader(open(csv_file_location),dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

employee_list = read_employees('/home/rduguet/Escritorio/cuarentena_python/empleados.csv')


def process_data(employee_list):
    department_list=[]
    for employee_data in employee_list:
        department_list.append(employee_data['departamento'])
        department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)
print(dictionary)

def reporte(dictionary,report_file):
    with open(report_file,'w+') as f:
        for k in sorted(dictionary):
            f.write(str(k)+' : '+str(dictionary[k])+'\n')
        f.close()

reporte(dictionary,'/home/rduguet/Escritorio/cuarentena_python/empleados.csv')