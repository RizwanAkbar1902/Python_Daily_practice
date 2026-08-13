\# Smart Notification Dispatcher (Python OOP) 🔔



A clean, scalable Notification Dispatcher System built in Python demonstrating core \*\*Object-Oriented Programming (OOP)\*\* concepts such as \*\*Abstraction\*\* and \*\*Polymorphism\*\*.



\## 🚀 Key Features



\- \*\*Abstract Base Class (`ABC`)\*\*: Enforces a strict interface (`send` method) for all notification channels.

\- \*\*Polymorphism\*\*: Unified calling mechanism where different notification types (`Email`, `SMS`, `Push`) respond to the same `send()` method differently.

\- \*\*Scalability\*\*: Easy to add new notification channels (e.g., Slack, Discord) without altering the manager logic.



\## 🛠️ Project Structure



\- `main.py`: Contains abstract base class, derived notification classes, and the broadcast manager.

\- `README.md`: Documentation.



\## 💻 How to Run



```bash

python main.py

