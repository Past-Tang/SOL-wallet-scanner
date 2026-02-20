<div align="center">

<img src="assets/logo.svg" alt="SOL Wallet Scanner" width="600">

<br/>
<br/>

**Solana 钱包扫描工具**

*随机密钥生成 | 余额查询 | 邮件通知*

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)]()
[![Status](https://img.shields.io/badge/Status-Archived-lightgrey.svg)]()

</div>

---

> **此仓库已归档，不再维护。** 仅作为 Solana 区块链交互的学习参考。

## 概述

随机生成 Solana 钱包密钥对并查询余额的扫描工具。当发现有余额的钱包时，通过 SMTP 邮件通知用户。纯概率实验性质，找到有余额钱包的可能性极低。

### 工作流程

```
随机生成 Solana 密钥对 (Solders)
        |
        v
  Base58 编码公钥 --> 查询 Solana RPC 余额
        |
        v
  余额 > 0 ?  --是-->  SMTP 邮件通知
        |
       否
        |
        v
  记录日志，每 100 次输出进度 --> 继续循环
```

---

## 技术栈

| 组件 | 用途 |
|:---|:---|
| Solders | Solana 密钥对生成与区块链交互 |
| Base58 | 公钥编码/解码 |
| Requests | Solana RPC HTTP 请求 |
| SMTP | 邮件通知 |

---

## 使用方法

### 安装

```bash
git clone https://github.com/Past-Tang/SOL-wallet-scanner.git
cd SOL-wallet-scanner
pip install solders base58 requests
```

### 配置

编辑 `solana.py`，配置邮件服务：

```python
self.smtp_server = "smtp.qq.com"
self.smtp_port = 465
self.username = ""    # 发件邮箱
self.password = ""    # 邮箱授权码
```

### 运行

```bash
python solana.py
```

---

## 免责声明

本项目仅供技术学习和研究目的。随机碰撞私钥在数学上几乎不可能成功。