# IDS-ML

![Project Banner](./assets/banner.png)

We are a group of three French engineering students at [ESILV](https://www.esilv.fr/), majoring in IoT and Cybersecurity. This repository contains our Machine Learning course project focused on real-time intrusion detection for IoT infrastructures.

## Dataset

We currently use the RT-IoT2022 dataset available here:  
https://archive.ics.uci.edu/dataset/942/rt-iot2022

RT-IoT2022 is a dataset collected from a real-time IoT infrastructure that integrates a variety of IoT devices (e.g., ThingSpeak-LED, Wipro-Bulb, MQTT-Temp) and simulated attack scenarios (Brute-Force SSH, DDoS with Hping and Slowloris, Nmap patterns). Bidirectional network traffic features were captured using the Zeek network monitoring tool with the Flowmeter plugin. The dataset includes both normal and adversarial behaviors representative of real-world conditions, and is intended to support the development and evaluation of Intrusion Detection Systems (IDS) for IoT networks.

The way the dataset was generated are detailed in the following paper:
- [Quantized autoencoder (QAE) intrusion detection system for anomaly detection in resource-constrained IoT devices using RT-IoT2022 dataset, Sharmila, 2022](https://cybersecurity.springeropen.com/counter/pdf/10.1186/s42400-023-00178-5.pdf)

## Project goal

The goal of this project is to develop a high-performance model capable of identifying malicious network flows in real time. The system will serve as a core detection component upon which other security tools can build. Emphasis will be placed on:
- robust and reliable accuracy,
- stable calibration for production use,
- low latency and a low false-alarm rate.

## Repository structure

```
IDS-ML/
├── assets/                 # Images and logos used in the project
├── data/                   # Dataset directory
│   └── rt_iot2022.csv      # The RT-IoT2022 dataset
├── jobs/                   # Saved models and preprocessing pipelines
│   ├── wdro_models/        # Wasserstein Distributionally Robust Optimization models
│   ├── logistic_regression_PCA_model.joblib
│   └── preprocessing.joblib
├── notebooks/              # Jupyter notebooks for analysis and modeling
│   ├── Cross_Validation.ipynb
│   ├── grid_search.ipynb
│   ├── LogisticRegression_with_PCA.ipynb
│   └── WDRO.ipynb
├── report/                 # LaTeX source for the project report
│   ├── images/
│   ├── main.tex
│   └── references.bib
├── import_data.py          # Script to download the dataset
└── requirements.txt        # Python dependencies
```

## Quick start

1. Clone the repository:
   ```bash
    git clone https://github.com/TheHardy04/IDS-ML
    cd IDS-ML
    ```
2. Install dependencies: 
    ```bash
    pip install -r requirements.txt
    ```
3. Download the RT-IoT2022 with the `import_data.py` script:
    ```bash
    python import_data.py 
    ```
4. You can put the following code in your notebook or python script to load the data:
    ```python
    import pandas as pd
    
    # load dataset
    data = pd.read_csv('../data/rt_iot2022.csv')
    ```

## Team members

- [Théo HARDY](https://github.com/TheHardy04)
- Gaël LE MOUEL
- Adam FERRE

## Acknowledgements

<a href="https://www.esilv.fr/" target="_blank" rel="noopener noreferrer">
  <img src="./assets/esilv_logo.png" alt="ESILV Logo" width="100" />
</a>

