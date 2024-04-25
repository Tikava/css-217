# Model

Basic model is - Support tiket. It has following fields:

```python
class SupportTicket:
    def __init__(self, id, description, type, priority):
        self.id = id
        self.description = description
        self.type = type
        self.priority = priority
```

# Handlers

There are three types of handelers: 
- HardwareSupportHandler
- SoftwareSupportHandler
- NetworkSupportHandler

They all have `handle_request` and `next_hander`, which are inherited from the base class `Handler`.

# Add

I use COR pattern to handle tickets step by step.
You can look at `main.py` to see the implementation.