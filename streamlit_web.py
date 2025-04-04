import streamlit as st
import numpy as np
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import xgboost as xgb
from xgboost import XGBClassifier


st.set_page_config(
    page_title="Obezite Tahmini",
    initial_sidebar_state="collapsed",  # Sidebar varsayılan olarak kapalı)
)


# st.markdown("## **Obezite Tahmin Modeli**")
# st.markdown("Bu site Obezite ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız")

st.markdown("""# **Obezite Tahmin Modeli**

Bu site Obezite ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız.

### **Ne kullanabilirdik:**
- Veri Tabanı: `postgresql`
- Web: `flask` & `streamlit`
- Veri Bilimi: `numpy`, `pandas`, `matplotlib` , `seaborn`
- Model Kütüphaneleri:  `statsmodels`, `scikit-learn` , `mlxtend`, `XGBosst`
- Görselleştirme: `qlik` & `tableau` (Opsiyonel)
""")
st.markdown("---")
gender = st.radio(
    "## **Cinsiyetin Ne?**",
    ["Kız", "Erkek"])
if gender == "Kız":
    gender_numeric = 0
elif gender == "Erkek":
    gender_numeric = 1

st.markdown("---")
st.markdown("#### **Yaş**")
age = st.slider("Yaşınızı Seçiniz:", min_value=10, max_value=110, value=30)

st.markdown("---")
st.markdown("#### **Boy**")
heigh = st.slider("Boyunuzu Seçiniz:", min_value=120, max_value=200, value=165)

st.markdown("---")
st.markdown("#### **Kilo**")
weigh = st.slider("Kilonuzu Seçiniz:", min_value=30, max_value=150, value=70)




st.markdown("---")

family_history = st.radio(
    "## **Aile Geçmişinde Obez Biri Var Mı?**",
    ["Evet", "Hayır"]
)

if family_history == "Evet":
    family_history_numeric = 1
elif family_history == "Hayır":
    family_history_numeric = 0

st.markdown("---")
high_calorie_food = st.radio(
    "## **Yüksek Kalorili Yemekleri Yer Misin?**",
    ["Evet", "Hayır"])
if high_calorie_food == "Evet":
    high_calorie_food_numeric = 1
elif high_calorie_food == "Hayır":
    high_calorie_food_numeric = 0

st.markdown("---")

vegatable_food = st.radio(
    "## **Meyve Sebze Yeme Seviyen?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
if vegatable_food == "Seviye 1":
    vegatable_food_numeric = 1.0
elif vegatable_food == "Seviye 2":
    vegatable_food_numeric = 2.0
elif vegatable_food == "Seviye 3":
    vegatable_food_numeric = 3.0

st.markdown("---")
st.markdown("**Günde Kaç Öğün Yemek Yersin**")
st.number_input("", min_value=1, max_value=5, value=3, step=1)
st.markdown("---")

food_between_meals = st.selectbox(
    "## **Hangi Sıklıkla Öğün Arası Atıştırırsın?**",
    ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])
if food_between_meals == "Hiçbir zaman":
    food_between_meals_numeric = 3
elif food_between_meals == "Bazen":
    food_between_meals_numeric = 2
elif food_between_meals == "Sık sık":
    
st.markdown("---")

smoking = st.radio(
    "## **Sigara İçer Misin?**",
    ["Evet", "Hayır"])
if smoking == "Evet":
    smoking_numeric = 1
elif smoking == "Hayır":
    smoking_numeric = 0
st.markdown("---")
water = st.radio(
    "## **Ne Kadar Su İçersin?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
if water == "Seviye 1":
    water_numeric = 1.0
elif water == "Seviye 2":
    water_numeric = 2.0
elif water == "Seviye 3":
    water_numeric = 3.0
st.markdown("---")
calorie_tracking = st.radio(
    "## **Kalori Alımını Takip Eder Misin?**",
    ["Evet", "Hayır"])
if calorie_tracking == "Evet":
    calorie_tracking_numeric = 1
elif calorie_tracking == "Hayır":
    calorie_tracking_numeric = 0


st.markdown("---")
physical_activity = st.radio(
    "## **Hangi Sıklıkla Fiziksel Aktevite Yaparsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
if physical_activity == "Seviye 0":
    physical_activity_numeric = 0.0
elif physical_activity == "Seviye 1":
    physical_activity_numeric = 1.0
elif physical_activity == "Seviye 2":
    physical_activity_numeric = 2.0
elif physical_activity == "Seviye 3":
    physical_activity_numeric = 3.0
st.markdown("---")
time_spent_on_tech = st.radio(
    "## **Zamanın Ne Kadarını Teknolojiye Ayırsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
if time_spent_on_tech == "Seviye 0":
    time_spent_on_tech_numeric = 0.0
elif time_spent_on_tech == "Seviye 1":
    time_spent_on_tech_numeric = 1.0
elif time_spent_on_tech == "Seviye 2":
    time_spent_on_tech_numeric = 2.0
elif time_spent_on_tech == "Seviye 3":
    time_spent_on_tech_numeric = 3.0
st.markdown("---")
alcohol = st.selectbox(
    "## **Hangi Sıklıkla Alkol Tüketirsin?**",
    ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])
st.markdown("---")
transportation = st.selectbox(
    "## **Genellikle Ulaşımını Ne ile Yaparsın?**",
    ["Otomobil", "Bisiklet", "Motobisiklet", "Toplu Taşıma", "Yürüme"])

st.button("# **Tahmin Yap**")





with st.sidebar:
    st.markdown("## **Repository'miz**:")
    st.markdown("Kaynak kodu ve daha fazla bilgi için Repositroy'mize bakabilirsiniz")
    st.link_button("GitHub", "https://github.com/AlpikTech/ISTDS-proje3")
    st.markdown("## **Biz Kimiz**")
    st.markdown("Ben Alpik Tech. Bu projeyi yaptım çünkü ISTDS'nin 3. projesiydi.")