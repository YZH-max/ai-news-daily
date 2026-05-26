# 🤖 AI News Daily

自动抓取AI领域每日最新资讯，通过GitHub Actions定时运行。

## 📋 功能

- 每日北京时间 9:00 自动运行
- 抓取多个AI新闻源（Hacker News、VentureBeat、TechCrunch等）
- 支持推送到飞书/钉钉/企业微信 Webhook

## 🚀 使用步骤

### 1. 创建 GitHub 仓库

```bash
# 在 GitHub 创建新仓库，例如：ai-news-daily
# 将此目录内容推送上去
```

### 2. 推送代码

```bash
cd ai-news-daily
git init
git add .
git commit -m "Initial commit: AI news daily fetcher"
git branch -M main
git remote add origin git@github.com:你的用户名/ai-news-daily.git
git push -u origin main
```

### 3. 启用 GitHub Actions

- 打开仓库 → Settings → Actions → General
- 确保 "Allow all actions and reusable workflows" 已启用
- Actions 会在每天北京时间 9:00 自动运行

### 4. （可选）配置 Webhook 推送

如果想把新闻推送到飞书/钉钉/企业微信：

1. 在对应平台创建 Webhook 机器人
2. 在仓库 Settings → Secrets → Actions 中添加：
   - `WEBHOOK_URL`: 你的 Webhook 地址

### 5. 手动触发

随时可以在仓库的 Actions 页面点击 "Run workflow" 手动运行

## 📡 新闻源

| 来源 | 内容 |
|------|------|
| Hacker News AI | AI/ML相关讨论 |
| Hacker News LLM | LLM/GPT/Transformer相关 |
| VentureBeat AI | VentureBeat AI频道 |
| TechCrunch AI | TechCrunch AI频道 |
| Ars Technica AI | Ars Technica AI标签 |

## 🔧 自定义

- 修改 `fetch_news.py` 中的 `FEEDS` 字典可添加/删除新闻源
- 修改 `.github/workflows/ai-news.yml` 中的 `cron` 表达式可调整运行时间
- Cron时区为UTC，北京时间9点 = UTC 1点

## 📄 输出

- `news.json`: JSON格式的新闻数据
- 控制台: 格式化的新闻摘要

---

由小白 🐾 为大白准备
