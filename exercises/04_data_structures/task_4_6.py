# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Для этого использовать шаблон template и подставить в него значения из строки
ospf_route. Значения из строки ospf_route надо получить с помощью Python.

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
template = """
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}
"""

ipadd = ospf_route[6:18]
metr = ospf_route[20:26]
nhop = ospf_route[32:41]
lupd = ospf_route[43:48]
intf = ospf_route[50:]

template = {'Prefix': ipadd, 'AD/Metric' : metr,'Next-Hop' : nhop, 'Last update' : lupd,'Outbound Interface' : intf}

template = (f" Prefix: {ospf_route.split()[0]:>27} \n AD/Metric: {ospf_route.split()[1]:>24} \n Next-Hop: {ospf_route.split()[3]:>26} \n Last update: {
     ...: ospf_route.split()[4]:>23} \n Outbound Interface: {ospf_route.split()[5]}")
 
 Prefix:                10.0.24.0/24 
 AD/Metric:                 [110/41] 
 Next-Hop:                 10.0.13.3, 
 Last update:                  3d18h, 
 Outbound Interface: FastEthernet0/0

