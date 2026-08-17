import os
import resend

def send_invoice_reminder(client_email, client_name, invoice_amount, days_late):
    # Set up the secure Resend API Key
    resend.api_key = os.environ.get("re_8boj4cak_5ovruVJAmY5XR7wairEq25dx")
    
    subject = f"Urgent: Invoice Reminder for {client_name} ({days_late} Days Overdue)"
    body_content = f"""Hello {client_name},
    
This is a friendly reminder that your recent invoice of ${invoice_amount} is currently {days_late} days overdue.

Please process this payment at your earliest convenience. 

Best regards,
Accounts Team"""
    
    try:
        # Free Resend accounts send from a verified testing domain automatically
        params = {
            "from": "InvoiceBot <onboarding@resend.dev>",
            "to": [client_email],
            "subject": subject,
            "text": body_content,
        }
        
        resend.Emails.send(params)
        return True, "Email sent successfully via Cloud API!"
        
    except Exception as e:
        return False, f"API Error: {e}"
