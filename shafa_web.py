import streamlit as st

def minimum_commission(price):
    # Мінімальна комісія залежно від суми замовлення
    if price <= 50:
        return 10
    elif price <= 100:
        return 20
    else:
        return 30

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
    actual_comm = price * percent / 100
    min_comm = minimum_commission(price)
    commission = max(min_comm, min(500, actual_comm))
    return percent, commission, actual_comm, min_comm

st.markdown('<div style="font-size: 2em; font-weight: bold; user-select: none;">Калькулятор комісії SHF</div>', unsafe_allow_html=True)

category = st.radio("Категорія:", ['Жіночий', 'Чоловічий', 'Дитячий', 'Аксесуари', 'Краса Та Здоров', 'Для Дому', 'Інше'])

price_input = st.text_input("Ціна продажу:", value="")

actual_price_input = st.text_input("Ціна зі знижкою:", value="")

if st.button("Розрахувати"):
    try:
        price = float(price_input) if price_input.strip() else 0
        actual_price = float(actual_price_input) if actual_price_input.strip() else 0
        if price <= 0:
            st.error("Необхідна ціна продажу")
        else:
            output = ""
            percent_price, comm_price, actual_comm_price, min_comm_price = calculate_commission(price, category)
            highlight_price = actual_comm_price < min_comm_price or actual_comm_price > 500
            comm_str_price = f"{comm_price:.2f} грн"
            if highlight_price:
                comm_str_price += f" | <span style='color: yellow; font-size: 14px;'>фактична {actual_comm_price:.2f} грн</span>"
            output += f"**Для ціни продажу ({price} грн):**\n- Відсоток: {percent_price}%\n- Сума списання: {comm_str_price}\n\n"
            if actual_price > 0:
                percent_actual, comm_actual, actual_comm_actual, min_comm_actual = calculate_commission(actual_price, category)
                highlight_actual = actual_comm_actual < min_comm_actual or actual_comm_actual > 500
                comm_str_actual = f"{comm_actual:.2f} грн"
                if highlight_actual:
                    comm_str_actual += f" | <span style='color: yellow; font-size: 14px;'>фактична {actual_comm_actual:.2f} грн</span>"
                output += f"**Для ціни зі знижкою ({actual_price} грн):**\n- Відсоток: {percent_actual}%\n- Сума списання: {comm_str_actual}\n\n"
                difference = comm_price - comm_actual
                if difference == 0:
                    diff_str = f"<span style='color: yellow;'>**Різниця для повернення: {difference:.2f} грн**</span>"
                else:
                    diff_str = f"**Різниця для повернення: {difference:.2f} грн**"
                output += diff_str
            st.markdown(output, unsafe_allow_html=True)
    except ValueError:
        st.error("Помилка - некоректна ціна")