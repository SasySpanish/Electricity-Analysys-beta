# Energy Production and Coverage Datasets (2005-2023)
## Overview
This repository contains datasets related to the production and coverage of electricity demand in Italy from 2005 to 2023. The data is derived from official sources and has been cleaned and merged to provide insights into energy trends across various regions and sources.
## Datasets
### 1. Production Data (2005-2023_prod.csv)

- Description: Contains detailed records of electricity production across Italian regions, provinces, and energy sources.
- Columns:
-- Anno: Year of production (e.g., 2005.0, 2023.0).
-- Tipo produzione: Type of production (e.g., Lorda, Netta).
-- Regione: Region in Italy (e.g., Veneto, Toscana).
-- Provincia: Province within the region (e.g., Verona, Siena).
-- Fonte: Energy source (e.g., Geotermoelettrico, Idrico, Fotovoltaico, Eolico).
-- Produzione(GWh): Electricity production in gigawatt-hours (GWh).


- Notes: Data includes both gross (Lorda) and net (Netta) production values. Some entries may contain minimal production (e.g., 0.000233 GWh) for certain sources like Eolico.

### 2. Coverage Data (2005-2023_cover.csv)

- Description: Provides data on the coverage of electricity demand by energy source and region.
- Columns:
-- Anno: Year of coverage (e.g., 2006, 2023).
-- Regione: Region in Italy (e.g., Liguria, Lombardia).
-- Fonte: Energy source (e.g., Fotovoltaico, Eolico, Termoelettrico tradizionale).
-- Copertura(GWh): Coverage of demand in gigawatt-hours (GWh).


- Notes: Includes aggregated values and excludes certain categories like "Saldo import/export" and "Bioenergie" for focused analysis. Some regions show negative values (e.g., -4245.3 GWh) indicating net import scenarios.

