import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def create_chart(input_data, chart_type):
    """
    生成统计图表

    Args:
        input_data: 输入数据，字典格式，包含 "columns" 和 "data" 两个键
        chart_type: 图表类型，支持 "bar"（柱状图）和 "line"（折线图）
    """
    df_data = pd.DataFrame(
        data={
            "x": input_data["columns"],
            "y": input_data["data"]
        }
    )
    df_data.set_index("x", inplace=True)

    # 生成动态标题函数
    def generate_chart_title(df_data):
        # 提取最大值和最小值
        max_value = df_data["y"].max()
        min_value = df_data["y"].min()
        total = df_data["y"].sum()

        title_parts = []
        if max_value > 0:
            title_parts.append(f"最大值: {max_value}")
        if min_value > 0:
            if min_value == max_value:
                title_parts.append(f"唯一值: {min_value}")
            else:
                title_parts.append(f"最小值: {min_value}")
        if len(title_parts) > 0:
            return " - ".join(title_parts)
        else:
            return "数据概览"

    # 生成动态标题
    chart_title = generate_chart_title(df_data)

    if chart_type == "bar":
        st.bar_chart(df_data)
        st.title(chart_title)
    elif chart_type == "line":
        plt.plot(df_data.index, df_data["y"], marker="o", linestyle="--")
        plt.ylim(0, df_data["y"].max() * 1.1)
        plt.title(chart_title)
        st.pyplot(plt.gcf())