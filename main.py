import streamlit as st
import pytz 
import datetime as dt
import locale

st.title("What day is it today ?")

# 指定する日付の範囲を設定
min_date = dt.date(1900, 1, 1)
max_date = dt.date(2100, 12, 31)
ivent_day = st.date_input("あの出来事はいつのこと？", min_value=min_date, max_value=max_date)

# タイムゾーンと曜日を日本で設定、取得
tz_japan = pytz.timezone("Asia/Tokyo")
weekday_list = ["月", "火", "水", "木", "金", "土", "金"]
now = dt.datetime.now(tz_japan).date()
wd = weekday_list[ivent_day.weekday()]

# 今日との差分の符号で過去と未来それぞれの結果を出力
div = (now - ivent_day).days
if div >= 0:
    st.markdown(f"あれから{div}日が経ちました。")
    st.markdown(f"その出来事は{wd}曜日のことでした。")
else:
    st.markdown(f"あと{-div}日です。")
    st.markdown(f"その出来事は{wd}曜日にあります。")

