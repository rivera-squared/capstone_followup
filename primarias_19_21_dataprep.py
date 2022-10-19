# Creating dataset to follow up my capstone's study
import pandas as pd
import numpy as np
import scipy

primarias = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/educacion_db/main/primarias_2021.csv')
columnas = ['codigo',
 'region',
 'municipioEscolar',
 'nombreEscuela',
 'nivel',
 'matricula',
 'ausentismo_cronico',
 'ciencias_meta',
 'espanol_meta',
 'ingles_meta',
 'mate_meta']
primarias = primarias[columnas]


escuelas_2019 = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/Escuelas_PR/main/escuelas_pr_capstone.csv')
list(escuelas_2019.columns)

columns = ['CODIGO_ESCUELA','escuela_receptora','espanol_1819','matematica_1819',
           'ingles_1819','ciencias_1819']

escuelas_2019 = escuelas_2019[columns]
escuelas_2019 = escuelas_2019.rename(columns = {'CODIGO_ESCUELA':'codigo',
                                'espanol_1819':'espanol_meta_19',
                                'matematica_1819':'mate_meta_19',
                                'ingles_1819':'ingles_meta_19',
                                'ciencias_1819':'ciencias_meta_19'})

primarias_merged = primarias.merge(escuelas_2019, on = 'codigo', how='left')

primarias_merged = primarias_merged.dropna(axis = 0, subset = ['escuela_receptora'])

list(primarias_merged.columns)
primarias_merged = primarias_merged.rename(columns = {'matricula':'matricula_21',
                                   'ciencias_meta':'ciencias_meta_21',
                                   'ausentismo_cronico':'ausentismo_cronico_21',
                                   'espanol_meta':'espanol_meta_21',
                                   'ingles_meta':'ingles_meta_21',
                                   'mate_meta':'mate_meta_21'})

enrollment_aY = pd.read_csv('https://raw.githubusercontent.com/rivera-squared/educacion_db/main/enrollment_by_acYear.csv')

enrollment_aY = enrollment_aY.rename(columns = {'PartitionKey':'codigo'})
enrollment_aY_2019 = enrollment_aY[enrollment_aY['AcademicYear'] == 2019]

columnas = ['codigo','All']
enrollment_aY_2019 = enrollment_aY_2019[columnas]
enrollment_aY_2019 = enrollment_aY_2019.rename(columns = {'All':'matricula_2019'})

primarias_merged = primarias_merged.merge(enrollment_aY_2019, on = 'codigo', how = 'left')

primarias_merged.to_csv('primarias_19_21.csv', index = False)

receptoras = primarias_merged[primarias_merged['escuela_receptora'] == 1]
no_receptoras =primarias_merged[primarias_merged['escuela_receptora'] == 0]

scipy.stats.ttest_rel(receptoras['espanol_meta_19'], receptoras['espanol_meta_21'])
scipy.stats.ttest_rel(receptoras['espanol_meta_19'], receptoras['espanol_meta_21'])




