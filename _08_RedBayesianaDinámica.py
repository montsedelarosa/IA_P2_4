# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

pip install pgmpy

from pgmpy.models import DynamicBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import DBNInference

# Crear la estructura de la DBN
model = DynamicBayesianNetwork()

# Definir las variables
model.add_edges_from([(('A', 0), ('B', 0)), (('A', 0), ('A', 1)), (('B', 0), ('B', 1))])

# Definir las distribuciones de probabilidad condicional (CPD)
cpd_A_0 = TabularCPD(variable='A', variable_card=2, values=[[0.7], [0.3]])
cpd_A_1 = TabularCPD(variable='A', variable_card=2, values=[[0.8], [0.2]], evidence=[('A', 0)], evidence_card=[2])
cpd_B_0 = TabularCPD(variable='B', variable_card=2, values=[[0.9, 0.6], [0.1, 0.4]])
cpd_B_1 = TabularCPD(variable='B', variable_card=2, values=[[0.7, 0.1], [0.3, 0.9]], evidence=[('B', 0)], evidence_card=[2])

model.add_cpds(cpd_A_0, cpd_A_1, cpd_B_0, cpd_B_1)

# Verificar la consistencia del modelo
assert model.check_model()

# Crear un objeto de inferencia
inference = DBNInference(model)

# Realizar inferencia en el instante de tiempo 1
query_result = inference.query(variables=['B', 'A'], evidence={'B': 1})
print(query_result)
