import streamlit as st

def health_and_fitness_advice(age, gender, activity_level):
    # แนะนำปริมาณการออกกำลังกายตามกลุ่มอายุและเพศ
    if age < 18:
        advice = "เด็กและวัยรุ่นควรออกกำลังกายอย่างสม่ำเสมออย่างน้อย 60 นาทีต่อวัน"
    elif age >= 18 and age <= 64:
        if gender == "ชาย":
            advice = "ชายที่มีอายุระหว่าง 18-64 ปีควรออกกำลังกายอย่างสม่ำเสมออย่างน้อย 150 นาทีต่อสัปดาห์"
        else:
            advice = "หญิงที่มีอายุระหว่าง 18-64 ปีควรออกกำลังกายอย่างสม่ำเสมออย่างน้อย 150 นาทีต่อสัปดาห์"
    else:
        advice = "ผู้สูงอายุควรออกกำลังกายอย่างสม่ำเสมออย่างน้อย 150 นาทีต่อสัปดาห์"

    # แนะนำระดับกิจกรรมทางกาย
    if activity_level == "น้อย":
        advice += "\nควรเพิ่มการออกกำลังกายอย่างน้อย 30 นาทีต่อวัน"
    elif activity_level == "ปานกลาง":
        advice += "\nควรเพิ่มการออกกำลังกายอย่างน้อย 60 นาทีต่อวัน"
    else:
        advice += "\nการออกกำลังกายอย่างสม่ำเสมอ เช่น วิ่ง, ว่ายน้ำ เป็นต้น"

    return advice

menu_option = st.sidebar.radio("เมนู", ["Health and exercise advice"])

if menu_option == 'Health and exercise advice':
    age = st.number_input('ระบุอายุของคุณ')
    gender = st.selectbox(
        'ระบุเพศของคุณ',
        ('ชาย', 'หญิง'), index=None, key='gender_select')
    activity_level = st.selectbox(
        'ระบุระดับกิจกรรมของคุณ',
        ('น้อย', 'ปานกลาง', 'มาก'), index=None, key='activity_select')

    if st.button('คำนวณ'):
        advice = health_and_fitness_advice(age, gender, activity_level)

        st.write(":red[คำแนะนำเกี่ยวกับสุขภาพและการออกกำลังกาย :]")
        st.write(advice)

