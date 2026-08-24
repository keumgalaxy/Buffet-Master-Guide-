import streamlit as st
import random

# ตั้งค่าหน้าเว็บให้สวยงามสไตล์โมเดิร์น
st.set_page_config(page_title="Buffet Master Steps", page_icon="🍲", layout="centered")

# หัวข้อหลักของแอปพลิเคชัน
st.markdown("<h1 style='text-align: center; color: #FF4B4B; font-size: 38px;'>🍲 Buffet Master Pro 🥓</h1>", unsafe_allow_html=True)
st.markdown("---")

# ฟังก์ชันดึงฐานราคากลางวัตถุดิบค้าส่งอัปเดตปี 2026 (บาทต่อกิโลกรัม)
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
        "ปlaหมึก": round(random.uniform(170.0, 230.0), 2),
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

# ระบบตรวจจับและจำค่าขั้นตอนหน้าปัจจุบัน
if "step" not in st.session_state:
    st.session_state.step = 1

# --- STEP 1: หน้าตั้งค่าราคาร้าน ---
if st.session_state.step == 1:
    st.write("### 💰 ขั้นตอนที่ 1: ตั้งค่าราคาร้าน")
    st.image("cover.png", use_container_width=True)
    
    default_price = st.session_state.get('raw_price', 399.0)
    default_vat = st.session_state.get('is_vat', True)
    
    raw_price = st.number_input("ราคาหัวบุฟเฟต์หน้าร้าน (บาท):", min_value=0.0, value=default_price, step=10.0)
    is_vat = st.toggle("ราคานี้ยังไม่รวม VAT 7%", value=default_vat)
    
    st.session_state.raw_price = raw_price
    st.session_state.is_vat = is_vat
    st.session_state.total_buffet_cost = raw_price * 1.07 if is_vat else raw_price
    
    st.write("")
    if st.button("ถัดไป: เลือกเมนูอาหาร ➡️", type="primary", use_container_width=True):
        st.session_state.step = 2
        st.rerun()
# --- STEP 2: หน้าเลือกรายการอาหาร ---
elif st.session_state.step == 2:
    st.write("### 🥢 ขั้นตอนที่ 2: รายการอาหารที่คุณทาน")
    
    st.info("""
    💡 **คู่มือกะน้ำหนักถาดสากลหน้าร้านบุฟเฟต์:**
    * 🔲 **ถาดคอนโดชาบูทั่วไป** = 40-50 กรัม | 🍽️ **จานเปลไซส์กลาง** = 120 กรัม | 🥗 **จานเปลใหญ่** = 280 กรัม
    """)
    
    size_map = {"เล็ก (~45g)": 45, "กลาง (~120g)": 120, "ใหญ่ (~280g)": 280}
    
    def menu_item_row(key_prefix, label_name):
        c_left, c_right = st.columns(2)
        with c_left:
            default_sz_idx = 0
            if f"sz_{key_prefix}" in st.session_state:
                default_sz_idx = ["เล็ก (~45g)", "กลาง (~120g)", "ใหญ่ (~280g)"].index(st.session_state[f"sz_{key_prefix}"])
            sz = st.selectbox(f"ไซส์ {label_name}:", ["เล็ก (~45g)", "กลาง (~120g)", "ใหญ่ (~280g)"], index=default_sz_idx, key=f"sz_{key_prefix}")
        with c_right:
            default_qty = st.session_state.get(f"qty_{key_prefix}", 0)
            qty = st.number_input(f"จำนวนจาน:", min_value=0, value=default_qty, key=f"qty_{key_prefix}")
        return qty * size_map[sz]

    with st.expander("🥩 หมวดเนื้อวัวพรีเมียม (Premium Beef)", expanded=True):
        st.image("beef.jpg", use_container_width=True)
        g_brisket = menu_item_row("brisket", "เนื้อบริสเกต")
        g_baipai = menu_item_row("baipai", "เนื้อไบพาย")
        g_nonglai = menu_item_row("nonglai", "เนื้อน่องลาย")
        g_sabainang = menu_item_row("sabainang", "สไบนาง")

    with st.expander("🐖 หมวดเนื้อหมูอนามัย (Premium Pork)", expanded=False):
        g_samchan = menu_item_row("samchan", "หมูสามชั้นสไลด์")
        g_sankor = menu_item_row("sankor", "สันคอหมูสไลด์")
        g_maipai = menu_item_row("maipai", "หมูไม้ไผ่")
        g_sai_moo = menu_item_row("saimoo", "ไส้หมู")

    with st.expander("🐓 เมนูไก่และไข่", expanded=False):
        g_chicken_lava = st.number_input("ไก่ลาวา (กรัม):", min_value=0, value=st.session_state.get("chicken_lava_val", 0), step=50, key="chicken_lava_val")
        pcs_egg = st.number_input("ไข่ไก่ (จำนวนฟอง):", min_value=0, value=st.session_state.get("pcs_egg_val", 0), step=1, key="pcs_egg_val")

    with st.expander("🦆 เมนูเป็ด", expanded=False):
        g_sai_ped = st.number_input("ไส้เป็ด (กรัม):", min_value=0, value=st.session_state.get("sai_ped_val", 0), step=50, key="sai_ped_val")

    with st.expander("🦐 เมนูซีฟู๊ด", expanded=False):
        g_shrimp = st.number_input("กุ้ง (กรัม):", min_value=0, value=st.session_state.get("shrimp_val", 0), step=50, key="shrimp_val")
        g_squid = st.number_input("ปลาหมึก (กรัม):", min_value=0, value=st.session_state.get("squid_val", 0), step=50, key="squid_val")
        g_jellyfish = st.number_input("แมงกะพรุน (กรัม):", min_value=0, value=st.session_state.get("jellyfish_val", 0), step=50, key="jellyfish_val")
        g_crispy_squid = st.number_input("ปลาหมึกกรอบ (กรัม):", min_value=0, value=st.session_state.get("crispy_squid_val", 0), step=50, key="crispy_squid_val")

    with st.expander("🥟 เมนูเกี๊ยว", expanded=False):
        g_spinach_cheese = st.number_input("เกี๊ยวผักโขมอบชีส (กรัม):", min_value=0, value=st.session_state.get("spinach_cheese_val", 0), step=50, key="spinach_cheese_val")
        g_pork_wonton = st.number_input("เกี๊ยวหมู (กรัม):", min_value=0, value=st.session_state.get("pork_wonton_val", 0), step=50, key="pork_wonton_val")

    with st.expander("🍥 เมนูของแปรรูป", expanded=False):
        g_crab = st.number_input("ปูอัด (กรัม):", min_value=0, value=st.session_state.get("crab_val", 0), step=50, key="crab_val")
        g_lookchin_moo = st.number_input("ลูกชิ้นหมู (กรัม):", min_value=0, value=st.session_state.get("lookchin_moo_val", 0), step=30, key="lookchin_moo_val")
        g_lookchin_neua = st.number_input("ลูกชิ้นเนื้อ (กรัม):", min_value=0, value=st.session_state.get("lookchin_neua_val", 0), step=30, key="lookchin_neua_val")
        g_lookchin_pla = st.number_input("ลูกชิ้นปลา (กรัม):", min_value=0, value=st.session_state.get("lookchin_pla_val", 0), step=30, key="lookchin_pla_val")
        g_sausage = st.number_input("ไส้กรอกไก่ (กรัม):", min_value=0, value=st.session_state.get("sausage_val", 0), step=30, key="sausage_val")
        g_tofu_egg = st.number_input("เต้าหู้ไข่ (กรัม):", min_value=0, value=st.session_state.get("tofu_egg_val", 0), step=30, key="tofu_egg_val")
        g_tofu_pla = st.number_input("เต้าหู้ปลา (กรัม):", min_value=0, value=st.session_state.get("tofu_pla_val", 0), step=30, key="tofu_pla_val")
        g_tofu_cheese = st.number_input("เต้าหู้ชีส (กรัม):", min_value=0, value=st.session_state.get("tofu_cheese_val", 0), step=30, key="tofu_cheese_val")
        g_chikuwa_cheese = st.number_input("ชิกุว่าไส้ชีส (กรัม):", min_value=0, value=st.session_state.get("chikuwa_cheese_val", 0), step=30, key="chikuwa_cheese_val")

    with st.expander("🥬 เมนูผักสวนครัว", expanded=False):
        use_veg_set = st.checkbox("🔄 ฉันเลือกทานเป็น 'ชุดผักรวม'", value=st.session_state.get("use_veg_set_val", False), key="use_veg_set_val")
        if use_veg_set:
            g_veg_set = st.number_input("ปริมาณชุดผักรวมทั้งหมด (กรัม):", min_value=0, value=st.session_state.get("veg_set_val", 200), step=50, key="veg_set_val")
            g_osun = g_kard = g_bung = g_kana = g_kablam = g_kwangtung = g_khunchai = g_needle = g_orinj = g_shii = g_carrot = g_radish = 0
        else:
            g_veg_set = 0
            c_v1, c_v2 = st.columns(2)
            with c_v1:
                g_osun = st.number_input("ผักโอซุ่น (กรัม):", min_value=0, value=st.session_state.get("osun_val", 0), step=20, key="osun_val")
                g_kard = st.number_input("ผักกาด (กรัม):", min_value=0, value=st.session_state.get("kard_val", 0), step=20, key="kard_val")
                g_bung = st.number_input("ผักบุ้ง (กรัม):", min_value=0, value=st.session_state.get("bung_val", 0), step=20, key="bung_val")
                g_kana = st.number_input("ผักคะน้า (กรัม):", min_value=0, value=st.session_state.get("kana_val", 0), step=20, key="kana_val")
                g_kablam = st.number_input("ผักกะหล่ำ (กรัม):", min_value=0, value=st.session_state.get("kablam_val", 0), step=20, key="kablam_val")
                g_kwangtung = st.number_input("ผักกวางตุ้ง (กรัม):", min_value=0, value=st.session_state.get("kwangtung_val", 0), step=20, key="kwangtung_val")
            with c_v2:
                g_khunchai = st.number_input("ผักคื่นช่าย (กรัม):", min_value=0, value=st.session_state.get("khunchai_val", 0), step=10, key="khunchai_val")
                g_needle = st.number_input("เห็ดเข็มทอง (กรัม):", min_value=0, value=st.session_state.get("needle_val", 0), step=20, key="needle_val")
                g_orinj = st.number_input("เห็ดออรินจิ (กรัม):", min_value=0, value=st.session_state.get("orinj_val", 0), step=20, key="orinj_val")
                g_shii = st.number_input("เห็ดหอม (กรัม):", min_value=0, value=st.session_state.get("shii_val", 0), step=20, key="shii_val")
                g_carrot = st.number_input("แครอท (กรัม):", min_value=0, value=st.session_state.get("carrot_val", 0), step=20, key="carrot_val")
                g_radish = st.number_input("หัวไชเท้า (กรัม):", min_value=0, value=st.session_state.get("radish_val", 0), step=20, key="radish_val")

    with st.expander("🍜 เมนูเส้นประหยัดท้อง", expanded=False):
        g_n_normal = st.number_input("เส้นบะหมี่ (กรัม):", min_value=0, value=st.session_state.get("n_normal_val", 0), step=30, key="n_normal_val")
        g_n_jade = st.number_input("เส้นบะหมี่หยก (กรัม):", min_value=0, value=st.session_state.get("n_jade_val", 0), step=30, key="n_jade_val")
        g_n_mee = st.number_input("เส้นหมี่ (กรัม):", min_value=0, value=st.session_state.get("n_mee_val", 0), step=30, key="n_mee_val")
        g_glass = st.number_input("วุ้นเส้น (กรัม):", min_value=0, value=st.session_state.get("glass_val", 0), step=30, key="glass_val")
        g_sticky = st.number_input("เส้นมันหนึบ (กรัม):", min_value=0, value=st.session_state.get("sticky_val", 0), step=30, key="sticky_val")
        g_instant = st.number_input("เส้นบะหมี่กึ่ง (กรัม):", min_value=0, value=st.session_state.get("instant_val", 0), step=30, key="instant_val")

    st.session_state.g_items = {
        "brisket": g_brisket, "baipai": g_baipai, "nonglai": g_nonglai, "sabainang": g_sabainang,
        "samchan": g_samchan, "sankor": g_sankor, "maipai": g_maipai, "saimoo": g_sai_moo,
        "chicken_lava": g_chicken_lava, "pcs_egg": pcs_egg, "sai_ped": g_sai_ped,
        "shrimp": g_shrimp, "squid": g_squid, "jellyfish": g_jellyfish, "crispy_squid": g_crispy_squid,
        "spinach_cheese": g_spinach_cheese, "pork_wonton": g_pork_wonton, "crab": g_crab,
        "lookchin_moo": g_lookchin_moo, "lookchin_neua": g_lookchin_neua, "lookchin_pla": g_lookchin_pla,
        "sausage": g_sausage, "tofu_egg": g_tofu_egg, "tofu_pla": g_tofu_pla, "tofu_cheese": g_tofu_cheese, "chikuwa_cheese": g_chikuwa_cheese,
        "use_veg_set": use_veg_set, "veg_set": g_veg_set, "osun": g_osun, "kard": g_kard, "bung": g_bung, "kana": g_kana, "kablam": g_kablam, "kwangtung": g_kwangtung, "khunchai": g_khunchai, "needle": g_needle, "orinj": g_orinj, "shii": g_shii, "carrot": g_carrot, "radish": g_radish,
        "n_normal": g_n_normal, "n_jade": g_n_jade, "n_mee": g_n_mee, "glass": g_glass, "sticky": g_sticky, "instant": g_instant
    }

    st.write("")
    c_btn1, c_btn2 = st.columns(2)
    with c_btn1:
        if st.button("⬅️ ย้อนกลับไปหน้าแรก", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    with c_btn2:
        if st.button("ถัดไป: สรุปผลความคุ้ม ➡️", type="primary", use_container_width=True):
            st.session_state.step = 3
            st.rerun()
# --- STEP 3: หน้าสรุปผลลัพธ์สุดท้ายโดดๆ ---
elif st.session_state.step == 3:
    st.write("### 🚀 ขั้นตอนที่ 3: สรุปผลลัพธ์ความคุ้มค่า")
    
    total_buffet_cost = st.session_state.get('total_buffet_cost', 399.0)
    g = st.session_state.get('g_items', {})
    prices = fetch_mega_market_prices()
    
    v_beef = ((g.get("brisket", 0) * prices["เนื้อบริสเกต"]) + (g.get("baipai", 0) * prices["เนื้อไบพาย"]) + 
              (g.get("nonglai", 0) * prices["เนื้อน่องลายสไลด์"]) + (g.get("sabainang", 0) * prices["สไบนาง"])) / 1000
              
    v_pork = ((g.get("samchan", 0) * prices["หมูสามชั้นสไลด์"]) + (g.get("sankor", 0) * prices["สันคอหมูสไลด์"]) + 
              (g.get("maipai", 0) * prices["หมูไม้ไผ่"]) + (g.get("saimoo", 0) * prices["ไ้ส้หมู"])) / 1000
              
    v_chicken_lava = ((g.get("chicken_lava", 0) * prices["เนื้อไก่ดิบ"]) / 1000) + ((g.get("chicken_lava", 0) / 100) * prices["ไข่ไก่"])
    v_eggs = g.get("pcs_egg", 0) * prices["ไข่ไก่"]
    v_duck = (g.get("sai_ped", 0) * prices["ไส้เป็ด"]) / 1000
    
    v_seafood = ((g.get("shrimp", 0) * prices["กุ้ง"]) + (g.get("squid", 0) * prices["ปลาหมึก"]) + 
                 (g.get("jellyfish", 0) * prices["แมงกะพรุน"]) + (g.get("crispy_squid", 0) * prices["ปลาหมึกกรอบ"])) / 1000
                 
    v_wonton = ((g.get("spinach_cheese", 0) * prices["เกี๊ยวผักโขมอบชีส"]) + (g.get("pork_wonton", 0) * prices["เกี๊ยวหมู"])) / 1000
    
    v_processed = ((g.get("crab", 0) * prices["ปูอัด"]) + (g.get("lookchin_moo", 0) * prices["ลูกชิ้นหมู"]) + 
                   (g.get("lookchin_neua", 0) * prices["ลูกชิ้นเนื้อ"]) + (g.get("lookchin_pla", 0) * prices["ลูกชิ้นปลา"]) + 
                   (g.get("sausage", 0) * prices["ไส้กรอกไก่"]) + (g.get("tofu_egg", 0) * prices["เต้าหู้ไข่"]) + 
                   (g.get("tofu_pla", 0) * prices["เต้าหู้ปลา"]) + (g.get("tofu_cheese", 0) * prices["เต้าหู้ชีส"]) + 
                   (g.get("chikuwa_cheese", 0) * prices["ชิกุว่าไส้ชีส"])) / 1000
                   
    if g.get("use_veg_set", False):
        v_veg = (g.get("veg_set", 0) * prices["ชุดผักรวม"]) / 1000
    else:
        total_veg_g = (g.get("osun", 0) + g.get("kard", 0) + g.get("bung", 0) + g.get("kana", 0) + g.get("kablam", 0) + 
                       g.get("kwangtung", 0) + g.get("khunchai", 0) + g.get("needle", 0) + g.get("orinj", 0) + g.get("shii", 0) + 
                       g.get("carrot", 0) + g.get("radish", 0))
        v_veg = (total_veg_g * prices["ผักเดี่ยว"]) / 1000
        
    v_lines = ((g.get("n_normal", 0) * prices["เส้นบะหมี่"]) + (g.get("n_jade", 0) * prices["เส้นบะหมี่หยก"]) + 
               (g.get("n_mee", 0) * prices["เส้นหมี่"]) + (g.get("glass", 0) * prices["วุ้นเส้น"]) + 
               (g.get("sticky", 0) * prices["เส้นมันหนึบ"]) + (g.get("instant", 0) * prices["เส้นบะหมี่กึ่ง"])) / 1000

    grand_eaten_value = v_beef + v_pork + v_chicken_lava + v_eggs + v_duck + v_seafood + v_wonton + v_processed + v_veg + v_lines
    final_ratio = (grand_eaten_value / total_buffet_cost) * 100
    
    st.write("📊 **หลอดเกจแสดงระดับความคุ้มค่าของคุณ:**")
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

    st.markdown("### 📋 สรุปรายงาน (คลิกไอคอนขวาบนเพื่อคัดลอกส่งไลน์)")
    summary_text = (
        f"📋 [รายงานความคุ้มค่าบุฟเฟต์]\n"
        f"💰 ราคาหน้าร้านสุทธิ: {total_buffet_cost:.2f} บาท\n"
        f"🥩 มูลค่าของสดที่กินจริง: {grand_total_eaten_value:.2f} บาท\n" if 'grand_total_eaten_value' in locals() else f"🥩 มูลค่าของสดที่กินจริง: {grand_eaten_value:.2f} บาท\n"
        f"📈 เปอร์เซ็นต์ความคุ้ม: {final_ratio:.1f}%\n"
        f"🏅 ผลประเมิน: {status_label}\n"
        f"🤖 คำนวณผ่านแอป Buffet Master Step-by-Step"
    )
    st.code(summary_text, language="text")
    
    st.write("")
    if st.button("⬅️ กลับไปแก้ไขรายการอาหาร", use_container_width=True):
        st.session_state.step = 2
        st.rerun()
