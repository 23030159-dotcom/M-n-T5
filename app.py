import streamlit as st

st.set_page_config(
    page_title="Thẩm định cho vay doanh nghiệp",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    background-color: #0066cc;
    color: white;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    font-size:18px;
}
.result-box{
    padding:20px;
    border-radius:15px;
    background-color:#eaf4ff;
    margin-top:20px;
}
</style>
""", unsafe_allow_html=True)

st.title("🏦 HỆ THỐNG THẨM ĐỊNH CHO VAY DOANH NGHIỆP")

st.subheader("Nhập thông tin doanh nghiệp")

col1, col2 = st.columns(2)

with col1:
    roa = st.number_input("ROA (%)", value=5.0)
    roe = st.number_input("ROE (%)", value=12.0)
    lnst = st.number_input("Lợi nhuận sau thuế (VNĐ)", value=100000000)

with col2:
    tsdb = st.number_input("Giá trị tài sản bảo đảm (VNĐ)", value=1000000000)
    so_tien_vay = st.number_input("Số tiền vay (VNĐ)", value=500000000)
    thoi_gian_vay = st.number_input("Thời gian vay (năm)", value=3)
    lai_suat = st.number_input("Lãi suất (%/năm)", value=10.0)

if st.button("ĐÁNH GIÁ KHOẢN VAY"):

    diem = 0

    if roa >= 5:
        diem += 30
    elif roa >= 3:
        diem += 15

    if roe >= 10:
        diem += 30
    elif roe >= 5:
        diem += 15

    if lnst > 0:
        diem += 20

    ty_le_tsdb = tsdb / so_tien_vay

    if ty_le_tsdb >= 1.5:
        diem += 20
    elif ty_le_tsdb >= 1:
        diem += 10

    tong_lai = so_tien_vay * lai_suat/100 * thoi_gian_vay
    tong_phai_tra = so_tien_vay + tong_lai

    if diem >= 80:
        xep_loai = "🟢 RỦI RO THẤP - ĐỀ XUẤT CHO VAY"
    elif diem >= 60:
        xep_loai = "🟡 CẦN XEM XÉT THÊM"
    else:
        xep_loai = "🔴 RỦI RO CAO"

    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    st.metric("Điểm tín dụng", diem)
    st.metric("Tỷ lệ TSĐB/Khoản vay", f"{ty_le_tsdb:.2f}")
    st.metric("Tổng tiền phải trả", f"{tong_phai_tra:,.0f} VNĐ")

    st.subheader(xep_loai)

    st.markdown("</div>", unsafe_allow_html=True)
