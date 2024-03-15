import numpy as np
import streamlit as st

import streamlit_nested_layout

outer_cols = st.columns([1, 1])

with outer_cols[0]:
    st.markdown('## Column 1')
    st.selectbox('selectbox', [1,2,3], key='sel1')
    
    inner_cols = st.columns([1, 1])
    with inner_cols[0]:
        st.markdown('Nested Column 1')
        st.selectbox('selectbox', [1,2,3], key='sel2')
    with inner_cols[1]:
        st.markdown('Nested Column 2')
        st.selectbox('selectbox', [1,2,3], key='sel3')
    
    with st.container(border=True):
        with st.chat_message('User1'):
            st.write("Hello (user1) 👋")
            st.line_chart(np.random.randn(30, 3), height=200)
            with st.container(border=True):
                with st.chat_message('User2'):
                    st.write("Hello (user2) 👋")
                    st.line_chart(np.random.randn(30, 3), height=200)

with outer_cols[1]:
    st.markdown('## Column 2')
    with st.expander('Expander 1', expanded=True):
        st.markdown('Some Stuff Here')
        with st.expander('Nested Expander 1', expanded=True):
            st.markdown('Some More Stuff Here')
            
            inner_cols = st.columns([1, 1])
            with inner_cols[0]:
                st.markdown('Nested Column 1')
                st.selectbox('selectbox', [1,2,3], key='sel4')
            with inner_cols[1]:
                st.markdown('Nested Column 2')
                st.selectbox('selectbox', [1,2,3], key='sel5')
        with st.expander('Nested Expander 2'):
            st.markdown('Some More Stuff Here')
    
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")
        name = st.text_input("What's your name?")
        st.write('Some')
        st.write('Text')
        st.write('Here')
        st.write('Some')
        st.write('Text')
        st.write('Here')
        with st.popover("Open nested popover"):
            st.markdown("Hello World again 👋")
            name = st.text_input("What's your name again?")
