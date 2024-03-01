import streamlit as st
from PIL import Image
# Function to set background image
def set_background(image_url):
    image_url_str = f'url("{image_url}")'
    css = f"""
    <style>
    .stApp {{
        background-image: {image_url_str};
        background-size: 100% 1000px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# เรียกใช้ฟังก์ชัน set_background() เพื่อกำหนดพื้นหลัง
set_background("https://png.pngtree.com/background/20210715/original/pngtree-white-simple-texture-background-picture-image_1323742.jpg")



#Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height/100)**2
    return bmi

#Health and exercise advice
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
        advice += "\nควรออกกำลังกายอย่างสม่ำเสมอ เช่น วิ่ง กระโดดเชือก หรือเดิน เป็นต้น"

    return advice

# Main
def main():
    st.header('Body mask index(BMI)', divider='red')
    st.sidebar.subheader(":red[Menu]")
    menu_option = st.sidebar.radio("Select Option :mag:", ["Home page", "Calculator","Health and exercise advice"])

    if menu_option == 'Calculator':
        image = Image.open('streamlit/BOdy mask index.jpg')
        st.image(image)
        st.markdown('''
            :black[การหาค่าดัชนีมวลกาย (Body Mass Index : BMI) คือเป็นมาตรการที่ใช้ประเมินภาวะอ้วนและผอม
            สามารถทำได้โดยการชั่งน้ำหนักตัวเป็นกิโลกรัมและวัดส่วนสูงเป็นเซนติเมตร 
            แล้วนำมาหาดัชมีมวลกาย โดยใช้โปรแกรมวัดค่าความอ้วน]
            ''')
        st.header("BMI Calculator",divider='red')
        
        # Select gender
        choice = st.selectbox('Select gender', ('Male', 'Female'))
        
        # Slider for age
        age = st.slider('Enter your age', 10, 100, 18)
        st.write('I am', age ,'years old')

        # Input weight in kg
        weight = st.number_input("Enter your weight (kg)")

        # Input height in cm
        height = st.number_input("Enter your height (cm)")

        # Button to calculate BMI
        if st.button("Calculate :red[->>]"):
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is :red[{bmi:.2f}]")

            # Interpretation of BMI
            if bmi < 18.5:
                image = Image.open('streamlit/Underweight.jpg')
                st.image(image)
                st.header('ข้อเเนะนำ',divider='red')
                st.write(''':red[การดูแลเรื่องอาหาร:] ควรระวังปริมาณและคุณภาพของอาหารที่บริโภค โดยเลือกอาหารที่มีประโยชน์และลดการบริโภคอาหารที่มีไขมันสูง น้ำตาล หรือเกลือ เพื่อลดความเสี่ยงต่อการเป็นโรคเบาหวาน ความดันเลือดสูง และไขมันในเลือดสูง อันเป็นผลเสียจากการผอมลงพุง\n
:red[การบริโภคอาหารที่หลากหลาย:] ควรรับประทานอาหารที่มีโปรตีนให้เพียงพอเพื่อส่งเสริมการสร้างกล้ามเนื้อ หากต้องการเพิ่มน้ำหนัก ควรเพิ่มปริมาณการบริโภคอาหารโดยการเลือกทานอาหารที่มีประโยชน์ เช่น คาร์โบไฮเดรตเชิงซ้อน และไขมันดี\n
:red[การออกกำลังกาย:] ควรเคลื่อนไหวและออกกำลังกายอย่างสม่ำเสมอ ในระดับความหนักปานกลาง โดยเลือกกิจกรรมที่สนุกสนานและเพลิดเพลิน เช่น เต้น เดิน วิ่ง ว่ายน้ำ หรือกิจกรรมที่ใช้พลังงานมาก เช่น การทำงานบ้าน หรือการทำสวน แนะนำให้ออกกำลังกายอย่างน้อย 30 นาทีต่อวัน หรือไม่น้อยกว่า 150 นาทีต่อสัปดาห์\n
                         ''')
                st.header('อาหารเพิ่มน้ำหนัก',divider='red')
                #header underweight
                tab1, tab2, tab3, tab4, tab5 = st.tabs(["นม","ไข่","ข้าวกล้อง","น้ำผลไม้","โยเกิร์ต"])
                
                with tab1:             
                    st.header(": นม")
                    st.image("https://s.isanook.com/he/0/ud/4/23301/milk.jpg", width=500)
                    st.write('นมเป็นอาหารที่มีคุณค่าทางโภชนาการสูง และเป็นที่รู้จักกันดีว่าเป็นตัวช่วยในการเพิ่มน้ำหนักได้ดี เนื่องจากมีโปรตีนที่มีคุณภาพสูง และมีไขมันและคาร์โบไฮเดรตเพียงพอ เป็นแหล่งพลังงานที่ดีต่อการเพิ่มน้ำหนักด้วยความสมดุล')

                with tab2:
                    st.header(": ไข่")
                    st.image("https://images.aws.nestle.recipes/resized/31d525faf51e6e2833c7b0f9a262e07f_boiled-egg_944_531.jpeg", width=500)
                    st.write('''ไข่เป็นอาหารที่มีคุณค่าทางโภชนาการสูงและเป็นที่รู้จักกันดีว่าเป็นแหล่งของโปรตีนและไขมันที่ดีต่อร่างกาย ไข่ 1 ฟองสามารถให้พลังงานสูงและมีโปรตีนคุณภาพสูงที่ช่วยสร้างกล้ามเนื้อและซ่อมแซมเนื้อเยื่อได้ดี''')
                with tab3:
                    st.header(" : ข้าวกล้อง ")
                    st.image("https://static.cdntap.com/tap-assets-prod/wp-content/uploads/sites/25/2023/07/can-pregnant-eat-brown-rice-3.jpg", width=500)
                    st.write('ข้าวกล้อง เป็นอาหารที่มีคาร์โบไฮเดรต จำพวกแป้งที่มีประโยชน์ ให้พลังงานที่สูง และมีวิตามินที่จำเป็น สามารถทานเป็นอาหารลดน้ำหนัก และอาหารเพิ่มน้ำหนักได้ โดยคนที่ต้องการเพิ่มน้ำหนักควรกินข้าวกล้องทุกมื้ออาหาร')
                with tab4:
                    st.header(" : น้ำผลไม้ ")
                    st.image("https://www.thaiheartfound.org/upload/26025/bf39fYbW3D.jpg", width=500)
                    st.write('น้ำผลไม้มีความหวานมาจากน้ำตาลธรรมชาติที่อยู่ในผลไม้เอง การดื่มน้ำผลไม้อย่างสม่ำเสมออาจทำให้ได้รับปริมาณคาร์โบไฮเดรตที่มากพอสำหรับการเพิ่มน้ำหนักหรือการเพิ่มไขมันตามความต้องการของร่างกาย ')
                    
                with tab5:
                    st.header(" : โยเกิร์ต ")
                    st.image("https://www.thaiheartfound.org/upload/26025/fpp8qhzopX.jpg", width=500)
                    st.write('เป็นแหล่งโปรตีนที่ดีและมีคุณค่าทางโภชนาการสูง เนื่องจากมักมีโปรตีนและไขมันที่ดี โยเกิร์ตที่มีโปรตีนและ ไขมันดีจะช่วยให้เพิ่มน้ำหนักได้')
                
            elif bmi >= 18.5 and bmi < 25:
                image = Image.open('streamlit/Normalweight.jpg')
                st.image(image)
                st.write(''':red[การดูแลเรื่องอาหาร:]เลือกกินอาหารให้เหมาะสมและมีประโยชน์ครบ 5 หมู่ โดยควรรวมอาหารหลากหลายและครบถ้วน เช่น ข้าว-แป้งขัดสีน้อย ธัญพืช ผักหลากหลาย ถั่ว และผลไม้อ่อนหวาน โดยบริบทนี้ควรมีปริมาณอย่างน้อย 400 กรัมต่อวัน เพื่อรับสารอาหารและวิตามินที่จำเป็นต่อร่างกาย และเพื่อรักษาและควบคุมน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม\n
:red[การออกกำลังกาย:]ออกกำลังกายหรือเคลื่อนไหวร่างกายสม่ำเสมอ โดยเลือกกิจกรรมที่มีความเข้มข้นปานกลางและสนุกสนาน เช่น เดินเร็ว, วิ่ง, ถีบจักรยาน, หรือเล่นกีฬาต่างๆ ออกกำลังกายอย่างสม่ำเสมอจะช่วยให้ร่างกายมีสุขภาพแข็งแรง ลดความเสี่ยงต่อโรคไม่ติดต่อเรื้อรัง และช่วยเพิ่มสมรรถภาพร่างกายด้วยการออกกำลังกายแบบแอโรบิค อย่างน้อยวันละ 20-30 นาที 3-4 วันต่อสัปดาห์\n
                         ''')
                st.header('อาหารคุมน้ำหนัก',divider='red')
                #header Normalweight
                tab6, tab7, tab8 = st.tabs(["สลัดผัก","ไก่ย่าง","แซลมอนย่าง"])
                with tab6:             
                    st.header(": สลัดผัก")
                    st.image("https://static.cdntap.com/tap-assets-prod/wp-content/uploads/sites/25/2022/06/salad-vegetables-list-lead.jpg", width=500)
                    st.write('สลัดผักช่วยเสริมความอิ่มด้วยใยอาหารและวิตามินต่างๆ')
                
                with tab7:             
                    st.header(": ไก่ย่าง")
                    st.image("https://food.mthai.com/app/uploads/2018/12/Grilled-Chicken-with-Turmeric.jpg", width=500)
                    st.write('ไก่เป็นแหล่งโปรตีนที่ดีและน้อยไขมัน มีวิตามินและแร่ธาตุสำคัญ เป็นอาหารที่มีพลังงานสูงและอิ่มท้อง')
                
                with tab8:             
                    st.header(": แซลมอนย่าง")
                    st.image("https://www.ajinomotofoodservicethailand.com/wp-content/uploads/2017/12/shutterstock_577605058-1920x1280.jpg", width=500)
                    st.write('เเซลมอนเป็นแหล่งโปรตีนและกรดไขมันอิ่มตัวในที่สุด มีไขมันดีช่วยลดความเสี่ยงต่อโรคหัวใจ')
                                 
            elif bmi >= 25 and bmi < 30:
                image = Image.open('streamlit/Overweight.jpg')
                st.image(image)
                st.write(''':red[การดูแลเรื่องอาหาร:] ควรเลือกกินอาหารที่มีประโยชน์และสมดุล โดยให้ครบ 5 หมู่ และคำนึงถึงปริมาณพลังงานที่เหมาะสมตามความต้องการของร่างกาย ควรลดการบริโภคอาหารที่มีน้ำตาล มัน และเค็ม และเน้นการบริโภคผลไม้ ผัก และธัญพืช\n
:red[ออกกำลังกาย:] เนื่องจากการออกกำลังกายช่วยในการเผาผลาญพลังงานและลดน้ำหนัก ควรเริ่มต้นด้วยกิจกรรมที่มีความเบาๆ เช่น การเดิน และเพิ่มความหนักและเวลาออกกำลังกายเรื่อยๆ ตามความพร้อมของร่างกาย''')
                st.header('อาหารคุมน้ำหนัก',divider='red')
                #header Overweight
                tab9, tab10, tab11 = st.tabs(["สลัดผัก","ปลากระพงนึ่งผัก","ไข่ต้มหรือไข่ตุ๋น"])
                with tab9:             
                    st.header(": สลัดผัก")
                    st.image("https://s359.kapook.com/pagebuilder/90cf722b-ded4-4809-9dd1-64a3e46b1ab2.jpg", width=500)
                    st.write('สลัดผักป็นเมนูที่ต่อยอดสำหรับการลดน้ำหนัก เนื่องจากมีพลังงานต่ำและสูงในใยอาหาร ช่วยเพิ่มความอิ่ม และลดความอยากอาหาร')
                with tab10:             
                    st.header(": ปลากระพงนึ่งผัก")
                    st.image("https://i.ytimg.com/vi/DTtWBRECdD0/maxresdefault.jpg", width=500)
                    st.write('ปลาเป็นอาหารที่มีโปรตีนสูงและไขมันไม่อันตราย มีกรดไขมันโอเมก้า-3 ที่ช่วยลดการอักเสบในร่างกาย และเสริมสารอาหารอื่น ๆ อีกมากมาย')
                with tab11:             
                    st.header(": ไข่ต้มหรือไข่ตุ๋น")
                    st.image("https://www.nestlemomandme.in.th/sites/default/files/content_image/AW_NST043316_NTDI_DigiA_10menu_Piconweb_03.jpg", width=500)
                    st.write('ไข่เป็นแหล่งโปรตีนคุณภาพสูง และสารอาหารอื่น ๆ เช่น วิตามิน B12, วิตามิน D และซีสเตอรอล ที่มีผลดีต่อระบบประสาทและระบบภูมิคุ้มกัน')
              
            else:
                 image = Image.open('streamlit/Obeseweight.jpg')
                 st.image(image)
                 st.write(''':red[การดูแลเรื่องอาหาร:] ควรเลือกกินอาหารที่มีประโยชน์โดยให้ครบ 5 หมู่ และคำนึงถึงปริมาณพลังงานที่เหมาะสมตามความต้องการของร่างกาย ควรลดการบริโภคอาหารที่มีน้ำตาล มัน และเค็ม และเน้นการบริโภคผลไม้ ผัก และธัญพืช\n
:red[ออกกำลังกาย:] เนื่องจากการออกกำลังกายช่วยในการเผาผลาญพลังงานและลดน้ำหนัก ควรเริ่มต้นด้วยกิจกรรมที่มีความเบาๆ เช่น การเดิน และเพิ่มความหนักและเวลาออกกำลังกายเรื่อยๆ ตามความพร้อมของร่างกาย''')
                 st.header('อาหารคุมน้ำหนัก',divider='red')
                #header Obese
                 tab12, tab13, tab14 = st.tabs(["ปลาแซลมอนอบ","สปาเก็ตตี้ผัดผัก","สลัดผักผลไม้"])
                 with tab12:             
                    st.header(": ปลาแซลมอนอบ")
                    st.image("https://st2.depositphotos.com/3833507/7193/i/450/depositphotos_71936917-stock-photo-fillet-of-salmon-with-asparagus.jpg", width=500)
                    st.write('แซลมอนเป็นแหล่งกรดไขมันโอเมก้า-3 ที่ดีต่อการลดความอ้วนและสุขภาพหัวใจ')
                 with tab13:             
                    st.header(": สปาเก็ตตี้ผัดผัก")
                    st.image("https://s.isanook.com/wo/0/ud/2/10718/food3.jpg", width=500)
                    st.write('สปาเก็ตตี้ผัดผักเป็นเมนูที่เหมาะสำหรับคนที่มีน้ำหนักเกินหรือโรคอ้วน เนื่องจากมีส่วนประกอบที่สมดุลและให้พลังงานไม่สูงมาก')
                 with tab14:             
                    st.header(": สลัดผักผลไม้")
                    st.image("https://sivasatciftligi.com/wp-content/uploads/2020/12/unnamed-1.jpg", width=500)
                    st.write(' สลัดผักผลไม้ มีใยอาหาร, วิตามิน, แร่ธาตุ และน้ำตาลธรรมชาติจากผลไม้')    
                 
    #home page sidebar        
    elif menu_option == 'Home page':
         video_file = open('streamlit/BOdy mask index.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         
         st.write('''ดัชนีมวลกาย หรือ BMI ย่อมาจาก Body Mass Index เป็นค่าสากลที่ใช้เพื่อคำนวณเพื่อหาน้ำหนักตัวที่ควรจะเป็น และประมาณระดับไขมันในร่างกายโดยใช้น้ำหนักตัว และส่วนสูง
การคำนวณดัชนีมวลกายไม่ใช่การวัดโดยตรงแต่ก็เป็นตัวชี้วัดไขมันในร่างกายที่ค่อนข้างเชื่อถือได้สำหรับคนส่วนใหญ่
ค่า BMI สามารถใช้บ่งบอกความเสี่ยงในการเกิดโรคต่างๆได้อีกด้วย เช่น โรคเบาหวาน ความดันโลหิตสูง ไขมันในเลือด ระบบหัวใจ รวมไปถึงมะเร็งบางชนิด
แต่อย่างไรก็ตามค่า BMI เป็นแค่การคำนวณเบื้องต้นเท่านั้น เนื่องจากคุณจำเป็นต้องนำปัจจัยอื่นๆ มาประกอบด้วย ทั้งเรื่องของพันธุกรรม ปริมาณกล้ามเนื้อ พฤติกรรมการกิน การใช้ชีวิต การออกกำลังกาย และอื่นๆ
                 ''')
         st.header('ความเสี่ยงจากการมีดัชนีมวลกายสูง',divider='red')
         st.write('''ดัชนีมวลกายสูงมักแสดงถึงมวลกายที่เกินมาก ซึ่งอาจส่งผลให้เกิดภาวะเสี่ยงต่อโรคหรือปัญหาสุขภาพอื่น ๆ ได้ตามที่กล่าวมาข้างต้น เป็นพื้นที่ที่ต้องให้ความสำคัญกับการดูแลสุขภาพอย่างสม่ำเสมอ 
                  และการปรับเปลี่ยนพฤติกรรมที่เกี่ยวข้องกับสุขภาพอย่างเหมาะสม เช่น การออกกำลังกายสม่ำเสมอ, การรักษาน้ำหนักให้อยู่ในเกณฑ์ที่เหมาะสม, การรับประทานอาหารที่มีประโยชน์, 
                  การลดบริโภคอาหารที่มีโภชนาการไม่ดี 
                  ''')
         image = Image.open('streamlit/removebg.png')
         st.image(image)  
         st.header('วิธีการเพิ่มหรือลดค่า BMI',divider='red')
         st.write(':red[- ควบคุมอาหาร :] รับประทานอาหารที่มีประโยชน์และลดการบริโภคอาหารที่มีไขมันและน้ำตาลสูง โดยเน้นผักผลไม้ ธัญพืช โปรตีนสูง และไขมันดี')
         st.write(':red[- ออกกำลังกาย :] เพิ่มการเคลื่อนไหวและออกกำลังกายอย่างสม่ำเสมอ เลือกกิจกรรมที่ชอบและทำได้เสมอ เช่น เดิน วิ่ง ว่ายน้ำ')
         st.write(':red[- พูดคุยกับผู้เชี่ยวชาญ :] หากต้องการคำแนะนำเพิ่มเติมในการควบคุมน้ำหนัก คุณสามารถพูดคุยกับนักโภชนาการหรือแพทย์ได้')
         st.write(':red[- ระมัดระวังกับการเพิ่มน้ำหนัก :] การเพิ่มน้ำหนักต้องเป็นอย่างระมัดระวังเพื่อไม่ให้เกินขีดจำกัดที่เป็นไปได้ เลือกกินอาหารที่มีประโยชน์และควบคุมสารอาหารอย่างเหมาะสม')
         st.image('https://static.thairath.co.th/media/dFQROr7oWzulq5Fa5K3y7TwF4LFOSrD9vTo84MxCkQHUoGKTRWfymL2xnMrEhaBDH9k.jpg')
         st.caption('Image credit URL:  https://static.thairath.co.th/media/dFQROr7oWzulq5Fa5K3y7TwF4LFOSrD9vTo84MxCkQHUoGKTRWfymL2xnMrEhaBDH9k.jpg')
    #side bar Health and exercise advice
    if menu_option == 'Health and exercise advice':
        st.subheader(':rainbow[Health and exercise advice]')
        st.image('https://t3.ftcdn.net/jpg/02/35/79/28/360_F_235792895_0SoLUsJ2PVOnjLWRtAqd6gLDuKJaDw93.jpg',width=600)
        st.caption('Image credit URL: https://t3.ftcdn.net/jpg/02/35/79/28/360_F_235792895_0SoLUsJ2PVOnjLWRtAqd6gLDuKJaDw93.jpg')
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


if __name__ == "__main__":
    main()
