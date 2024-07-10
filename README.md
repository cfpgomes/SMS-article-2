# SMS-article-2

This repository contains the code and data files for the article "A Systematic Mapping Study on Quantum and Quantum-inspired Algorithms in Operations Research" by Claudio Gomes, João Paulo Fernandes, Gabriel Falcao, Soummya Kar, and Sridhar Tayur. The article is under review for publication in the journal "ACM Computing Surveys".
 
## Main Code File and Running Instructions

- **`analysis.py`**: The main Jupyter Notebook for data analysis. The notebook has titles for each step of the analysis, including data loading, validation, quality assessment, and exploratory analysis.

To run the code, you need to have Python installed on your machine. You can run the code in a Jupyter Notebook environment or any other Python IDE. Make sure to have the required libraries installed before running the code, which are mentioned at the beginning of the notebook.

## Data Files

- **`allarticles.csv`**: Contains data extracted from all the articles considered in the study.
- **`QualityChecklists.csv`**: Contains manually filled-in quality checklists used in the quality assessment process.
- **`CORE 2013.csv` to `CORE 2021.csv`**: Contain data from CORE conferences for different years, used for analysis and quality assessment.
- **`scimagojr 2011.csv` to `scimagojr 2021.csv`.**: Provide Scimago Journal & Country Rank data, crucial for evaluating the impact and quality of journals where the articles are published.
- **`ISIC_Rev_4_english_structure.csv`**: Contains English data from the International Standard Industrial Classification (ISIC) system, used for analysis.

## Output Folders

- `qualityassessment/`: Contains PDF files with quality assessment results considering the selected articles.
- `analysis/`: Contains PDF files with the results from individual feature analysis, analysis of pairs, and exploratory analysis.
- `searchandstudyselectionvalidation/`: Contains PDF files with the results from the search and study selection validation process.
- `website/`: Contains HTML files for data visualization in (https://cfpgomes.github.io/sms)[https://cfpgomes.github.io/sms].