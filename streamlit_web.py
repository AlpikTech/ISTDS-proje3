import streamlit as st


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

st.markdown("---")
st.markdown("#### **Yaş**")
st.slider("Yaşınızı Seçiniz:", min_value=10, max_value=110, value=30)

st.markdown("---")
st.markdown("#### **Boy**")
st.slider("Boyunuzu Seçiniz:", min_value=120, max_value=200, value=165)

st.markdown("---")
st.markdown("#### **Kilo**")
st.slider("Kilonuzu Seçiniz:", min_value=30, max_value=150, value=70)




st.markdown("---")

family_history = st.radio(
    "## **Aile Geçmişinde Obez Biri Var Mı?**",
    ["Evet", "Hayır"]
)
st.markdown("---")
high_calorie_food = st.radio(
    "## **Yüksek Kalorili Yemekleri Yer Misin?**",
    ["Evet", "Hayır"])

st.markdown("---")

vegatable_food = st.radio(
    "## **Meyve Sebze Yeme Seviyen?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
st.markdown("---")
st.markdown("**Günde Kaç Öğün Yemek Yersin**")
st.number_input("", min_value=1, max_value=5, value=3, step=1)
st.markdown("---")

food_between_meals = st.selectbox(
    "## **Hangi Sıklıkla Öğün Arası Atıştırırsın?**",
    ["Hiçbir zaman", "Bazen", "Sık sık", "Her zaman"])
st.markdown("---")

smoking = st.radio(
    "## **Sigara İçer Misin?**",
    ["Evet", "Hayır"])
st.markdown("---")
water = st.radio(
    "## **Ne Kadar Su İçersin?**",
    ["Seviye 1", "Seviye 2", "Seviye 3"])
st.markdown("---")
calorie_tracking = st.radio(
    "## **Kalori Alımını Takip Eder Misin?**",
    ["Evet", "Hayır"])


st.markdown("---")
physical_activity = st.radio(
    "## **Hangi Sıklıkla Fiziksel Aktevite Yaparsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
st.markdown("---")
time_spent_on_tech = st.radio(
    "## **Zamanın Ne Kadarını Teknolojiye Ayırsın?**",
    ["Seviye 0", "Seviye 1", "Seviye 2", "Seviye 3"])
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