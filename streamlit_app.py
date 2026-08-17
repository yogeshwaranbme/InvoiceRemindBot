import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 1. Page Configuration & Styling
st.set_page_config(page_title="Invoice RemindBot", page_icon="🛠️", layout="centered")

st.title("Invoice RemindBot 🛠️")
st.write("Send quick, polite email reminders to clients with past-due invoices.")

# 2. Email Function
def send_invoice_reminder(client_email, client_name, invoice_amount, days_late):
    # Dummy credentials (use Replit Secrets to hide your real ones later!)
    sender_email = "your-business-email@gmail.com"
    sender_password = "your-app-password" 
    
    subject = f"Urgent: Invoice Reminder for {client_name} ({days_late} Days Overdue)"
    body = f"""Hello {client_name},
    
This is a friendly reminder that your recent invoice of ${invoice_amount} is currently {days_late} days overdue.

Please process this payment at your earliest convenience. 

Best regards,
Accounts Team"""
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = client_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))
    
    try:
        server = smtplib.SMTP("://gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, client_email, message.as_string())
        server.quit()
        return True, "Email sent successfully!"
    except Exception as e:
        return False, f"Error: {e}"

# 3. Streamlit Visual UI Inputs
# This creates fields automatically without writing any HTML
with st.form("invoice_form", clear_on_submit=False):
    client_name = st.text_input("Client Name", placeholder="John Doe")
    client_email = st.text_input("Client Email Address", placeholder="john@example.com")
    invoice_amount = st.number_input("Invoice Amount ($)", min_value=0.0, step=10.0, value=450.0)
    days_late = st.number_input("Days Overdue", min_value=1, step=1, value=7)
    
    # The submit button
    submitted = st.form_submit_button("Send Automated Reminder")

# 4. Trigger logic when button is clicked
if submitted:
    if not client_name or not client_email:
        st.error("Please fill out both the Client Name and Email Address.")
    else:
        with st.spinner("Connecting to secure server..."):
            success, feedback_msg = send_invoice_reminder(client_email, client_name, invoice_amount, days_late)
            
            if success:
                st.success(feedback_msg)
            else:
                # Shows error if your email/password isn't valid yet
                st.error(feedback_msg)
