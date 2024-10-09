from mitmproxy import dns

class CustomDNSResolver:
    def __init__(self):
        self.host_mappings = {
            "www.example1.com": "127.0.0.2",
            "www.example2.com": "127.0.0.3"
        }
       
    def dns_request(self, flow: dns.DNSFlow):
        for question in flow.request.questions:
            query_name = question.name
            if query_name in self.host_mappings:
                response_ip = self.host_mappings[query_name]

                # Split the IP address into a byte array
                ip_bytes = bytes(map(int, response_ip.split(".")))
                flow.response.response_code = 0
                flow.response.answers.append(dns.ResourceRecord(
                    name=question.name,
                    type=question.type,
                    class_ = question.class_,
                    ttl=3600,
                    data=ip_bytes
                ))

addons = [
    CustomDNSResolver()
]