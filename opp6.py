class Logger:
    def log(self, message):
        print(f"Log: {message}")
    def log_with_timestamp(self, message):
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Log: {message}")### 1. **Using `self`**
#Create a class `Logger` that has an instance method to log messages with a timestamp.
# Create objects
logger1 = Logger()
logger2 = Logger()
# Call methods  
logger1.log("This is a simple log message.")
logger2.log_with_timestamp("This is a log message with a timestamp.")   
logger1.log("Another log message from logger1.")
logger2.log_with_timestamp("Another log message with timestamp from logger2.")
logger1.log("Final log message from logger1.")