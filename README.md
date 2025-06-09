# Sol-Wallet-Scanner

[![许可证](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> **注意**: 此仓库已不再维护。

## 项目概述

Sol-Wallet-Scanner 是一个用于扫描 Solana 区块链上的钱包地址的工具。它能够随机生成 Solana 钱包密钥对，并检查这些钱包中是否存在余额。当发现有余额的钱包时，程序会通过邮件通知用户。

## 特点

- 随机生成 Solana 钱包密钥对
- 自动查询生成钱包的余额
- 通过邮件通知发现有余额的钱包
- 日志记录功能，便于追踪程序运行状态
- 定期进度报告

## 技术栈

- Python 3.7+
- Solders (Solana 区块链交互库)
- Base58 (用于编码/解码)
- Requests (HTTP 请求)
- SMTP 邮件服务

## 安装说明

1. 克隆仓库
```bash
git clone https://github.com/yourusername/sol-wallet-scanner.git
cd sol-wallet-scanner
```

2. 安装依赖
```bash
pip install solders base58 requests
```

## 配置

使用前需要配置邮件发送服务，在 `solana.py` 文件中修改以下内容：

```python
self.smtp_server = "smtp.qq.com"  # SMTP服务器地址
self.smtp_port = 465              # SMTP端口
self.username = ""                # 发件邮箱地址
self.password = ""                # 邮箱授权码
```

同时，在主函数中修改收件邮箱地址：

```python
to_addr="your-email@example.com"  # 替换为收件邮箱
```

## 使用方法

运行以下命令启动扫描程序：

```bash
python solana.py
```

程序将持续运行并:
1. 生成随机 Solana 钱包密钥对
2. 检查钱包余额
3. 当发现有余额的钱包时，发送邮件通知
4. 每 100 次尝试输出一次进度报告

## 依赖项列表

- solders: Solana 区块链交互库
- base58: 用于编码/解码 Base58 格式的数据
- requests: HTTP 请求库
- 标准库: logging, time, smtplib, email

## 常见问题(FAQ)

### Q: 程序需要持续运行多久才能找到有余额的钱包?
A: 由于随机生成钱包的特性，找到有余额的钱包是极其罕见的事件，程序可能需要运行很长时间。

### Q: 如何停止程序?
A: 在终端中按 Ctrl+C 可以中断程序运行。

### Q: 为什么需要配置邮箱?
A: 当程序发现有余额的钱包时，会通过邮件通知您，这样您无需一直盯着终端输出。

## 项目维护者

此项目已不再维护。

## 许可证

MIT 许可证 