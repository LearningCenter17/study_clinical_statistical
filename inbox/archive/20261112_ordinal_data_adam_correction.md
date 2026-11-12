<!-- 来源：Li 粘贴的 Claude 对话回复（2026-11-12），针对 ordinal_data.md 中"AVALCAT / AVALN"写法的更正。已直接合并进 CON-ordinal-data。 -->

你说得对，是我写错了。`AVALN` 不是 BDS 标准变量，`AVAL` 本身就是数值型，`AVALCAT` 后面也漏了编号。

正确的对应关系：

- **`AVAL`**（Num）/ **`AVALC`**（Char）：分析值本身。对原生就是 ordinal 的参数（比如 mRS、ECOG、CGI-I），通常 `AVALC` 存文字类别，`AVAL` 存对应的有序数字编码。两者必须一一对应。
- **`AVALCATy`**（Char）/ **`AVALCAyN`**（Num）：对 `AVAL` 做的**派生分类**，y = 1, 2, …。主要用于把连续值切成有序类别，比如把 eGFR 分成 CKD 分期。`AVALCAyN` 用来保证排序。注意变量名是 `AVALCA1N`，不是 `AVALCAT1N`，这是为了遵守 8 字符的限制。

所以更准确的说法是：原生 ordinal 参数用 `AVAL` + `AVALC` 就够了；只有在从 `AVAL` 再派生分类时才用 `AVALCATy` + `AVALCAyN`。卡片里如果要写得更严谨，可以直接按这个区分来写，不用只标注"泛指"。
