# python -m streamlit run C:\Users\lenovo\Desktop\data\python\p14.py
import streamlit as st

if 'pin' not in st.session_state:
    st.session_state.pin = ""
if 'balance' not in st.session_state:
    st.session_state.balance = 0

class ATM:
    def __init__(self):
        self.menu()

    def menu(self):
        st.title("ATM Application")
       
        option = st.radio(
            "Select an option", 
            ('Generate Pin', 'Change Pin', 'Balance Enquiry', 'Withdraw', 'Exit'), 
            key="main_menu"
        )

        if option == 'Generate Pin':
            self.pinGenerate()
        elif option == 'Change Pin':
            self.pinChange()
        elif option == 'Balance Enquiry':
            self.balanceEnquiry()
        elif option == 'Withdraw':
            self.withDrawl()
        elif option == 'Exit':
            self.exit()

    def pinGenerate(self):
        st.subheader("Generate Pin and Set Balance")
        newPin = st.text_input("Enter your new pin:", type="password", key="pin_generate")
        newBalance = st.number_input("Enter your new balance:", min_value=0, key="balance_generate")

        if st.button("Submit", key="submit_generate"):
            st.session_state.pin = newPin
            st.session_state.balance = newBalance
            st.success(f"Pin generated successfully and balance set to {st.session_state.balance}.")

    def pinChange(self):
        st.subheader("Change Pin")
        oldPin = st.text_input("Enter your old pin:", type="password", key="pin_change_old")
        if oldPin == st.session_state.pin:
            newPin2 = st.text_input("Enter your new pin:", type="password", key="pin_change_new")
            if st.button("Submit", key="submit_change"):
                st.session_state.pin = newPin2
                st.success("Pin changed successfully.")
        else:
            st.error("Incorrect old pin, try again!")

    def balanceEnquiry(self):
        st.subheader("Balance Enquiry")
        st.info(f"Your current balance is: {st.session_state.balance}")

    def withDrawl(self):
        st.subheader("Withdraw Money")
        enteredPin = st.text_input("Enter your pin:", type="password", key="pin_withdraw")
        if enteredPin == st.session_state.pin:
            withdrawAmount = st.number_input("Enter the amount to withdraw:", min_value=0, key="amount_withdraw")
            if st.button("Withdraw", key="submit_withdraw"):
                if withdrawAmount > st.session_state.balance:
                    st.error("You don't have enough balance!")
                else:
                    st.session_state.balance -= withdrawAmount
                    st.success(f"Successfully withdrawn {withdrawAmount}. Remaining balance is {st.session_state.balance}.")
        else:
            st.error("Incorrect pin, try again!")

    def exit(self):
        st.subheader("Thank You for Using the ATM")
        st.info("Goodbye!")
        st.stop()

if __name__ == "__main__":
    c1 = ATM()
