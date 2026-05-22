# Claude Code KDP 精美封面生成指令

## 项目目标
- 为 Gen Z 哲学+心理学 KDP 书籍生成高质量封面
- 封面必须：
  - 商业出版感
  - 符合 Gen Z 审美
  - 情绪氛围与书籍内容一致
  - 三种风格方向：商业风、情绪风、极简风

---

## 必须安装的 GitHub 插件
1. **ComfyUI**  
   - Stable Diffusion 节点式工作流，生成高质量封面
2. **Fooocus**  
   - 自动优化 Prompt、构图、光影，适合 KDP 封面
3. **IPAdapter**  
   - 保持封面风格统一，参考优秀封面
4. **ControlNet**  
   - 控制人物姿态、构图，避免封面崩坏
5. **Stable Diffusion WebUI Forge（推荐）**  
   - 增强版 WebUI，运行更快、更稳定

---

## Claude Code 封面生成工作流

### 1. 分析书籍内容
- 提取核心情绪
- 提取主题关键词
- 确定视觉风格

### 2. 生成封面Prompt
- 正向 Prompt（构图、色彩、光影、字体布局）
- Negative Prompt（低质量、AI感、杂乱元素排除）

### 3. 输出三种封面方向
- 商业风  
- 情绪风  
- 极简风

---

## Prompt示例（商业风）
```
Cinematic, minimalist, modern editorial, Gen Z philosophical-psychology book cover, soft cinematic lighting, calm emotional tone, professional typography, clear title layout, clean background, premium illustration style
```

## Negative Prompt示例
```
low quality, blurry, extra limbs, bad anatomy, AI artifacts, plastic skin, cluttered composition, amateur, oversaturated, cartoonish, fantasy style
```

---

## 艺术方向
- 高级感、商业出版感
- 简洁构图，留白合理
- 情绪符合书中主题
- 哲学 + 心理学氛围

---

## 配色方案
- 商业风：蓝灰+白+黑  
- 情绪风：暗夜蓝+霓虹粉+灰色  
- 极简风：白底+黑线条+单色高光

---

## 字体方案
- 标题：现代无衬线、粗体  
- 副标题：简洁小字体  
- 作者名：清晰易读字体，保证商业风格

---

## 输出要求
- 每种封面方向生成：
  - `prompt.txt`  
  - `negative_prompt.txt`  
  - `art_direction.md`  
  - `typography.md`  
  - `color_palette.md`  
  - `composition.md`
- 确保封面风格与文章内容和目标读者一致

