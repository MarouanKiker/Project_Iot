from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
import telebot


@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({'data': data})


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize
    authentication_classes = []
    permission_classes = []

    def perform_create(self, serializer):
        # 1. Enregistrer la mesure en base de données
        data = serializer.save()

        # 2. Vérifier le seuil de température
        temperature = data.temperature
        threshold = getattr(settings, 'TEMP_ALERT_THRESHOLD', 28)

        if temperature > threshold:
            message = (
                f"🚨 ALERTE Cold Chain !\n"
                f"━━━━━━━━━━━━━━━━━━\n"
                f"🌡️ Température : {temperature:.1f} °C\n"
                f"💧 Humidité    : {data.humidity:.1f} %\n"
                f"⚠️ Seuil dépassé : > {threshold} °C\n"
                f"🏢 Labo Ta7alil - Frigo Réactifs"
            )

            # 3. Envoi Email Gmail
            try:
                send_mail(
                    subject="Alerte Temperature",
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.ALERT_EMAIL_RECIPIENT],
                    fail_silently=False
                )
                print(f"[ALERTE GMAIL] Envoyé pour {temperature:.1f} °C")
            except Exception as e:
                print(f"[ERREUR GMAIL] {e}")

            # 4. Envoi Telegram
            try:
                bot = telebot.TeleBot(settings.TELEGRAM_TOKEN)
                bot.send_message(settings.TELEGRAM_CHAT_ID, message)
                print(f"[ALERTE TELEGRAM] Envoyé pour {temperature:.1f} °C")
            except Exception as e:
                print(f"[ERREUR TELEGRAM] {e}")
