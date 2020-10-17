import streamlit as st


def main():

	st.title('Intelligent Height Measure')
	st.text('This tool uses advanced technology to measure your height based on a few simple questions')
	st.text_input('What is your zip code', value='90210')
	height = st.text_input('How tall are you in inches?', value='60')
	

	if st.button('Measure Me'):
		st.text('You are '+ height + ' inches tall')
		st.text('Not satisfied with your result?')
		st.text('Please make sure the information you provided is accurate, and try again!')


if __name__ == '__main__':
    main()