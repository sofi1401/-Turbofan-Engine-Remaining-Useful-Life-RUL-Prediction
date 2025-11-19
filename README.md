# -Turbofan-Engine-Remaining-Useful-Life-RUL-Prediction
This repository presents a complete end-to-end pipeline for **Predictive Maintenance** using NASA's CMAPSS Turbofan Engine dataset. The goal is to estimate the **Remaining Useful Life (RUL)** of engines before failure, using progressively advanced techniques—from baseline machine learning to multimodal deep learning.

---

## 📌 Project Workflow

|          Stage           |                                        Technique                                    |
|--------------------------|-------------------------------------------------------------------------------------|
| Baseline Models          | Linear Regression, Random Forest, XGBoost, SVR                                      |
| Hybrid Ensemble          | RF + XGBoost + LSTM                                                                 |
| Multimodal Deep Learning | LSTM for sensor data + DNN for statistical features + Embedding for engine settings |
| Final Pipeline           | Complete comparison, feature engineering, results evaluation                        |

---

## 🚀 Notebooks in This Repository

|          Notebook        |                                      Description                                         |
|--------------------------|------------------------------------------------------------------------------------------|
| `baseline.ipynb`         | Implements basic ML models for RUL prediction (LR, RF, XGB, SVR).                        |
| `rf_xgb_lstm_pred.ipynb` | Hybrid ensemble model combining RF, XGB, and LSTM for more accurate predictions.         |
| `multimodal_pred.ipynb`  | Multimodal deep learning using sensor sequence data, statistical features, and metadata. |
| `RUL_pred.ipynb`         | Complete workflow with model comparison, evaluation metrics, final conclusions.          |

---

## 🧠 Key Features

✔ Feature engineering: cycles, degradation trend, rolling window stats  
✔ Time-series modeling using sliding window sequences  
✔ Hybrid ensemble learning (RF + XGB + LSTM)  
✔ Multimodal fusion (sensor → LSTM, metadata → DNN)  
✔ Comparative performance analysis (RMSE, MAE, R²)  
✔ Suitable for **Predictive Maintenance / Aerospace / IoT Analytics**

---

## 📊 Model Performance 

|           Model          | RMSE ↓ | 
|--------------------------|--------|
| Random Forest            | 26.144 | 
| XGBoost                  | 25.669 |
| LSTM                     | 28.543 | 
| Multimodal Deep Learning | 30.68  |

---

## 🛠 Tech Stack
- Python, NumPy, Pandas, Matplotlib, Seaborn  
- Scikit-Learn, XGBoost  
- TensorFlow / Keras (LSTM, DNN)  
- NASA CMAPSS Turbofan RUL Dataset

---

## 🔮 Applications
🔹 Aircraft engine health monitoring  
🔹 Industrial equipment failure prediction  
🔹 IoT-based predictive maintenance  
🔹 Smart manufacturing and prognosis systems  

---

## 📈 Repository Structure
├── baseline.ipynb
├── rf_xgb_lstm_pred.ipynb
├── multimodal_pred.ipynb
├── RUL_pred.ipynb
├── data/ (Not included due to size)
└── README.md

---

## 🧑‍💻 Author
**Sofika M**  
AI | Deep Learning | Predictive Analytics  

---

### ⭐ If you like this work, consider giving a ⭐ to the repository!
