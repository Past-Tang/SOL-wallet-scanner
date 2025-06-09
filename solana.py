import logging,time
from solders.keypair import Keypair
import base58  # 需要安装 base58 库
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import requests

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class EmailSender:
    def __init__(self):
        """
        初始化邮件发送器
        :param smtp_server: SMTP服务器地址
        :param smtp_port: SMTP端口
        :param username: 发件邮箱
        :param password: 邮箱密码/授权码
        """
        self.smtp_server = "smtp.qq.com"
        self.smtp_port = 465
        self.username = ""
        self.password = ""

    def send_email(self, to_addr: str, subject: str, content: str):
        """
        发送邮件
        :param to_addr: 收件人邮箱
        :param subject: 邮件主题
        :param content: 邮件内容
        :return: 发送成功返回True，失败返回False
        """
        try:
            # 创建邮件对象
            msg = MIMEText(content, 'plain', 'utf-8')
            msg['From'] = Header(self.username)
            msg['To'] = Header(to_addr)
            msg['Subject'] = Header(subject)

            # 连接SMTP服务器
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
                server.login(self.username, self.password)
                server.sendmail(self.username, [to_addr], msg.as_string())
            return True
        except Exception as e:
            if "-1" in str(e):
                 return True
            else:
                print(f"邮件发送失败: {str(e)}")
            return False    


def get_transaction_details(public_key):
    payload = {"jsonrpc":"2.0","id":"1","method":"getBalance","params":[public_key]}
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "content-type": "application/json",
        "origin": "https://app.meteora.ag",
        "priority": "u=1, i",
        "referer": "https://app.meteora.ag/",
        "solana-client": "js/0.0.0-development",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive"
    }
    try:
        response = requests.post(
            'https://mercuria-fronten-1cd8.mainnet.rpcpool.com/',
            json=payload,
            timeout=5,
            headers=headers,
        )
        if response.status_code == 200:
            data = response.json()
            return data
        return None

    except requests.exceptions.RequestException as e:
        print(f"网络请求异常: {str(e)}")
        return None
    except (KeyError, IndexError) as e:
        print(f"数据解析异常: {str(e)}")
        return None
    except Exception as e:
        print(f"未知异常: {str(e)}")
        return None
def find_keypair_with_prefix():
    keypair = Keypair()
    public_key = str(keypair.pubkey())
    private_key_bytes = bytes(keypair)
    private_key_base58 = base58.b58encode(private_key_bytes).decode('utf-8')

    data = get_transaction_details(public_key)
    if data is not None and 'result' in data and 'value' in data['result']:
        lamports = data['result']['value']
        if lamports > 0:
            sol_balance = lamports / 1_000_000_000
            return [public_key, private_key_base58, f'{sol_balance:.9f}']
        else:
            return None
if __name__ == "__main__":
    sender = EmailSender()
    total_attempts = 0
    success_count = 0
    
    logger.info("程序启动")
    while True:
        time.sleep(2)
        total_attempts += 1
        outup = find_keypair_with_prefix()
        
        if outup != None:
            success_count += 1
            logger.info(f"找到账户，公钥: {outup[0]}, 私钥={str(outup[1])},余额: {outup[2]} SOL")
            msg=str(f"找到账户，公钥: {outup[0]}, 私钥={str(outup[1])},余额: {outup[2]} SOL")
            if sender.send_email(
                    to_addr="2056606309@qq.com",  # 替换为收件邮箱
                    subject="获得彩票提醒",
                    content=msg):
                logger.info("邮件发送成功")
            else:
                logger.warning("邮件发送失败")
        
        if total_attempts % 100 == 0:
            logger.info(f"进度报告 - 总尝试次数: {total_attempts}, 成功次数: {success_count}")
