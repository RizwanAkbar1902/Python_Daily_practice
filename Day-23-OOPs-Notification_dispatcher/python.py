from abc import ABC, abstractmethod

# 1. ABSTRACT BASE CLASS (Abstraction)
class BaseNotification(ABC):
    def __init__(self, recipient: str):
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str):
        """Every child class MUST implement this method"""
        pass


# 2. CHILD CLASSES (Polymorphism & Method Overriding)
class EmailNotification(BaseNotification):
    def send(self, message: str):
        print(f"[EMAIL SENT] To: {self.recipient} | Content: '{message}'")


class SMSNotification(BaseNotification):
    def send(self, message: str):
        print(f"[SMS SENT] To: {self.recipient} | Content: '{message}'")


class PushNotification(BaseNotification):
    def send(self, message: str):
        print(f"[PUSH ALERT] User: {self.recipient} | Message: '{message}'")


# 3. MANAGER CLASS (Handling Multiple Notification Types)
class NotificationManager:
    def __init__(self):
        self.channels = []  # List of notification objects

    def add_channel(self, channel: BaseNotification):
        self.channels.append(channel)

    def broadcast(self, alert_message: str):
        """Sends message across all channels simultaneously (Polymorphism)"""
        print(f"\n--- BROADCASTING ALERT: '{alert_message}' ---")
        for channel in self.channels:
            channel.send(alert_message)  # Same method call, different behaviors!


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Create Manager instance
    manager = NotificationManager()

    # Create Notification Channels
    email = EmailNotification("user@example.com")
    sms = SMSNotification("+1234567890")
    push = PushNotification("Device_Token_9981")

    # Add Channels to Manager
    manager.add_channel(email)
    manager.add_channel(sms)
    manager.add_channel(push)

    # Broadcast Security Alert
    manager.broadcast("Security Notice: Unexpected Login Detected!")