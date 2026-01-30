import streamlit as st

def calculate_commission(price, category):
    if category in ['Жіночий', 'Чоловічий', 'Дитячий', 'Аксесуари', 'КрасаТаЗдоров', 'ДляДому']:
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

st.title("Калькулятор комісії Shafa.ua")

category = st.selectbox("Оберіть категорію:", ['Жіночий', 'Чоловічий', 'Дитячий', 'Аксесуари', 'КрасаТаЗдоров', 'ДляДому', 'Інше'])

price = st.number_input("Ціна товара (грн):", min_value=0.0, step=0.01)

actual_price = st.number_input("Фактична ціна продажу (грн):", min_value=0.0, step=0.01)

if st.button("Розрахувати"):
    if price > 0 and actual_price > 0:
        percent_price, comm_price = calculate_commission(price, category)
        percent_actual, comm_actual = calculate_commission(actual_price, category)
        
        difference = comm_price - comm_actual
        
        st.write(f"**Для ціни товара ({price} грн):**")
        st.write(f"Відсоток: {percent_price}%")
        st.write(f"Сума списання: {comm_price:.2f} грн")
        
        st.write(f"**Для фактичної ціни ({actual_price} грн):**")
        st.write(f"Відсоток: {percent_actual}%")
        st.write(f"Сума списання: {comm_actual:.2f} грн")
        
        st.write(f"**Різниця для повернення: {difference:.2f} грн**")
    else:
        st.error("Введіть позитивні значення для цін")