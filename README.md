# AI Council — 多角色AI评议系统

一个基于多Agent协作的决策评估框架，模仿"三省六部"式分权审议逻辑，通过角色隔离、交叉辩论和多轮迭代，为人类决策者提供结构化的评议报告。

> **AI负责判断，人类负责决策。**

---

## 核心理念

| 问题 | 解法 |
|------|------|
| 单一AI易产生偏见 | 多角色独立审查，互相隔离 |
| AI容易顺从用户 | 批驳官以"找问题"为唯一职责 |
| 多AI容易虚假共识 | 评议层物理隔离，高度一致时强制追加反向挑战 |
| 决策依据不透明 | 每条结论标注来源角色与置信度 |

---

## 系统流程

```
人类提交议案
     ↓
[准备层] 议案解构官 — 拆解问题、触发专科顾问
     ↓
[评议层] 各角色独立审查（互相隔离）
   ├── 起草官：补全方案
   ├── 批驳官：专职找漏洞
   └── 专科顾问N：领域视角审查
     ↓
[辩论层] 交叉质询（最多3轮）
     ↓
[整合层] 整合官汇总，识别争议与信息缺口
     ↓        ↑
     └─需要补充信息─┘（最多2次回流）
     ↓
[输出层] 结构化评议报告
     ↓
人类决策
```

---

## 目录结构

```
ai-council/
├── README.md
├── docs/
│   ├── architecture.md          # 系统架构说明
│   ├── report-format.md         # 输出报告格式规范
│   └── anti-consensus.md        # 防虚假共识机制说明
├── roles/                       # 各角色定义与Prompt规范
│   ├── README.md
│   ├── 00-decomposer.md         # 准备层：议案解构官
│   ├── 01-drafter.md            # 起草官
│   ├── 02-critic.md             # 批驳官
│   ├── 03-integrator.md         # 整合官
│   └── specialists/             # 专科顾问模板
│       ├── legal.md
│       ├── financial.md
│       ├── technical.md
│       └── ethics.md
├── flows/                       # 流程控制逻辑
│   ├── main-flow.md
│   ├── debate-rules.md
│   └── termination-rules.md
├── config/                      # 配置模板
│   ├── model-config.example.yaml
│   └── council-config.example.yaml
└── tools/
    └── tool-registry.md
```

---

## 快速开始

1. 阅读 `docs/architecture.md` 了解整体设计
2. 查看 `roles/` 了解各角色职责与Prompt规范
3. 根据 `config/council-config.example.yaml` 配置模型
4. 参考 `flows/main-flow.md` 接入调用逻辑

---

## 设计原则

- **单层单职**：每一层只做一件事
- **信息单向流动**：评议层各角色不共享输出，防止锚定效应
- **强制异见**：批驳官找不到问题视为失职
- **人类主权**：系统只输出判断依据，不替人类做决定
