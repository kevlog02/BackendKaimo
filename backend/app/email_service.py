import emails
from emails.template import JinjaTemplate
from .config import settings

def send_email(email_to: str, subject: str, html_content: str):
    message = emails.Message(
        subject=subject,
        html=html_content,
        mail_from=(settings.EMAILS_FROM_NAME, settings.EMAILS_FROM_EMAIL)
    )
    
    smtp_options = {
        "host": settings.SMTP_HOST,
        "port": settings.SMTP_PORT,
        "tls": True,
        "user": settings.SMTP_USER,
        "password": settings.SMTP_PASSWORD
    }

    
    response = message.send(to=email_to, smtp=smtp_options)
    return response

def send_verification_email(email_to: str, username: str, token: str):
    verification_url = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    
    html_content = f"""
    <html>
    <body style="margin:0; padding:0; background:#f4f4f4; font-family: Arial, sans-serif;">
        <table width="100%" cellpadding="0" cellspacing="0" style="background:#f4f4f4; padding:40px 0;">
        <tr>
            <td align="center">
            <table width="600" cellpadding="0" cellspacing="0" 
                    style="background:white; border-radius:12px; padding:40px; box-shadow:0 4px 12px rgba(0,0,0,0.1);">
                
                <tr>
                <td align="center">
                    <h1 style="color:#0077cc; margin-bottom:20px; font-size:28px;">
                        Bienvenido a Kaimo
                    </h1>
                </td>
                </tr>

                <tr>
                <td style="font-size:16px; color:#444;">
                    <p>Hola <strong>{username}</strong>,</p>
                    <p>
                    Gracias por crear una cuenta en <strong>Kaimo</strong>. Para continuar,
                    por favor confirma tu correo haciendo clic en el siguiente botón:
                    </p>
                </td>
                </tr>

                <tr>
                <td align="center" style="padding:30px 0;">
                    <a href="{verification_url}"
                    style="background:#0077cc; color:white; padding:14px 32px; 
                            font-size:16px; text-decoration:none; border-radius:8px;">
                    Verificar correo
                    </a>
                </td>
                </tr>

                <tr>
                <td style="font-size:14px; color:#777; padding-top:20px;">
                    <p>Si tú no solicitaste esta cuenta, simplemente ignora este mensaje.</p>
                </td>
                </tr>
            </table>
            </td>
        </tr>
        </table>
    </body>
    </html>
    """

    
    send_email(
        email_to=email_to,
        subject="Verifica tu correo electrónico",
        html_content=html_content
    )