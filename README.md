# 贵金属实时价格 - Android APK 应用

## 📱 应用功能特性

### 核心功能
- **实时价格显示**：展示四项贵金属价格数据
  - Au99.99（国内黄金）
  - Ag(T+D)（国内白银）
  - XAU/USD（国际黄金）
  - XAG/USD（国际白银）

- **UI设计**
  - 深色背景 (#1a1a2e)
  - 金色/白色文字配色
  - 半透明悬浮窗风格
  - 圆角矩形窗口

- **交互功能**
  - ✅ 拖拽移动：触摸标题栏可自由拖动位置
  - ✅ 边缘吸附：松手时自动吸附到屏幕边缘（阈值20px）
  - ✅ 边界限制：无法拖出屏幕范围
  - ✅ 隐藏/恢复：点击最小化按钮收缩为小标签，双击恢复
  - ✅ 定时刷新：国内价格30秒、国际价格1秒自动更新

### 技术架构
- **框架**：Python 3.11 + Kivy 2.3.1
- **网络请求**：urllib + ssl（无需额外依赖）
- **多线程**：异步刷新避免UI卡顿
- **目标平台**：Android 5.0+ (API 21+)

---

## 📦 文件结构

```
precious-metal-price/
├── main.py              # 主程序入口
├── buildozer.spec       # Buildozer打包配置
├── README.md            # 本说明文档
└── build_apk.sh         # Linux打包脚本
```

---

## 🔧 环境要求

### 开发环境（测试运行）
```bash
# 安装依赖
pip install kivy requests

# 运行桌面版（测试用）
python main.py
```

### 打包环境（生成APK）
需要以下任一环境：

#### 方案A：Linux原生环境（推荐Ubuntu 22.04）
```bash
# 安装系统依赖
sudo apt update
sudo apt install -y build-essential git zlib1g-dev \
    python3-pip openjdk-17-jdk android-sdk \
    libncurses5-dev libncursesw5-dev \
    libstdc++6 autoconf libtool libffi-dev

# 安装Buildozer
pip3 install buildozer cython

# 初始化（首次）
buildozer init

# 打包Debug版本
buildozer android debug

# 打包Release版本（需签名）
buildozer android release
```

#### 方案B：Windows WSL2
```bash
# 在WSL2 Ubuntu中执行上述Linux命令
```

#### 方案C：Docker容器
```bash
docker run --rm -v $(pwd):/home/user/app \
    -w /home/user/app \
    kivy/buildozer:latest \
    android debug
```

#### 方案D：GitHub Actions（自动化）
见 `.github/workflows/build-apk.yml` 配置文件

---

## 🚀 快速开始

### 1. 测试运行（桌面版）

在Windows/Linux/macOS上直接运行查看效果：

```bash
cd precious-metal-price
python main.py
```

预期效果：
- 显示深色悬浮窗
- 展示4项价格数据（初始为模拟数据）
- 可拖拽、可最小化
- 自动定时刷新

### 2. 打包为APK

#### 步骤1：准备环境
确保已安装：
- Python 3.8+
- Buildozer
- Android SDK/NDK（Buildozer会自动下载）

#### 步骤2：修改配置（可选）
编辑 `buildozer.spec` 调整参数：
- `title`：应用名称
- `package.domain`：包名
- `android.api`：目标API级别
- `requirements`：Python依赖列表

#### 步骤3：执行打包
```bash
# 进入项目目录
cd precious-metal-price

# Debug版本（用于测试）
buildozer android debug deploy run

# Release版本（用于发布）
buildozer android release
```

#### 步骤4：获取APK
打包完成后，APK文件位于：
```
bin/
└── [package.name]-[version]-debug.apk
```

---

## ⚙️ 配置说明

### buildozer.spec 关键配置项

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `title` | 贵金属实时价格 | 应用显示名称 |
| `package.domain` | com.preciousmetal.price | 应用包名 |
| `source.dir` | . | 源代码目录 |
| `source.main` | main.py | 入口文件 |
| `android.permissions` | INTERNET,SYSTEM_ALERT_WINDOW | 权限声明 |
| `android.api` | 33 | 目标API（Android 13） |
| `android.minapi` | 21 | 最低API（Android 5.0） |
| `android.archs` | arm64-v8a,armeabi-v7a | 支持CPU架构 |
| `requirements` | python3,kivy,requests,... | Python依赖 |

### Android权限说明
- `INTERNET`：访问网络获取价格数据
- `SYSTEM_ALERT_WINDOW`：实现悬浮窗显示（必需）

---

## 📊 数据源说明

### 当前使用的API
1. **国际金价**：Metals.dev API（备用：汇率API）
2. **国内金价**：基于汇率计算（演示模式）

### 生产环境建议替换为
- 上海黄金交易所官方API
- 新浪财经/腾讯财经接口
- 自建后端代理服务

### 数据格式示例
```json
{
  "metals": {
    "gold": {
      "price": 1950.45,
      "change": 12.30,
      "change_percent": 0.63
    },
    "silver": {
      "price": 23.15,
      "change": -0.25,
      "change_percent": -1.07
    }
  }
}
```

---

## 🔒 安全与权限

### 必要权限
- **网络访问**：获取实时价格数据
- **悬浮窗权限**：Android 6.0+ 需用户手动授权

### 用户授权流程
1. 首次启动时申请悬浮窗权限
2. 引导用户至系统设置开启
3. 未授权时降级为普通Activity显示

### 隐私政策
- 仅收集必要的网络请求数据
- 不存储用户个人信息
- 不包含广告追踪SDK

---

## 🛠️ 常见问题

### Q: 打包失败提示缺少依赖？
```bash
# 清理缓存重试
buildozer android clean
buildozer android debug
```

### Q: APK安装失败？
- 检查是否开启"允许未知来源"
- 确认API级别符合设备系统版本
- 尝试使用Debug版本测试

### Q: 悬浮窗不显示？
- 检查是否授予"显示在其他应用上层"权限
- 部分ROM需在设置中单独开启

### Q: 价格数据不更新？
- 检查网络连接
- 确认API服务可用性
- 查看Logcat日志排查错误

### Q: 如何自定义UI颜色？
编辑 `main.py` 中的 `COLORS` 字典：
```python
COLORS = {
    'bg_dark': (0.102, 0.102, 0.180, 0.95),  # 背景
    'gold': (1.0, 0.843, 0.0, 1.0),           # 金色
    'white': (1.0, 1.0, 1.0, 1.0),            # 白色
    # ... 更多颜色定义
}
```

---

## 📈 性能优化建议

1. **减少刷新频率**
   - 国际价格改为3-5秒刷新
   - 国内价格改为60秒刷新

2. **离线缓存**
   - 本地SQLite缓存最近数据
   - 无网络时显示最后已知价格

3. **电量优化**
   - 屏幕关闭时暂停刷新
   - 使用AlarmManager替代定时器

4. **内存管理**
   - 及时释放图片资源
   - 避免内存泄漏

---

## 📝 更新日志

### v1.0.0 (2024-01-15)
- ✅ 初始版本发布
- ✅ 实现四项价格显示
- ✅ 悬浮窗拖拽与吸附
- ✅ 最小化/恢复功能
- ✅ 定时自动刷新
- ✅ 深色主题UI

---

## 📄 许可证

MIT License

Copyright (c) 2024 Precious Metal Price App

---

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

---

## 📞 技术支持

如遇问题，请提供以下信息：
- 操作系统及版本
- Python版本 (`python --version`)
- Buildozer版本 (`buildozer --version`)
- 完整错误日志

---

**⭐ 如果这个项目对您有帮助，请给个Star支持一下！**
