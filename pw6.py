import pandas as po
import numpy as np

df = po.read_csv('D:/.vscode/Python-2026-L1/commaseperatedvalues/students.csv')
df2 = po.read_csv('D:/.vscode/Python-2026-L1/commaseperatedvalues/marks.csv')
df3 = po.read_csv('D:/.vscode/Python-2026-L1/commaseperatedvalues/courses.csv')

df.query('Name == "Vladimir Putin"')
df2.query('French Language >= 14')
df3.query('Name == "Xi Jinping" & Operating Systems >= 16')

