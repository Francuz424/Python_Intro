# Raport – Analiza MCDM z użyciem biblioteki pymcdm

## 1. Wprowadzenie
Celem analizy było zapoznanie się z funkcjonalnością biblioteki `pymcdm` oraz porównanie dwóch metod wielokryterialnego podejmowania decyzji: TOPSIS i SPOTIS.

## 2. Dane wejściowe
Macierz decyzyjna zawierała dane dla 4 alternatyw (A1–A4) oraz 3 kryteriów:
- Koszt (minimalizowany),
- Zysk (maksymalizowany),
- Ryzyko (minimalizowane).

Wagi: [0.4, 0.4, 0.2]
Typy: [0, 1, 0]

## 3. Zastosowane metody
Zastosowano metody: TOPSIS (po normalizacji MinMax) oraz SPOTIS (bez normalizacji).

## 4. Wyniki
Wyniki znajdują się w pliku `wyniki_mcdm.csv` po uruchomieniu skryptu.

## 5. Wnioski
- Różnice w rankingach wynikają z różnych podejść obliczeniowych.
- Alternatywy mogą mieć różne pozycje w zależności od metody.

## 6. Repozytorium
Pliki:
- `pymcdm_analysis.py`
- `wyniki_mcdm.csv`
- `raport.md`
- `README.md`
- `requirements.txt`
