from enums import SupportType

class SupportHandler:
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler

    def handle_request(self, ticket):
        pass
    
class HardwareSupportHandler(SupportHandler):
    def handle_request(self, ticket):
        if ticket.type == SupportType.HARDWARE:
            print(f"Hardware support team is handling ticket {ticket.id}")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)
            
class SoftwareSupportHandler(SupportHandler):
    def handle_request(self, ticket):
        if ticket.type == SupportType.SOFTWARE:
            print(f"Software support team is handling ticket {ticket.id}")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)

class NetworkSupportHandler(SupportHandler):
    def handle_request(self, ticket):
        if ticket.type == SupportType.NETWORK:
            print(f"Network support team is handling ticket {ticket.id}")
        elif self.next_handler:
            self.next_handler.handle_request(ticket)