import streamlit as st


st.set_page_config(
    page_title="Obezite Tahmini",
    initial_sidebar_state="collapsed",  # Sidebar varsayılan olarak kapalı)
)


# st.markdown("## **Obezite Tahmin Modeli**")
# st.markdown("Bu site Obezite ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız")

st.markdown("""# **Obezite Tahmin Modeli**

Bu site Obezite ile alakalı tahmin yapmak için tasarlanmıştır. Bunu yapmak için sınıflandırma modeli kullanacağız.

### **Ne kullanabiliriz:**
- Veri Tabanı: `postgresql`
- Web: `flask` & `streamlit`
- Veri Bilimi: `numpy`, `pandas`, `matplotlib` , `seaborn`
- Model Kütüphaneleri:  `statsmodels`, `scikit-learn` , `mlxtend`, `XGBosst`
- Görselleştirme: `qlik` & `tableau` (Opsiyonel)
""")

st.markdown("---")
st.markdown("#### **Kilo**")
st.slider("Kilonuzu Seçiniz:", min_value=30, max_value=150, value=70)

st.markdown("---")
st.markdown("#### **Boy**")
st.slider("Boyunuzu Seçiniz:", min_value=120, max_value=200, value=165)

st.markdown("---")
st.markdown("#### **Yaş**")
st.slider("Yaşınızı Seçiniz:", min_value=10, max_value=110, value=30)

st.button("# **Tahmin Yap**")

with st.sidebar:
    st.markdown("## **Repository'miz**:")
    st.markdown("Kaynak kodu ve daha fazla bilgi için Repositroy'mize bakabilirsiniz")
    st.link_button("GitHub", "https://github.com/AlpikTech/ISTDS-proje3")
    st.markdown("## **Biz Kimiz**")
    st.markdown("Ben Alpik Tech. Bu projeyi yaptım çünkü ISTDS'nin 3. projesiydi.")