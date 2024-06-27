import uasyncio as asyncio
import socket
import struct

class DNSServer:
    def __init__(self, records):
        self.dns_records = records
        self.sock = None
        self.running = False

    def build_response(self, data):
            transaction_id = data[:2]  # 事务ID
            flags = b'\x85\x80'  # 标志位，表示标准查询响应，无错误，权威应答
            questions = struct.unpack('>H', data[4:6])[0]  # 问题数
            answer_rrs = struct.pack('>H', questions)  # 回答数，与问题数相同
            authority_rrs = b'\x00\x00'  # 权威记录数
            additional_rrs = b'\x00\x00'  # 附加记录数

            dns_header = transaction_id + flags + data[4:6] + answer_rrs + authority_rrs + additional_rrs

            offset = 12
            answers = b''

            for _ in range(questions):
                query_name_end = data[offset:].find(b'\x00') + 1
                query = data[offset:offset + query_name_end + 4]
                qtype = data[offset + query_name_end:offset + query_name_end + 2]
                qclass = data[offset + query_name_end + 2:offset + query_name_end + 4]

                query_name = data[offset:offset + query_name_end - 1]
                query_name_parts = []
                while query_name:
                    length = query_name[0]
                    query_name_parts.append(query_name[1:length + 1].decode())
                    query_name = query_name[length + 1:]
                query_name_str = '.'.join(query_name_parts)


                if qclass == b'\x00\x01' and qtype == b'\x00\x01':  # A记录
                    if query_name_str in self.dns_records and "A" in self.dns_records[query_name_str]:
                        response_ip = self.dns_records[query_name_str]["A"]
                        answer_name = b'\xc0\x0c'  # 指向问题部分的指针
                        answer_type = qtype
                        answer_class = qclass
                        ttl = b'\x00\x00\x00\x3c'  # 生存时间
                        rdlength = b'\x00\x04'  # 数据长度
                        rdata = bytes(map(int, response_ip.split('.')))
                        dns_answer = answer_name + answer_type + answer_class + ttl + rdlength + rdata
                        answers += dns_answer

                elif qclass == b'\x00\x01' and qtype == b'\x00\x05':  # CNAME记录
                    if query_name_str in self.dns_records and "CNAME" in self.dns_records[query_name_str]:
                        cname = self.dns_records[query_name_str]["CNAME"]
                        cname_parts = cname.split('.')
                        answer_name = b'\xc0\x0c'  # 指向问题部分的指针
                        answer_type = qtype
                        answer_class = qclass
                        ttl = b'\x00\x00\x00\x3c'  # 生存时间
                        rdlength = struct.pack('>H', sum(len(part) + 1 for part in cname_parts) + 1)
                        rdata = b''.join(len(part).to_bytes(1, 'big') + part.encode() for part in cname_parts) + b'\x00'
                        dns_answer = answer_name + answer_type + answer_class + ttl + rdlength + rdata
                        answers += dns_answer

                offset += query_name_end + 4

            response = dns_header + data[12:offset] + answers
            return response

    async def handle_dns_request(self):
        while self.running:
            try:
                data, addr = self.sock.recvfrom(512)
                response = self.build_response(data)
                writeBytes=self.sock.sendto(response, addr)
            except Exception as e:
                print(f"Error handling DNS request: {e}")
            await asyncio.sleep_ms(100)  # 确保事件循环继续运行

    async def run(self, host='0.0.0.0', port=53):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((host, port))
        self.running = True
        print(f"DNS server started on {host}:{port}")

        await self.handle_dns_request()

    async def shutdown(self):
        if self.sock:
            self.running = False
            self.sock.close()
            print("DNS server shut down successfully")
