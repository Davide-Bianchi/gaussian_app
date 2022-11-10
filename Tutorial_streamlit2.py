import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
st.title("Let's make a Gaussian!")
st.latex(r"\mathcal{N}(\mu, \sigma) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp{-\frac{(x-\mu)^2}{2\sigma^2}}")
st.markdown("""By changing the sliders you can :
- Change $\mu$
- Change $\sigma$
- Change color
""")
with st.sidebar.form("my_form"):
   mu = st.slider('Select mean of Gaussian: ', -20., 20., 0., step = 0.01)
   sigma = st.number_input(r'Pick a value for $\sigma$', 0.01,10.)
   color = st.color_picker('Choose graph color')
   lock_axes = st.checkbox('Lock axes')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write(r'$\mu$: ', mu, r'$\sigma$:', sigma)


rand=np.random.normal(mu, sigma, size=10000000)
fig, ax = plt.subplots()
ax.hist(rand, bins=np.arange(mu - 5*sigma, mu + 5*sigma, 0.01*sigma), color=color, density=True)
if lock_axes:
    plt.ylim(0, 1)
    plt.xlim(-20,20)
st.pyplot(fig)
