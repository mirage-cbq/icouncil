# 贡献指南

## 可以贡献的内容

- **新的专科顾问模板**：在 `roles/specialists/` 下新增领域顾问
- **流程规则改进**：对 `flows/` 下的规则提出修改建议
- **防共识机制**：完善 `docs/anti-consensus.md` 中的机制设计
- **工具定义**：在 `tools/tool-registry.md` 中新增工具

## 贡献规范

### 新增专科顾问
复制现有模板（如 `roles/specialists/legal.md`），包含：
- 触发条件（何时自动加载）
- 审查范围（只审查什么）
- 可调用工具列表
- System Prompt 模板

### 修改流程规则
在 PR 中说明：
- 修改解决了什么问题
- 是否经过实际测试
- 对其他流程环节的影响

## Issue 类型

- `design` — 制度设计讨论
- `prompt` — Prompt 优化建议
- `tool` — 新工具接入
- `bug` — 流程逻辑错误
