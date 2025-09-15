# EduScoreAI - AI-powered student grade prediction

## Project Goal
EduScoreAI is designed to predict student performance by analyzing exam scores and demographic details. It provides a predicted grade, helping teachers and institutions identify performance patterns and assist students who may be at risk.

---

## Overview
This project uses **Logistic Regression** to classify student grades based on input features such as gender, race/ethnicity, parental education, lunch type, test preparation, and exam scores.  
The model was trained on a student performance dataset, evaluated using standard metrics, and deployed as a **Streamlit web app** for interactive use.

---

## Project Workflow

### 1. Data Preprocessing
- Removed null values and standardized the dataset.
- Encoded categorical features:
  - Gender  
  - Race/Ethnicity  
  - Parental Level of Education  
  - Lunch  
  - Test Preparation Course  
- Added engineered features such as:
  - **Pass/Fail per subject (Math, Reading, Writing)**  
  - **Total Score**  
  - **Percentage**  
  - **Overall Pass/Fail status**  
- Scaled features using **StandardScaler**.

### 2. Model Building
- Chose **Logistic Regression** due to its simplicity and interpretability.  
- Trained the model on the processed dataset.  
- Achieved strong generalization without overfitting.  
- Saved the trained model (`model.pkl`) and scaler (`scaler.pkl`) for deployment.



## Features
- Predicts student grades (O, A, B, C, D, E).
- Uses demographic, parental, and exam score data.
- Pass/Fail detection for each subject.
- Calculates total score, percentage, and overall status.
- Interactive Streamlit UI for predictions.

## Future Enhancements
- Deploy on cloud (Streamlit Cloud, Render, or Heroku).
- Add support for multiple models (Random Forest, Gradient Boosting).
- Expand dataset for broader applicability.
- Integrate performance insights dashboards.
- Enable CSV bulk upload for multiple student predictions.

---

## 📌 How to Run Locally  

```
git clone https://github.com/AradhyaRay05/CarValuatorAI.git
cd CarValuatorAI
pip install -r requirements.txt
streamlit run app.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀
