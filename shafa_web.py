import streamlit as st

def calculate_commission(price, category):
    if category in ['Жіночий', 'Чоловічий', 'Дитячий', 'Аксесуари', 'Краса Та Здоров', 'Для Дому']:
        if price <= 500:
            percent = 20
        elif price <= 1000:
            percent = 17
        else:
            percent = 13
    else:
        if price <= 500:
            percent = 15
        elif price <= 1000:
            percent = 12
        else:
            percent = 9
    commission = price * percent / 100
    commission = max(30, min(400, commission))
    return percent, commission

st.markdown('<div style="font-size: 2em; font-weight: bold; user-select: none;">Калькулятор комісії SHF</div>', unsafe_allow_html=True)

category = st.radio("Категорія:", ['Жіночий', 'Чоловічий', 'Дитячий', 'Аксесуари', 'Краса Та Здоров', 'Для Дому', 'Інше'])

price_input = st.text_input("Ціна продажу:", value="")

actual_price_input = st.text_input("Ціна зі знижкою:", value="")

if st.button("Розрахувати"):
    try:
        price = float(price_input)
        actual_price = float(actual_price_input)
        if price > 0 and actual_price > 0:
            percent_price, comm_price = calculate_commission(price, category)
            percent_actual, comm_actual = calculate_commission(actual_price, category)
            
            difference = comm_price - comm_actual
            
            st.markdown(f"""
**Для ціни продажу ({price} грн):**
- Відсоток: {percent_price}%
- Сума списання: {comm_price:.2f} грн

**Для ціни зі знижкою ({actual_price} грн):**
- Відсоток: {percent_actual}%
- Сума списання: {comm_actual:.2f} грн

**Різниця для повернення: {difference:.2f} грн**
""")
        else:
            st.error("Введіть позитивні значення для цін")
    except ValueError:
        st.error("Введіть коректні цифри для цін")