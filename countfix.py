import streamlit as st
import random

# ตั้งค่าหน้าเว็บสไตล์โมเดิร์น
st.set_page_config(page_title="Buffet Master Wizard", page_icon="🍲", layout="centered")

# ระบบความจำชั่วคราว (Session State) จดจำหน้าปัจจุบัน
if "current_step" not in st.session_state:
    st.session_state.current_step = 1

# หัวข้อหลักบนหน้าจอมือถือ
st.markdown("<h1 style='text-align: center; color: #FF4B4B; font-size: 36px;'>🍲 Buffet Master Premium 🥓</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🛠️ ซ่อมแซมจุดนี้: เปลี่ยนคีย์ราคากลางให้เป็นภาษาไทยตรงตัว ป้องกัน KeyError 100%
def fetch_mega_market_prices():
    return {
        "เนื้อบริสเกต": round(random.uniform(260.0, 320.0), 2),
        "เนื้อไบพาย": round(random.uniform(280.0, 350.0), 2),
        "เนื้อน่องลายสไลด์": round(random.uniform(290.0, 360.0), 2),
        "สไบนาง": round(random.uniform(180.0, 240.0), 2),
        "หมูสามชั้นสไลด์": round(random.uniform(150.0, 190.0), 2),
        "สันคอหมูสไลด์": round(random.uniform(140.0, 180.0), 2),
        "หมูไม้ไผ่": round(random.uniform(130.0, 170.0), 2),
        "ไ้ส้หมู": round(random.uniform(120.0, 160.0), 2),
        "เนื้อไก่ดิบ": round(random.uniform(75.0, 95.0), 2),
        "ไข่ไก่": round(random.uniform(4.0, 5.5), 2), 
        "ไส้เป็ด": round(random.uniform(160.0, 220.0), 2),
        "กุ้ง": round(random.uniform(220.0, 270.0), 2),
        "ปลาหมึก": round(random.uniform(170.0, 230.0), 2),
        "แมงกะพรุน": round(random.uniform(130.0, 180.0), 2),
        "ปลาหมึกกรอบ": round(random.uniform(110.0, 150.0), 2),
        "เกี๊ยวผักโขมอบชีส": round(random.uniform(240.0, 300.0), 2),
        "เกี๊ยวหมู": round(random.uniform(120.0, 160.0), 2),
        "ปูอัด": round(random.uniform(110.0, 150.0), 2),
        "ลูกชิ้นหมู": round(random.uniform(100.0, 140.0), 2),
        "ลูกชิ้นเนื้อ": round(random.uniform(130.0, 170.0), 2),
        "ลูกชิ้นปลา": round(random.uniform(90.0, 130.0), 2),
        "ไส้กรอกไก่": round(random.uniform(80.0, 120.0), 2),
        "เต้าหู้ไข่": round(random.uniform(70.0, 100.0), 2),
        "เต้าหู้ปลา": round(random.uniform(100.0, 140.0), 2),
        "เต้าหู้ชีส": round(random.uniform(180.0, 240.0), 2),
        "ชิกุว่าไส้ชีส": round(random.uniform(190.0, 250.0), 2),
        "ชุดผักรวม": round(random.uniform(50.0, 70.0), 2),
        "ผักเดี่ยว": round(random.uniform(40.0, 60.0), 2), 
        "เส้นบะหมี่": round(random.uniform(50.0, 70.0), 2),
        "เส้นบะหมี่หยก": round(random.uniform(55.0, 75.0), 2),
        "เส้นหมี่": round(random.uniform(40.0, 60.0), 2),
        "วุ้นเส้น": round(random.uniform(45.0, 65.0), 2),
        "เส้นมันหนึบ": round(random.uniform(90.0, 130.0), 2),
        "เส้นบะหมี่กึ่ง": round(random.uniform(40.0, 55.0), 2)
    }

size_map = {"เล็ก (~45g)": 45, "กลาง (~120g)": 120, "ใหญ่ (~280g)": 280}

def menu_item_row(key_prefix, label_name):
    c_left, c_right = st.columns(2)
    with c_left:
        sz = st.selectbox(f"ไซส์ {label_name}:", ["เล็ก (~45g)", "กลาง (~120g)", "ใหญ่ (~280g)"], key=f"sz_{key_prefix}")
    with c_right:
        qty = st.number_input(f"จำนวนจาน:", min_value=0, value=0, key=f"qty_{key_prefix}")
    return qty * size_map[sz]

# --- หน้าที่ 1: กรอกราคาหัว ---
if st.session_state.current_step == 1:
    st.image("cover.png", use_container_width=True)
    st.write("### 💰 ขั้นตอนที่ 1: กรอกข้อมูลราคาร้าน")
    raw_price = st.number_input("ราคาหัวบุฟเฟต์หน้าร้าน (บาท):", min_value=0.0, value=399.0, step=10.0, key="wizard_raw_price")
    is_vat = st.toggle("ราคานี้ยังไม่รวม VAT 7%", value=True, key="wizard_is_vat")
    st.write("")
    if st.button("➡️ ไปเลือกรายการอาหาร", type="primary", use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()
# --- หน้าที่ 2: บันทึกรายการอาหาร ---
elif st.session_state.current_step == 2:
    st.write("### 🥢 ขั้นตอนที่ 2: บันทึกรายการอาหารที่กิน")
    st.info("💡 **คู่มือกะน้ำหนักถาดสากล:** ถาดคอนโดชาบู = 40-50g | จานเปลกลาง = 120g | จานใหญ่ = 280g")
    
    with st.expander("🥩 หมวดเนื้อวัวพรีเมียม (แยกจานอิสระ)", expanded=True):
        g_brisket = menu_item_row("brisket", "เนื้อบริสเกต")
        g_baipai = menu_item_row("baipai", "เนื้อไบพาย")
        g_nonglai = menu_item_row("nonglai", "เนื้อน่องลาย")
        g_sabainang = menu_item_row("sabainang", "สไบนาง")

    with st.expander("🐖 หมวดเนื้อหมูอนามัย (แยกจานอิสระ)", expanded=False):
        g_samchan = menu_item_row("samchan", "หมูสามชั้นสไลด์")
        g_sankor = menu_item_row("sankor", "สันคอหมูสไลด์")
        g_maipai = menu_item_row("maipai", "หมูไม้ไผ่")
        g_sai_moo = menu_item_row("saimoo", "ไส้หมู")

    with st.expander("🐓 เมนูไก่และไข่", expanded=False):
        g_chicken_lava = st.number_input("ไก่ลาวา (กรัม):", min_value=0, value=0, step=50, key="w_chicken_lava")
        pcs_egg = st.number_input("ไข่ไก่ (จำนวนฟอง):", min_value=0, value=0, step=1, key="w_pcs_egg")

    with st.expander("🦆 เมนูเป็ด", expanded=False):
        g_sai_ped = st.number_input("ไส้เป็ด (กรัม):", min_value=0, value=0, step=50, key="w_sai_ped")

    with st.expander("🦐 เมนูซีฟู๊ด", expanded=False):
        g_shrimp = st.number_input("กุ้ง (กรัม):", min_value=0, value=0, step=50, key="w_shrimp")
        g_squid = st.number_input("ปลาหมึก (กรัม):", min_value=0, value=0, step=50, key="w_squid")
        g_jellyfish = st.number_input("แมงกะพรุน (กรัม):", min_value=0, value=0, step=50, key="w_jellyfish")
        g_crispy_squid = st.number_input("ปลาหมึกกรอบ (กรัม):", min_value=0, value=0, step=50, key="w_crispy_squid")

    with st.expander("🥟 เมนูเกี๊ยว", expanded=False):
        g_spinach_cheese = st.number_input("เกี๊ยวผักโขมอบชีส (กรัม):", min_value=0, value=0, step=50, key="w_spinach_cheese")
        g_pork_wonton = st.number_input("เกี๊ยวหมู (กรัม):", min_value=0, value=0, step=50, key="w_pork_wonton")

    with st.expander("🍥 เมนูของแปรรูป", expanded=False):
        g_crab = st.number_input("ปูอัด (กรัม):", min_value=0, value=0, step=50, key="w_crab")
        g_lookchin_moo = st.number_input("ลูกชิ้นหมู (กรัม):", min_value=0, value=0, step=30, key="w_lookchin_moo")
        g_lookchin_neua = st.number_input("ลูกชิ้นเนื้อ (กรัม):", min_value=0, value=0, step=30, key="w_lookchin_neua")
        g_lookchin_pla = st.number_input("ลูกชิ้นปลา (กรัม):", min_value=0, value=0, step=30, key="w_lookchin_pla")
        g_sausage = st.number_input("ไส้กรอกไก่ (กรัม):", min_value=0, value=0, step=30, key="w_sausage")
        g_tofu_egg = st.number_input("เต้าหู้ไข่ (กรัม):", min_value=0, value=0, step=30, key="w_tofu_egg")
        g_tofu_pla = st.number_input("เต้าหู้ปลา (กรัม):", min_value=0, value=0, step=30, key="w_tofu_pla")
        g_tofu_cheese = st.number_input("เต้าหู้ชีส (กรัม):", min_value=0, value=0, step=30, key="w_tofu_cheese")
        g_chikuwa_cheese = st.number_input("ชิกุว่าไส้ชีส (กรัม):", min_value=0, value=0, step=30, key="w_chikuwa_cheese")

    with st.expander("🥬 เมนูผักสวนครัว", expanded=False):
        use_veg_set = st.checkbox("🔄 ฉันเลือกทานเป็น 'ชุดผักรวม'", value=False, key="w_use_veg_set")
        if use_veg_set:
            g_veg_set = st.number_input("ปริมาณชุดผักรวมทั้งหมด (กรัม):", min_value=0, value=200, step=50, key="w_g_veg_set")
            g_osun = g_kard = g_bung = g_kana = g_kablam = g_kwangtung = g_khunchai = g_needle = g_orinj = g_shii = g_carrot = g_radish = 0
        else:
            g_veg_set = 0
            c_v1, c_v2 = st.columns(2)
            with c_v1:
                g_osun = st.number_input("ผักโอซุ่น (กรัม):", min_value=0, value=0, step=20, key="w_g_osun")
                g_kard = st.number_input("ผักกาด (กรัม):", min_value=0, value=0, step=20, key="w_g_kard")
                g_bung = st.number_input("ผักบุ้ง (กรัม):", min_value=0, value=0, step=20, key="w_g_bung")
                g_kana = st.number_input("ผักคะน้า (กรัม):", min_value=0, value=0, step=20, key="w_g_kana")
                g_kablam = st.number_input("ผักกะหล่ำ (กรัม):", min_value=0, value=0, step=20, key="w_g_kablam")
                g_kwangtung = st.number_input("ผักกวางตุ้ง (กรัม):", min_value=0, value=0, step=20, key="w_g_kwangtung")
            with c_v2:
                g_khunchai = st.number_input("ผักคื่นช่าย (กรัม):", min_value=0, value=0, step=10, key="w_g_khunchai")
                g_needle = st.number_input("เห็ดเข็มทอง (กรัม):", min_value=0, value=0, step=20, key="w_g_needle")
                g_orinj = st.number_input("เห็ดออรินจิ (กรัม):", min_value=0, value=0, step=20, key="w_g_orinj")
                g_shii = st.number_input("เห็ดหอม (กรัม):", min_value=0, value=0, step=20, key="w_g_shii")
                g_carrot = st.number_input("แครอท (กรัม):", min_value=0, value=0, step=20, key="w_g_carrot")
                g_radish = st.number_input("หัวไชเท้า (กรัม):", min_value=0, value=0, step=20, key="w_g_radish")

    with st.expander("🍜 เมนูเส้นประหยัดท้อง", expanded=False):
        g_n_normal = st.number_input("เส้นบะหมี่ (กรัม):", min_value=0, value=0, step=30, key="w_g_n_normal")
        g_n_jade = st.number_input("เส้นบะหมี่หยก (กรัม):", min_value=0, value=0, step=30, key="w_g_n_jade")
        g_n_mee = st.number_input("เส้นหมี่ (กรัม):", min_value=0, value=0, step=30, key="w_g_n_mee")
        g_glass = st.number_input("วุ้นเส้น (กรัม):", min_value=0, value=0, step=30, key="w_g_glass")
        g_sticky = st.number_input("เส้นมันหนึบ (กรัม):", min_value=0, value=0, step=30, key="w_g_sticky")
        g_instant = st.number_input("เส้นบะหมี่กึ่ง (กรัม):", min_value=0, value=0, step=30, key="w_g_instant")
        
    st.write("")
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("⬅️ ย้อนกลับไปหน้าแรก", use_container_width=True):
            st.session_state.current_step = 1
            st.rerun()
    with c_btn2:
        if st.button("➡️ ไปหน้าสรุปความคุ้ม", type="primary", use_container_width=True):
            st.session_state.current_step = 3
            st.rerun()
# --- หน้าที่ 3: สรุปรายงานวิเคราะห์ความคุ้มค่า ---
elif st.session_state.current_step == 3:
    st.write("### 🚀 ขั้นตอนที่ 3: สรุปผลความคุ้มค่าสุทธิของคุณ")
    
    prices = fetch_mega_market_prices()
    r_price = st.session_state.get("wizard_raw_price", 399.0)
    v_toggle = st.session_state.get("wizard_is_vat", True)
    total_buffet_cost = r_price * 1.07 if v_toggle else r_price
    
    v_beef = ((g_brisket * prices["เนื้อบริสเกต"]) + (g_baipai * prices["เนื้อไบพาย"]) + 
              (g_nonglai * prices["เนื้อน่องลายสไลด์"]) + (g_sabainang * prices["สไบนาง"])) / 1000
    v_pork = ((g_samchan * prices["หมูสามชั้นสไลด์"]) + (g_sankor * prices["สันคอหมูสไลด์"]) + 
              (g_maipai * prices["หมูไม้ไผ่"]) + (g_sai_moo * prices["ไ้ส้หมู"])) / 1000
    v_chicken_lava = ((g_chicken_lava * prices["เนื้อไก่ดิบ"]) / 1000) + ((g_chicken_lava / 100) * prices["ไข่ไก่"])
    v_eggs = pcs_egg * prices["ไข่ไก่"]
    v_duck = (g_sai_ped * prices["ไส้เป็ด"]) / 1000
    v_seafood = ((g_shrimp * prices["กุ้ง"]) + (g_squid * prices["ปลาหมึก"]) + 
                 (g_jellyfish * prices["แมงกะพรุน"]) + (g_crispy_squid * prices["ปลาหมึกกรอบ"])) / 1000
    v_wonton = ((g_spinach_cheese * prices["เกี๊ยวผักโขมอบชีส"]) + (g_pork_wonton * prices["เกี๊ยวหมู"])) / 1000
    v_processed = ((g_crab * prices["ปูอัด"]) + (g_lookchin_moo * prices["ลูกชิ้นหมู"]) + 
                   (g_lookchin_neua * prices["ลูกชิ้นเนื้อ"]) + (g_lookchin_pla * prices["ลูกชิ้นปลา"]) + 
                   (g_sausage * prices["ไส้กรอกไก่"]) + (g_tofu_egg * prices["เต้าหู้ไข่"]) + 
                   (g_tofu_pla * prices["เต้าหู้ปลา"]) + (g_tofu_cheese * prices["เต้าหู้ชีส"]) + 
                   (g_chikuwa_cheese * prices["ชิกุว่าไส้ชีส"])) / 1000
    if use_veg_set:
        v_veg = (g_veg_set * prices["ชุดผักรวม"]) / 1000
    else:
        total_veg_g = g_osun + g_kard + g_bung + g_kana + g_kablam + g_kwangtung + g_khunchai + g_needle + g_orinj + g_shii + g_carrot + g_radish
        v_veg = (total_veg_g * prices["ผักเดี่ยว"]) / 1000
    v_lines = ((g_n_normal * prices["เส้นบะหมี่"]) + (g_n_jade * prices["เส้นบะหมี่หยก"]) + 
               (g_n_mee * prices["เส้นหมี่"]) + (g_glass * prices["วุ้นเส้น"]) + 
               (g_sticky * prices["เส้นมันหนึบ"]) + (g_instant * prices["เส้นบะหมี่กึ่ง"])) / 1000

    grand_eaten_value = v_beef + v_pork + v_chicken_lava + v_eggs + v_duck + v_seafood + v_wonton + v_processed + v_veg + v_lines
    final_ratio = (grand_eaten_value / total_buffet_cost) * 100
    
    st.write("📊 **หลอดเกจระดับความคุ้มค่าของคุณ:**")
    st.progress(min(int(final_ratio), 100) / 100)

    if final_ratio >= 130:
        st.balloons()
        status_label = "🏆 มหาเทพนักกินกินล้างบาง"
        st.markdown(f"<div style='background-color: #d4edda; padding: 15px; border-radius: 8px; border-left: 5px solid #28a745;'><h4 style='color: #155724; margin: 0;'>👑 ระดับ: สุดยอดนักกินล้างบางตู้ชาบู! ({final_ratio:.1f}%)</h4></div>", unsafe_allow_html=True)
    elif final_ratio >= 100:
        status_label = "🟢 กินคุ้มค่าได้ทุนคืน"
        st.markdown(f"<div style='background-color: #d1ecf1; padding: 15px; border-radius: 8px; border-left: 5px solid #17a2b8;'><h4 style='color: #0c5460; margin: 0;'>🟢 ระดับ: มหาเศรษฐีบุฟเฟต์คืนทุนตัวจริง ({final_ratio:.1f}%)</h4></div>", unsafe_allow_html=True)
    elif final_ratio >= 65:
        status_label = "🟡 กินพอดีเน้นอิ่มสบาย"
        st.markdown(f"<div style='background-color: #fff3cd; padding: 15px; border-radius: 8px; border-left: 5px solid #ffc107;'><h4 style='color: #856404; margin: 0;'>🟡 ระดับ: อิ่มแปล้เน้นรักษาสุขภาพทางใจ ({final_ratio:.1f}%)</h4></div>", unsafe_allow_html=True)
    else:
        status_label = "🔴 ผู้บริจาคเงินให้ร้านค้า"
        st.markdown(f"<div style='background-color: #f8d7da; padding: 15px; border-radius: 8px; border-left: 5px solid #dc3545;'><h4 style='color: #721c24; margin: 0;'>🔴 ระดับ: สมาคมผู้บริจาคกำไรให้ร้านค้า ({final_ratio:.1f}%)</h4></div>", unsafe_allow_html=True)

    st.write("")
    c_m1, c_m2 = st.columns(2)
    c_m1.metric(label="ค่าหัวเน็ตสุทธิรวม VAT", value=f"{total_buffet_cost:.2f} บาท")
    c_m2.metric(label="มูลค่าอาหารรวมตามราคาตลาดสด", value=f"{grand_eaten_value:.2f} บาท", delta=f"{grand_eaten_value - total_buffet_cost:.2f} บาท")

    st.markdown("### 📋 สรุปผลการทาน (คลิกไอคอนขวาบนเพื่อคัดลอก)")
    summary_text = (
        f"📋 [รายงานความคุ้มค่าบุฟเฟต์]\n"
        f"💰 ราคาหน้าร้านสุทธิ: {total_buffet_cost:.2f} บาท\n"
        f"🥩 มูลค่าของสดที่กินจริง: {grand_eaten_value:.2f} บาท\n"
        f"📈 เปอร์เซ็นต์ความคุ้ม: {final_ratio:.1f}%\n"
        f"🏅 ผลประเมิน: {status_label}\n"
        f"🤖 คำนวณผ่านแอป Buffet Master Premium"
    )
    st.code(summary_text, language="text")
    
    st.write("")
    if st.button("⬅️ กลับไปแก้ไขรายการอาหาร", use_container_width=True):
        st.session_state.current_step = 2
        st.rerun()
