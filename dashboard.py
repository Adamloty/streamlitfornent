import streamlit as st  
from PIL import Image  
from pathlib import Path
from streamlit_option_menu import option_menu  
import os
import webbrowser
import streamlit.components.v1 as components

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def display_home():
    THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    ASSETS_DIR = THIS_DIR / "assets"
    STYLES_DIR = THIS_DIR / "styles"
    CSS_FILE = STYLES_DIR / "main.css"

    STRIPE_CHECKOUT = "http://192.168.1.6:8501"
    CONTACT_EMAIL = "adamlotfy011@gmail.com"
    PRODUCT_NAME = "Chatxt AI "
    PRODUCT_TAGLINE = "Welcome to Chatxt AI!"
    PRODUCT_DESCRIPTION = """
We offer a variety of tools and services in the field of artificial intelligence to meet your needs. 
Whether you're a developer, a student, a curious mind, or just someone interested in the possibilities that AI offers, you've come to the right website.
    """

    load_css_file(CSS_FILE)
    st.header(PRODUCT_NAME)
    st.subheader(PRODUCT_TAGLINE)
    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.text("")
        st.write(PRODUCT_DESCRIPTION)
    with right_col:
        product_image = Image.open(ASSETS_DIR / "product.png")
        st.image(product_image, width=450)

    st.write("")
    st.write("---")
    st.subheader(":rocket: Features")

    features = {
        "Feature_1.png": [
            "Chat with website",
        ],
        "Feature_2.png": [
            "Chat with CSV",
        ],

        "Feature_3.png": [
            "Chat with Pdf",
        ],
    }
    for image, description in features.items():
      image = Image.open(ASSETS_DIR / image)
      st.write("")
      left_col, right_col = st.columns(2)
      left_col.image(image, use_column_width=True)
      right_col.write(f"**{description[0]}**")
      if len(description) > 1:
        right_col.write(description[1])

    st.write("")
    st.write("---")
    st.subheader(":raising_hand: الأسئلة الشائعة")
    faq = {
        "هل ستكون هناك تحديثات؟ ": "نعم، ستكون هناك تحديثات مستمرة",
    }
    for question, answer in faq.items():
        with st.expander(question):
            st.write(answer)

    st.write("")
    st.write("---")
    st.subheader(":mailbox: هل لديك سؤال؟ اسأل الآن!")
    contact_form = f"""
    <form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="اسمك" required>
         <input type="email" name="email" placeholder="بريدك الإلكتروني" required>
         <textarea name="message" placeholder="رسالتك هنا"></textarea>
         <button type="submit" class="button">إرسال ✉</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

def display_yearly_pricing():
    load_css_file("styles/subscription.css")
    subscription_form = """
        <div class="card">
            <div class="content">
                <div class="title">Yearly</div>
                <div class="price">$40.00</div>
                <div class="description">-All Features</div>
                <div class="description">-Seven days free</div>
            </div>
        </div>
    </div>
    """

    st.markdown(subscription_form, unsafe_allow_html=True)

    google_pay_button_yearly = """
<!DOCTYPE html>
<html>
  <head>
    <title>Google Pay Demo</title>
    <script async
      src="https://pay.google.com/gp/p/js/pay.js"
      onload="onGooglePayLoaded()"></script>
    <script>
      let paymentsClient;

      function onGooglePayLoaded() {
        paymentsClient = new google.payments.api.PaymentsClient({ environment: 'TEST' });
        const button = paymentsClient.createButton({
          onClick: onGooglePayButtonClicked,
        });
        document.getElementById('container').appendChild(button);
      }

      function onGooglePayButtonClicked() {
        const paymentDataRequest = getGooglePaymentDataRequest();
        paymentsClient.loadPaymentData(paymentDataRequest).then(function(paymentData) {
          processPayment(paymentData);
        }).catch(function(err) {
          console.error(err);
        });
      }

      function getGooglePaymentDataRequest() {
        return {
          apiVersion: 2,
          apiVersionMinor: 0,
          allowedPaymentMethods: [{
            type: 'CARD',
            parameters: {
              allowedAuthMethods: ['PAN_ONLY', 'CRYPTOGRAM_3DS'],
              allowedCardNetworks: ['MASTERCARD', 'VISA']
            },
            tokenizationSpecification: {
              type: 'PAYMENT_GATEWAY',
              parameters: {
                gateway: 'example', // استبدل 'example' ببوابة الدفع الخاصة بك
                gatewayMerchantId: 'exampleMerchantId' // استبدل 'exampleMerchantId' بمعرف التاجر الخاص بك
              }
            }
          }],
          merchantInfo: {
            merchantId: 'YOUR_MERCHANT_ID', // استبدل 'YOUR_MERCHANT_ID' بمعرف التاجر الخاص بك
            merchantName: 'Example Merchant' // استبدل 'Example Merchant' باسم متجرك
          },
          transactionInfo: {
            totalPriceStatus: 'FINAL',
            totalPrice: '40.00', // اشتراك شهري مجاني
            currencyCode: 'USD'
          },
          recurringPayment: {
            type: 'YEARLY', // اشتراك شهري
            billingPeriod: 'YEAR',
            trialPeriod: 'THREE_DAYS' // فترة تجريبية مجانية لثلاثة أيام
          }
        };
      }

      function processPayment(paymentData) {
        // التعامل مع الرد من جوجل بي هنا
        console.log('تم الدفع بنجاح', paymentData);
        // توجيه المستخدم إلى موقع الويب بعد الدفع الناجح
        window.location.href = 'https://your-website.com';
      }
    </script>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
    """

    components.html(google_pay_button_yearly, height=50)

def display_monthly_pricing():
    load_css_file("styles/subscription.css")
    subscription_form_monthly = """
        <div class="card">
            <div class="content">
                <div class="title">Monthly</div>
                <div class="price">$5.00</div>
                <div class="description">-All Features</div>
                <div class="description">-Seven days free</div>
            </div>
        </div>
    </div>
    """

    st.markdown(subscription_form_monthly, unsafe_allow_html=True)

    google_pay_button_monthly = """
<!DOCTYPE html>
<html>
  <head>
    <title>Google Pay Demo</title>
    <script async
      src="https://pay.google.com/gp/p/js/pay.js"
      onload="onGooglePayLoaded()"></script>
    <script>
      let paymentsClient;

      function onGooglePayLoaded() {
        paymentsClient = new google.payments.api.PaymentsClient({ environment: 'TEST' });
        const button = paymentsClient.createButton({
          onClick: onGooglePayButtonClicked,
        });
        document.getElementById('container').appendChild(button);
      }

      function onGooglePayButtonClicked() {
        const paymentDataRequest = getGooglePaymentDataRequest();
        paymentsClient.loadPaymentData(paymentDataRequest).then(function(paymentData) {
          processPayment(paymentData);
        }).catch(function(err) {
          console.error(err);
        });
      }

      function getGooglePaymentDataRequest() {
        return {
          apiVersion: 2,
          apiVersionMinor: 0,
          allowedPaymentMethods: [{
            type: 'CARD',
            parameters: {
              allowedAuthMethods: ['PAN_ONLY', 'CRYPTOGRAM_3DS'],
              allowedCardNetworks: ['MASTERCARD', 'VISA']
            },
            tokenizationSpecification: {
              type: 'PAYMENT_GATEWAY',
              parameters: {
                gateway: 'example', // استبدل 'example' ببوابة الدفع الخاصة بك
                gatewayMerchantId: 'exampleMerchantId' // استبدل 'exampleMerchantId' بمعرف التاجر الخاص بك
              }
            }
          }],
          merchantInfo: {
            merchantId: 'YOUR_MERCHANT_ID', // استبدل 'YOUR_MERCHANT_ID' بمعرف التاجر الخاص بك
            merchantName: 'Example Merchant' // استبدل 'Example Merchant' باسم متجرك
          },
          transactionInfo: {
            totalPriceStatus: 'FINAL',
            totalPrice: '5.00', // اشتراك شهري مجاني
            currencyCode: 'USD'
          },
          recurringPayment: {
            type: 'MONTHLY', // اشتراك شهري
            billingPeriod: 'MONTH',
            trialPeriod: 'THREE_DAYS' // فترة تجريبية مجانية لثلاثة أيام
          }
        };
      }

      function processPayment(paymentData) {
        // التعامل مع الرد من جوجل بي هنا
        console.log('تم الدفع بنجاح', paymentData);
        // توجيه المستخدم إلى موقع الويب بعد الدفع الناجح
        window.location.href = 'https://your-website.com';
      }
    </script>
  </head>
  <body>
    <div id="container"></div>
  </body>
</html>
    """

    components.html(google_pay_button_monthly, height=50)

selected = option_menu(
    menu_title=None, 
    options=["Home",  "Pricing monthly" ,"Pricing yearly" ], 
    icons=["house", "cart" , "cart"],  
    default_index=0,  
    orientation="horizontal",
)

if selected == "Home":
    display_home()
elif selected == "Pricing yearly":
    display_yearly_pricing()
elif selected == "Pricing monthly":
    display_monthly_pricing()
     





















     