# pymcdm_analysis.py
import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import MinMax

# --- Dane decyzyjne ---
matrix = np.array([
    [250000, 30000, 0.3],
    [200000, 25000, 0.4],
    [300000, 40000, 0.5],
    [275000, 35000, 0.2]
])

weights = [0.4, 0.4, 0.2]
types = [0, 1, 0]

normalizer = MinMax()
norm_matrix = normalizer.normalize(matrix, types)

topsis = TOPSIS()
topsis_scores = topsis(matrix=norm_matrix, weights=weights, types=types)

spotis = SPOTIS()
spotis_scores = spotis(matrix=matrix, weights=weights, types=types)

df = pd.DataFrame({
    'Alternatywa': ['A1', 'A2', 'A3', 'A4'],
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores
})

df['TOPSIS_ranking'] = df['TOPSIS'].rank(ascending=False)
df['SPOTIS_ranking'] = df['SPOTIS'].rank()

print(df)

df.to_csv("wyniki_mcdm.csv", index=False)
